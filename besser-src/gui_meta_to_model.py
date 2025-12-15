import json
from gui_metamodel import domain_model as gui_metamodel
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

def add_gui_associations_for_class(class_name, source_model: DomainModel, target_model: DomainModel):
    for assoc in source_model.associations:
        # Check if any assoc end references the class
        involved = False
        for end in assoc.ends:
            if end.type.name == class_name:
                involved = True
                break
        
        if involved:
            # Check if all classes in assoc are in the target model
            all_present = True
            for end in assoc.ends:
                if target_model.get_class_by_name(end.type.name) is None:
                    all_present = False
                    break
            if all_present and assoc not in target_model.associations:
                target_model.associations.add(assoc)

def add_gui_elements(element_names, gui_model, gui_metamodel):
    for name in element_names:
        element = gui_metamodel.get_class_by_name(name)
        if element:
            gui_model.add_type(element)
            add_gui_associations_for_class(name, gui_metamodel, gui_model)

def build_core_gui(gui_model: DomainModel):
    """Elements that are always present in the GUI"""
    add_gui_elements(["Frontend", "CommonScreen"], gui_model, gui_metamodel)
    core_screens = [
        "HomeScreen",
        "LoginScreen",
        "ProfileScreen",
        "ListingsScreen",
        "ListingDetailsScreen",
        "CreateListingScreen",
        "NotFoundScreen",
        "TransactionHistoryScreen"
    ]
    add_gui_elements(core_screens, gui_model, gui_metamodel)
    core_components = [
        "TopBarComponent",
        "AppPresentationComponent",
        "FooterComponent",
        "ProfileContentsComponent",
        "EditProfileButton",
        "UsernameField",
        "PasswordField",
        "LoginButton",
        "ListingsListComponent",
        "EnterListingComponent",
        "ListingsFilterButton",
        "TransactionListComponent",
        "TransactionCardComponent",
        "ImageGalleryComponent",
        "MainImageComponent",
        "ProductTitleLabel",
        "ProductDescriptionLabel",
        "ProfileButton",
        "LogoutButton",
        "MenuButton"
    ]

    # Mandatory listing components
    add_gui_elements(core_components, gui_model, gui_metamodel)
    listing_form_components = [
        "ProductTitleField",
        "ProductDescriptionField",
        "SubmitListingButton",
        "ListingTypeSelector",
        "CheckboxesComponent"
    ]
    add_gui_elements(listing_form_components, gui_model, gui_metamodel)

def build_exchange_type_gui(app_block, gui_model: DomainModel):
    item_config = app_block['inputs']['ITEMCONFIG']['block']
    
    exchange_types = set()
    
    # Extract from DSML
    if 'ITEMEXCHANGE' in item_config.get('inputs', {}):
        current = item_config['inputs']['ITEMEXCHANGE']['block']
        while current:
            exchange_type = current['fields']['name']
            exchange_types.add(exchange_type)
            current = current.get('next', {}).get('block')
    
    if "Auction" in exchange_types:
        auction_components = [
            "AuctionCardComponent",
            "AuctionDetailsComponent",
            "BidField",
            "BidNowButton",
            "AuctionCheckbox",
            "AuctionClosingTimeField",
            "ViewAuctionsButton"
        ]
        add_gui_elements(auction_components, gui_model, gui_metamodel)
    if "BuyNow" in exchange_types or "Free" in exchange_types:
        sale_components = [
            "SaleCardComponent",
            "SaleDetailsComponent",
            "BuyNowButton",
            "PriceLabel",
            "SaleCheckbox",
            "PriceField",
            "ViewSalesButton"
        ]
        add_gui_elements(sale_components, gui_model, gui_metamodel)
    if "Exchange" in exchange_types:
        exchange_components = [
            "ExchangeCardComponent",
            "ExchangeDetailsComponent",
            "ExchangeNowButton",
            "ExchangeCheckbox",
            "PreferedExchangeTypeField",
            "ProposedExchangeField",
            "ViewExchangesButton"
        ]
        add_gui_elements(exchange_components, gui_model, gui_metamodel)

