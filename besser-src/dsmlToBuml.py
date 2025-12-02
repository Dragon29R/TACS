import json
from structural_model import domain_model as structural_metamodel
from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)


def extract_app_block(data):
    blocks = data.get('blocks').get('blocks')
    app_custom_block = next((b for b in blocks if b['type'] == 'AppCustomization'), None)
    
    if not app_custom_block:
        raise ValueError("No AppCustomization block found")
    
    return app_custom_block

def build_item_config(app_block, domain_model):
    pass
def build_features(app_block, domain_model):
    rules = app_block['inputs']['FEATURES']['block']['fields']
    print(rules['enableChat'])
    if rules['enableChat']:
        domain_model.add_type(structural_metamodel.get_class_by_name("ChatThread"))
    if rules['enableRatings']:
        domain_model.add_type(structural_metamodel.get_class_by_name("Review"))
    if rules['enableNotifications']:
        pass
    if rules['moderationMode'] == "ReportOnly":
        domain_model.add_type(structural_metamodel.get_class_by_name("Report"))
        pass
    if rules['enableAnalytics']:
        pass
    
    pass
def build_community(app_block, domain_model):
    pass
def build_community_fields(app_block, domain_model):
    pass
def build_theme_config(app_block, domain_model):
    pass
def build_user(app_block, domain_model):
    pass

if __name__ == "__main__":
    with open('DSML_model.json', 'r') as f:
        config = json.load(f)
        
    app_block = extract_app_block(config)

    new_domain_model = DomainModel(name=app_block.get('fields').get('name', ""))
    
    #default classes
    new_domain_model.add_type(structural_metamodel.get_class_by_name("User"))
    new_domain_model.add_type(structural_metamodel.get_class_by_name("Community"))
    new_domain_model.add_type(structural_metamodel.get_class_by_name("Item"))
    new_domain_model.add_type(structural_metamodel.get_class_by_name("PhotoUrl"))
    new_domain_model.add_type(structural_metamodel.get_class_by_name("Role"))
    
    
    # Use api to parse DSML 
    # https://besser.readthedocs.io/en/latest/api/BUML/metamodel/api_structural.html
    build_item_config(app_block,new_domain_model)
    build_features(app_block,new_domain_model)
    build_community(app_block,new_domain_model)
    build_community_fields(app_block,new_domain_model)
    build_theme_config(app_block,new_domain_model)
    build_user(app_block,new_domain_model)
    