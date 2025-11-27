import json
from besser.BUML.metamodel.structural.structural import DomainModel
from structural_model import domain_model as structural_model


def extract_app_block(data):
    blocks = data.get('blocks').get('blocks')
    app_custom_block = next((b for b in blocks if b['type'] == 'AppCustomization'), None)
    
    if not app_custom_block:
        raise ValueError("No AppCustomization block found")
    
    return app_custom_block

def build_types(app_block, domain_model):
    pass
def build_associations(app_block, domain_model):
    pass
def build_generalizations(app_block, domain_model):
    pass

if __name__ == "__main__":
    with open('pipeline.json', 'r') as f:
        config = json.load(f)
        
    app_block = extract_app_block(config)

    new_domain_model = DomainModel(name=app_block.get('fields').get('name', ""))
    # Use api to parse DSML 
    # https://besser.readthedocs.io/en/latest/api/BUML/metamodel/api_structural.html
    build_types(app_block,new_domain_model)
    build_associations(app_block, new_domain_model)
    build_generalizations(app_block,new_domain_model)
    
    