def build_features_gui(app_block, gui_model: DomainModel):
    features = app_block['inputs']['FEATURES']['block']['fields']
    
    if features.get('enableChat') == "True":
        chat_components = [
            "ChatScreen",
            "MessageListComponent",
            "NewMessageField",
            "SendButton",
            "MessageCardComponent"
        ]
        add_gui_elements(chat_components, gui_model, gui_metamodel)
    if features.get('enableRatings') == "True":
        review_components = [
            "ReviewScreen",
            "NewReviewFormComponent",
            "ReviewListComponent",
            "ReviewCardComponent"
        ]
        add_gui_elements(review_components, gui_model, gui_metamodel)
    if features.get('moderationMode') == "ReportOnly":
        report_components = [
            "ReportScreen",
            "NewReportFormComponent",
            "ReportCardComponent",
            "ReportManagementComponent"
        ]
        add_gui_elements(report_components, gui_model, gui_metamodel)

def build_item_config_gui(app_block, gui_model: DomainModel):
    item_config = app_block['inputs']['ITEMCONFIG']['block']['fields']
    
    if item_config.get('enableItemLocation') == "True":
        add_gui_elements(["LocationField"], gui_model, gui_metamodel)
    
    max_photos = item_config.get('maxItemPhotos', '1')
    try:
        max_photos_int = int(max_photos) if max_photos else 1
    except (ValueError, TypeError):
        max_photos_int = 1
    
    if max_photos_int > 1:
        add_gui_elements(["MultipleImagesUploadComponent"], gui_model, gui_metamodel)
    else:
        add_gui_elements(["SingleImageUploadComponent"], gui_model, gui_metamodel)

def create_gui_model_from_dsml(dsml_path: str) -> DomainModel:
    with open(dsml_path, 'r') as f:
        config = json.load(f)
    
    app_block = extract_app_block(config)
    
    gui_model = DomainModel(name=f"{app_block.get('fields').get('name', 'App')}")
    build_core_gui(gui_model)
    build_exchange_type_gui(app_block, gui_model)
    build_features_gui(app_block, gui_model)
    build_item_config_gui(app_block, gui_model)
    
    return gui_model

if __name__ == "__main__":
    dsml_path = 'DSML_model.json'
    gui_model = create_gui_model_from_dsml(dsml_path)
    
    print(f"GUI Model: {gui_model.name}")
    print(f"\nClasses ({len(gui_model.get_classes())}):")
    for cls in sorted(gui_model.get_classes(), key=lambda c: c.name):
        print(f"  - {cls.name}")
    
    print(f"\nAssociations ({len(gui_model.associations)}):")
    for assoc in sorted(gui_model.associations, key=lambda a: a.name):
        print(f"  - {assoc.name}")
    
    # Group classes by type
    screens = [c for c in gui_model.get_classes() if c.name.endswith("Screen")]
    components = [c for c in gui_model.get_classes() if c.name.endswith("Component")]
    fields = [c for c in gui_model.get_classes() if c.name.endswith("Field")]
    buttons = [c for c in gui_model.get_classes() if c.name.endswith("Button")]
    others = [c for c in gui_model.get_classes() 
              if not any(c.name.endswith(suffix) for suffix in ["Screen", "Component", "Field", "Button"])]
    
    print(f"Screens ({len(screens)}): {', '.join(sorted(c.name for c in screens))}")
    print(f"Components ({len(components)}): {', '.join(sorted(c.name for c in components))}")
    print(f"Fields ({len(fields)}): {', '.join(sorted(c.name for c in fields))}")
    print(f"Buttons ({len(buttons)}): {', '.join(sorted(c.name for c in buttons))}")
    if others:
        print(f"Others ({len(others)}): {', '.join(sorted(c.name for c in others))}")
    
    # validation
    result_dict = gui_model.validate()
    if result_dict['success']:
        print("\nGUI model is valid.")
