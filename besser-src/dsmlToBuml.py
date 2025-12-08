import json
from structural_model import Community_description, Community_locale, User_avatarUrl, User_description, User_displayName, User_email, User_fullName, User_id, User_reputationScore, domain_model as structural_metamodel
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
    item_config = app_block['inputs']['ITEMCONFIG']['block']
    fields = item_config['fields']
    
    needs_transaction = False
    exchange_types = set()
    
    if 'ITEMEXCHANGE' in item_config.get('inputs', {}):
        current = item_config['inputs']['ITEMEXCHANGE']['block']
        while current:
            exchange_type = current['fields']['name']
            exchange_types.add(exchange_type)
            current = current.get('next', {}).get('block')
    
    if "Auction" in exchange_types:
        auction_class = structural_metamodel.get_class_by_name("Auction")
        bid_class = structural_metamodel.get_class_by_name("Bid")
        domain_model.add_type(auction_class)
        domain_model.add_type(bid_class)
        needs_transaction = True
        add_associations_for_class("Auction", structural_metamodel, domain_model)
        add_associations_for_class("Bid", structural_metamodel, domain_model)
    
    if "BuyNow" in exchange_types or "Free" in exchange_types:
        sale_class = structural_metamodel.get_class_by_name("Sale")
        domain_model.add_type(sale_class)
        needs_transaction = True
        add_associations_for_class("Sale", structural_metamodel, domain_model)
    
    if "Exchange" in exchange_types:
        exchange_class = structural_metamodel.get_class_by_name("Exchange")
        domain_model.add_type(exchange_class)
        needs_transaction = True
        add_associations_for_class("Exchange", structural_metamodel, domain_model)
    
    if needs_transaction:
        transaction_class = structural_metamodel.get_class_by_name("Transaction")
        domain_model.add_type(transaction_class)
        add_associations_for_class("Transaction", structural_metamodel, domain_model)
        
        # Add generalizations
        add_generalizations_for_class("Sale", structural_metamodel, domain_model)
        add_generalizations_for_class("Exchange", structural_metamodel, domain_model)
        add_generalizations_for_class("Auction", structural_metamodel, domain_model)
    
    # Handle categories
    if fields.get('enableItemCategories') == "True":
        category_class = structural_metamodel.get_class_by_name("Category")
        domain_model.add_type(category_class)
        add_associations_for_class("Category", structural_metamodel, domain_model)
        
    # TODO: other item config are not in the structural model
    
def build_features(app_block, domain_model: DomainModel):
    rules = app_block['inputs']['FEATURES']['block']['fields']
    if rules['enableChat'] == "True":
        domain_model.add_type(structural_metamodel.get_class_by_name("ChatThread"))
        domain_model.add_type(structural_metamodel.get_class_by_name("Message"))
        add_associations_for_class("ChatThread", structural_metamodel, domain_model)
        add_associations_for_class("Message", structural_metamodel, domain_model)
        
    if rules['enableRatings'] == "True":
        domain_model.add_type(structural_metamodel.get_class_by_name("Review"))
        domain_model.get_class_by_name("User").add_attribute(User_reputationScore)
        add_associations_for_class("Review", structural_metamodel, domain_model)

    if rules['moderationMode'] == "ReportOnly":
        domain_model.add_type(structural_metamodel.get_class_by_name("Report"))
        add_associations_for_class("Report", structural_metamodel, domain_model)
    
    # TODO: These are not defined in the structural model
    if rules['enableAnalytics']:
        pass
    if rules['enableNotifications']:
        pass
    if rules['authMode']:
        pass

def build_community(app_block, domain_model: DomainModel):
    # TODO: community struct model vs dsml are mismatched
    pass
def build_community_fields(app_block, domain_model: DomainModel):
    community_fields = app_block['inputs']['COMMUNITY_FIELDS']['block']['fields']
    community_class = domain_model.get_class_by_name("Community")
    
    if community_class:
        current_attrs = community_class.all_attributes()
        
        if community_fields.get('locale') != "True":
            current_attrs.discard(Community_locale)
        if community_fields.get('description') != "True":
            current_attrs.discard(Community_description)
        # Update attributes
        community_class.attributes = current_attrs

def build_theme_config(app_block, domain_model: DomainModel):
    # TODO: Not reflected in structural model
    pass
def build_user(app_block, domain_model: DomainModel):
    user_fields = app_block['inputs']['USER_FIELDS_LIST']['block']['fields']
    User = structural_metamodel.get_class_by_name("User")
    base_attributes = {User_id, User_email, User_displayName, User_avatarUrl, User_description}

    optional_fields = {
        "full_name": User_fullName,
        # TODO: nickname address and age are not in the structural model

    }
    for key, prop in optional_fields.items():
        if user_fields.get(key) == "True":
            base_attributes.add(prop)
    # reputationScore in build_features

    User.attributes = {attr for attr in User.attributes if attr in base_attributes}
    domain_model.add_type(User)

def add_associations_for_class(class_name, domain_model: DomainModel, new_domain_model: DomainModel):
    for assoc in domain_model.associations:
        # Check if any assoc references class
        involved = False
        for end in assoc.ends:
            if end.type.name == class_name:
                involved = True
                break
        
        if involved:
            # Check if all classes in assoc are in the new model
            all_present = True
            for end in assoc.ends:
                if new_domain_model.get_class_by_name(end.type.name) is None:
                    all_present = False
                    break
            if all_present and assoc not in new_domain_model.associations:
                new_domain_model.associations.add(assoc)

def add_generalizations_for_class(class_name, domain_model: DomainModel, new_domain_model: DomainModel):
    for gen in domain_model.generalizations:
        if gen.specific.name == class_name or gen.general.name == class_name:
            # Check if both general and specific are in the new model
            if (new_domain_model.get_class_by_name(gen.general.name) is not None and
                new_domain_model.get_class_by_name(gen.specific.name) is not None):
                if gen not in new_domain_model.generalizations:
                    new_domain_model.generalizations.add(gen)

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
    
    add_associations_for_class("User", structural_metamodel, new_domain_model)
    add_associations_for_class("Community", structural_metamodel, new_domain_model)
    add_associations_for_class("Item", structural_metamodel, new_domain_model)
    add_associations_for_class("PhotoUrl", structural_metamodel, new_domain_model)
    add_associations_for_class("Membership", structural_metamodel, new_domain_model)
    
    # Use api to parse DSML 
    # https://besser.readthedocs.io/en/latest/api/BUML/metamodel/api_structural.html
    build_item_config(app_block,new_domain_model)
    build_features(app_block,new_domain_model)
    build_community(app_block,new_domain_model)
    build_community_fields(app_block,new_domain_model)
    build_theme_config(app_block,new_domain_model)
    
    print(f"Domain Model: {new_domain_model.name}")
    print(f"\nClasses ({len(new_domain_model.get_classes())}):")
    for cls in new_domain_model.get_classes():
        print(f"  - {cls.name}")
    
    print(f"\nAssociations ({len(new_domain_model.associations)}):")
    for assoc in new_domain_model.associations:
        print(f"  - {assoc.name}")
    
    print(f"\nGeneralizations ({len(new_domain_model.generalizations)}):")
    for gen in new_domain_model.generalizations:
        print(f"  - {gen.specific.name} -> {gen.general.name}")
    
    print(f"\nUser attributes:")
    user = new_domain_model.get_class_by_name("User")
    if user:
        for attr in user.attributes:
            print(f"  - {attr.name}: {attr.type}")
            
    # Validation
    result_dict = new_domain_model.validate(True)
    if result_dict['success']:
        print("\nDomain model is valid.")        
