from besser.generators.generator_interface import GeneratorInterface
from jinja2 import Environment, FileSystemLoader

class GuiGenerator(GeneratorInterface):
    def __init__(self, model, dsml_config, output_dir, template_dir):
        super().__init__(model, output_dir=output_dir)
        self.dsml_config = dsml_config
        self.template_dir = template_dir
        self.env = Environment(loader=FileSystemLoader(self.template_dir))

    def generate(self):
        raise NotImplementedError
