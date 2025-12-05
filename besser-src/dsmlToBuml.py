import json
from structural_model import User_reputationScore, domain_model as structural_metamodel
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

def build_item_config(app_block, domain_model: DomainModel):
    pass
def build_features(app_block, domain_model: DomainModel):
    rules = app_block['inputs']['FEATURES']['block']['fields']
    if rules['enableChat'] == "True":
        domain_model.add_type(structural_metamodel.get_class_by_name("ChatThread"))
        domain_model.add_type(structural_metamodel.get_class_by_name("Message"))
    if rules['enableRatings'] == "True":
        domain_model.add_type(structural_metamodel.get_class_by_name("Review"))
        domain_model.get_class_by_name("User").add_attribute(User_reputationScore)
    if rules['moderationMode'] == "ReportOnly":
        domain_model.add_type(structural_metamodel.get_class_by_name("Report"))
    if rules['enableAnalytics']:
        pass
    if rules['enableNotifications']:
        pass
    if rules['authMode']:
        pass

def build_community(app_block, domain_model: DomainModel):
    pass
def build_community_fields(app_block, domain_model: DomainModel):
    pass
def build_theme_config(app_block, domain_model: DomainModel):
    pass
def build_user(app_block, domain_model: DomainModel):
    attributes_set: set[Property] = structural_metamodel.get_class_by_name("User").all_attributes()
    attributes_set.remove(User_reputationScore)
    methods_set: set[Method] = structural_metamodel.get_class_by_name("User").methods
    User = Class(name="User", attributes= attributes_set, methods= methods_set)
    domain_model.add_type(User)

if __name__ == "__main__":
    with open('DSML_model.json', 'r') as f:
        config = json.load(f)
        
    app_block = extract_app_block(config)

    new_domain_model:DomainModel = DomainModel(name=app_block.get('fields').get('name', ""))
    
    #default classes
    build_user(app_block, new_domain_model)
    new_domain_model.add_type(structural_metamodel.get_class_by_name("Community"))
    new_domain_model.add_type(structural_metamodel.get_class_by_name("Item"))
    new_domain_model.add_type(structural_metamodel.get_class_by_name("PhotoUrl"))
    new_domain_model.add_type(structural_metamodel.get_class_by_name("Membership"))
    
    
    # Use api to parse DSML 
    # https://besser.readthedocs.io/en/latest/api/BUML/metamodel/api_structural.html
    build_item_config(app_block,new_domain_model)
    build_features(app_block,new_domain_model)
    build_community(app_block,new_domain_model)
    build_community_fields(app_block,new_domain_model)
    build_theme_config(app_block,new_domain_model)
    
#    for cls in new_domain_model.get_classes():
#        if cls.name == "User":
#            print(cls.attributes)
