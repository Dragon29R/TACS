import os
import re
import json
from besser.generators import GeneratorInterface
from besser.BUML.metamodel.structural import DomainModel, Class
from jinja2 import Environment, FileSystemLoader

# Assuming 'self.model' is an object that contains a list or dictionary of classes/components
# and likely has a structure where components have a 'name' attribute.

def rename_component(model, old_name, new_name):
    """
    Renames a component in the gui_model.
    This effectively "removes" it from the template's visibility 
    if the template checks for the old_name.
    """
    # If get_class_by_name returns the actual component object:
    component = model.get_class_by_name(old_name)
    
    if component:
        # Change the name attribute
        component.name = new_name
        print(f"Renamed '{old_name}' to '{new_name}'.")
    else:
        print(f"Component '{old_name}' not found.")

class GuiGenerator(GeneratorInterface):
    def __init__(self, model: DomainModel, output_dir: str, dsml_config: dict, template_dir: str, mocks_dir: str = None):
        super().__init__(model, output_dir=output_dir)
        self.dsml_config = dsml_config
        self.template_dir = template_dir
        self.mocks_dir = mocks_dir
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
        base_name = file_name.replace('_screen', '')
        file_name = f"{base_name}.html"
        template_name = f"{file_name}.jinja2"

        try:
            if not os.path.exists(os.path.join(self.template_dir, template_name)):
                print(f"Error: Template not found for {screen.name}: {template_name}")
                return

            template = self.env.get_template(template_name)
            
            # Load mock data
            mock_data = {}
            if self.mocks_dir:
                mock_file = os.path.join(self.mocks_dir, f"{base_name}.json")
                if os.path.exists(mock_file):
                    try:
                        with open(mock_file, 'r', encoding='utf-8') as f:
                            mock_data = json.load(f)
                        print(f"- Loaded mock data from {mock_file}")
                    except Exception as e:
                        print(f"- Warning: Failed to load mock data: {e}")

            #rename_component(self.model, "SaleDetailsComponent", "SaleDetailsComponent_HIDDEN")
            #rename_component(self.model, "AuctionDetailsComponent", "AuctionDetailsComponent_HIDDEN")
            #rename_component(self.model, "MainImageComponent", "MainImageComponent_HIDDEN")


            context = {
                "screen": screen, # Class API used for interaction in templates
                "gui_model": self.model, 
                "dsml": self.dsml_config, # Dictionary with DSML config
                "data": mock_data # Mock data
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