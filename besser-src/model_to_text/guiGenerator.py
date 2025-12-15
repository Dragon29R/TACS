import os
import re
from besser.generators import GeneratorInterface
from besser.BUML.metamodel.structural import DomainModel, Class
from jinja2 import Environment, FileSystemLoader

class GuiGenerator(GeneratorInterface):
    def __init__(self, model: DomainModel, output_dir: str, dsml_config: dict, template_dir: str):
        super().__init__(model, output_dir=output_dir)
        self.dsml_config = dsml_config
        self.template_dir = template_dir
        self.env = Environment(loader=FileSystemLoader(self.template_dir))

    def generate(self, *args):
        print(f"Outputing to: {self.output_dir}")
        os.makedirs(self.output_dir, exist_ok=True)
        
        screens = []
        if isinstance(self.model, DomainModel):
            screens = [cls for cls in self.model.get_classes() if cls.name.endswith('Screen')]
        else:
            print(f"Warning: Model type not supported.")
            
        if not screens:
            print("Warning: No screens in model")

        for screen in screens:
            self._generate_screen(screen)
            
    def _generate_screen(self, screen: Class):
        """
        Generates a HTML page for a given Screen class
        """
        file_name = self._camel_to_snake(screen.name)
        file_name = file_name.replace('_screen', '') + ".html"
        # LoginScreen -> login.html.jinja2
        template_name = f"{file_name}.jinja2"

        try:
            if not os.path.exists(os.path.join(self.template_dir, template_name)):
                print(f"Error: Template not found for {screen.name}: {template_name}")
                return

            template = self.env.get_template(template_name)
            context = {
                "screen": screen, # Class API used for interaction in templates
                "dsml": self.dsml_config # Dictionary with DSML config
            }

            rendered_content = template.render(**context)
            
            output_path = os.path.join(self.output_dir, file_name)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(rendered_content)
            
            print(f"Generated: {output_path}")

        except Exception as e:
            print(f"Error: Failed to generate {screen.name}: {e}")

    def _camel_to_snake(self, name):
        name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()