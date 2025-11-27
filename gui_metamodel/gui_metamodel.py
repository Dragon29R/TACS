####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
Test123(GUIModel) = Class(name="Test123(GUIModel)")
Module(Module) = Class(name="Module(Module)")
ChatScreen(Screen) = Class(name="ChatScreen(Screen)")
LoginScreen(Screen) = Class(name="LoginScreen(Screen)")
HomeScreen(Screen) = Class(name="HomeScreen(Screen)")
ListingDetailsScreen(Screen) = Class(name="ListingDetailsScreen(Screen)")
CreateListeningScreen(Screen) = Class(name="CreateListeningScreen(Screen)")
AuctionScreen(Screen) = Class(name="AuctionScreen(Screen)")
ProfileScreen(Screen) = Class(name="ProfileScreen(Screen)")
InputField(InputField) = Class(name="InputField(InputField)")
SendButton(Button) = Class(name="SendButton(Button)")
MessageList(ViewContainer) = Class(name="MessageList(ViewContainer)")
UsernameField(InputField) = Class(name="UsernameField(InputField)")
PasswordField(InputField) = Class(name="PasswordField(InputField)")
LoginButton(Button) = Class(name="LoginButton(Button)")
MainMenu(Menu) = Class(name="MainMenu(Menu)")
ProfileButton(Button) = Class(name="ProfileButton(Button)")
HomeLogoutButton(Button) = Class(name="HomeLogoutButton(Button)")
ProfileMenu(Menu) = Class(name="ProfileMenu(Menu)")
EditProfileButton(Button) = Class(name="EditProfileButton(Button)")
ProfileLogoutButton(Button) = Class(name="ProfileLogoutButton(Button)")
ImageGallery(Image) = Class(name="ImageGallery(Image)")
TitleLabel(Label) = Class(name="TitleLabel(Label)")
PriceLabel(Label) = Class(name="PriceLabel(Label)")
BidInput(InputField) = Class(name="BidInput(InputField)")
BidButton(Button) = Class(name="BidButton(Button)")
BuyNowButton(Button) = Class(name="BuyNowButton(Button)")
TitleField(InputField) = Class(name="TitleField(InputField)")
DescriptionField(InputField) = Class(name="DescriptionField(InputField)")
PriceField(InputField) = Class(name="PriceField(InputField)")
ImageUpload(InputField) = Class(name="ImageUpload(InputField)")
SubmitButton(Button) = Class(name="SubmitButton(Button)")
AuctionList(ViewContainer) = Class(name="AuctionList(ViewContainer)")
FilterMenu(Menu) = Class(name="FilterMenu(Menu)")
EnterAuctionButton(Button) = Class(name="EnterAuctionButton(Button)")

# Test123(GUIModel) class attributes and methods

# Module(Module) class attributes and methods

# ChatScreen(Screen) class attributes and methods

# LoginScreen(Screen) class attributes and methods

# HomeScreen(Screen) class attributes and methods

# ListingDetailsScreen(Screen) class attributes and methods

# CreateListeningScreen(Screen) class attributes and methods

# AuctionScreen(Screen) class attributes and methods

# ProfileScreen(Screen) class attributes and methods

# InputField(InputField) class attributes and methods

# SendButton(Button) class attributes and methods

# MessageList(ViewContainer) class attributes and methods

# UsernameField(InputField) class attributes and methods

# PasswordField(InputField) class attributes and methods

# LoginButton(Button) class attributes and methods

# MainMenu(Menu) class attributes and methods

# ProfileButton(Button) class attributes and methods

# HomeLogoutButton(Button) class attributes and methods

# ProfileMenu(Menu) class attributes and methods

# EditProfileButton(Button) class attributes and methods

# ProfileLogoutButton(Button) class attributes and methods

# ImageGallery(Image) class attributes and methods

# TitleLabel(Label) class attributes and methods

# PriceLabel(Label) class attributes and methods

# BidInput(InputField) class attributes and methods

# BidButton(Button) class attributes and methods

# BuyNowButton(Button) class attributes and methods

# TitleField(InputField) class attributes and methods

# DescriptionField(InputField) class attributes and methods

# PriceField(InputField) class attributes and methods

# ImageUpload(InputField) class attributes and methods

# SubmitButton(Button) class attributes and methods

# AuctionList(ViewContainer) class attributes and methods

# FilterMenu(Menu) class attributes and methods

# EnterAuctionButton(Button) class attributes and methods

# Relationships
ListingDetailsScreen(Screen)_Module(Module): BinaryAssociation = BinaryAssociation(
    name="ListingDetailsScreen(Screen)_Module(Module)",
    ends={
        Property(name="listingdetailsscreen(screen)", type=ListingDetailsScreen(Screen), multiplicity=Multiplicity(1, 1)),
        Property(name="module(module)", type=Module(Module), multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ProfileScreen(Screen)_Module(Module): BinaryAssociation = BinaryAssociation(
    name="ProfileScreen(Screen)_Module(Module)",
    ends={
        Property(name="profilescreen(screen)", type=ProfileScreen(Screen), multiplicity=Multiplicity(1, 1)),
        Property(name="module(module)_1", type=Module(Module), multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
LoginScreen(Screen)_Module(Module): BinaryAssociation = BinaryAssociation(
    name="LoginScreen(Screen)_Module(Module)",
    ends={
        Property(name="loginscreen(screen)", type=LoginScreen(Screen), multiplicity=Multiplicity(1, 1)),
        Property(name="module(module)_2", type=Module(Module), multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ChatScreen(Screen)_Module(Module): BinaryAssociation = BinaryAssociation(
    name="ChatScreen(Screen)_Module(Module)",
    ends={
        Property(name="chatscreen(screen)", type=ChatScreen(Screen), multiplicity=Multiplicity(1, 1)),
        Property(name="module(module)_3", type=Module(Module), multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
UsernameField(InputField)_LoginScreen(Screen): BinaryAssociation = BinaryAssociation(
    name="UsernameField(InputField)_LoginScreen(Screen)",
    ends={
        Property(name="loginscreen(screen)_1", type=LoginScreen(Screen), multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="usernamefield(inputfield)", type=UsernameField(InputField), multiplicity=Multiplicity(1, 1))
    }
)
CreateListeningScreen(Screen)_Module(Module): BinaryAssociation = BinaryAssociation(
    name="CreateListeningScreen(Screen)_Module(Module)",
    ends={
        Property(name="createlisteningscreen(screen)", type=CreateListeningScreen(Screen), multiplicity=Multiplicity(1, 1)),
        Property(name="module(module)_4", type=Module(Module), multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
PasswordField(InputField)_LoginScreen(Screen): BinaryAssociation = BinaryAssociation(
    name="PasswordField(InputField)_LoginScreen(Screen)",
    ends={
        Property(name="passwordfield(inputfield)", type=PasswordField(InputField), multiplicity=Multiplicity(1, 1)),
        Property(name="loginscreen(screen)_2", type=LoginScreen(Screen), multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
AuctionScreen(Screen)_Module(Module): BinaryAssociation = BinaryAssociation(
    name="AuctionScreen(Screen)_Module(Module)",
    ends={
        Property(name="auctionscreen(screen)", type=AuctionScreen(Screen), multiplicity=Multiplicity(1, 1)),
        Property(name="module(module)_5", type=Module(Module), multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
LoginButton(Button)_LoginScreen(Screen): BinaryAssociation = BinaryAssociation(
    name="LoginButton(Button)_LoginScreen(Screen)",
    ends={
        Property(name="loginbutton(button)", type=LoginButton(Button), multiplicity=Multiplicity(1, 1)),
        Property(name="loginscreen(screen)_3", type=LoginScreen(Screen), multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
HomeScreen(Screen)_Module(Module): BinaryAssociation = BinaryAssociation(
    name="HomeScreen(Screen)_Module(Module)",
    ends={
        Property(name="homescreen(screen)", type=HomeScreen(Screen), multiplicity=Multiplicity(1, 1)),
        Property(name="module(module)_6", type=Module(Module), multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
MainMenu(Menu)_HomeScreen(Screen): BinaryAssociation = BinaryAssociation(
    name="MainMenu(Menu)_HomeScreen(Screen)",
    ends={
        Property(name="mainmenu(menu)", type=MainMenu(Menu), multiplicity=Multiplicity(1, 1)),
        Property(name="homescreen(screen)_1", type=HomeScreen(Screen), multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
SendButton(Button)_ChatScreen(Screen): BinaryAssociation = BinaryAssociation(
    name="SendButton(Button)_ChatScreen(Screen)",
    ends={
        Property(name="sendbutton(button)", type=SendButton(Button), multiplicity=Multiplicity(1, 1)),
        Property(name="chatscreen(screen)_1", type=ChatScreen(Screen), multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ProfileButton(Button)_HomeScreen(Screen): BinaryAssociation = BinaryAssociation(
    name="ProfileButton(Button)_HomeScreen(Screen)",
    ends={
        Property(name="profilebutton(button)", type=ProfileButton(Button), multiplicity=Multiplicity(1, 1)),
        Property(name="homescreen(screen)_2", type=HomeScreen(Screen), multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
InputField(InputField)_ChatScreen(Screen): BinaryAssociation = BinaryAssociation(
    name="InputField(InputField)_ChatScreen(Screen)",
    ends={
        Property(name="inputfield(inputfield)", type=InputField(InputField), multiplicity=Multiplicity(1, 1)),
        Property(name="chatscreen(screen)_2", type=ChatScreen(Screen), multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
HomeLogoutButton(Button)_HomeScreen(Screen): BinaryAssociation = BinaryAssociation(
    name="HomeLogoutButton(Button)_HomeScreen(Screen)",
    ends={
        Property(name="homelogoutbutton(button)", type=HomeLogoutButton(Button), multiplicity=Multiplicity(1, 1)),
        Property(name="homescreen(screen)_3", type=HomeScreen(Screen), multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
MessageList(ViewContainer)_ChatScreen(Screen): BinaryAssociation = BinaryAssociation(
    name="MessageList(ViewContainer)_ChatScreen(Screen)",
    ends={
        Property(name="messagelist(viewcontainer)", type=MessageList(ViewContainer), multiplicity=Multiplicity(1, 1)),
        Property(name="chatscreen(screen)_3", type=ChatScreen(Screen), multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ProfileMenu(Menu)_ProfileScreen(Screen): BinaryAssociation = BinaryAssociation(
    name="ProfileMenu(Menu)_ProfileScreen(Screen)",
    ends={
        Property(name="profilemenu(menu)", type=ProfileMenu(Menu), multiplicity=Multiplicity(1, 1)),
        Property(name="profilescreen(screen)_1", type=ProfileScreen(Screen), multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
BidInput(InputField)_ListingDetailsScreen(Screen): BinaryAssociation = BinaryAssociation(
    name="BidInput(InputField)_ListingDetailsScreen(Screen)",
    ends={
        Property(name="bidinput(inputfield)", type=BidInput(InputField), multiplicity=Multiplicity(1, 1)),
        Property(name="listingdetailsscreen(screen)_4", type=ListingDetailsScreen(Screen), multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
EditProfileButton(Button)_ProfileScreen(Screen): BinaryAssociation = BinaryAssociation(
    name="EditProfileButton(Button)_ProfileScreen(Screen)",
    ends={
        Property(name="editprofilebutton(button)", type=EditProfileButton(Button), multiplicity=Multiplicity(1, 1)),
        Property(name="profilescreen(screen)_2", type=ProfileScreen(Screen), multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
BidButton(Button)_ListingDetailsScreen(Screen): BinaryAssociation = BinaryAssociation(
    name="BidButton(Button)_ListingDetailsScreen(Screen)",
    ends={
        Property(name="bidbutton(button)", type=BidButton(Button), multiplicity=Multiplicity(1, 1)),
        Property(name="listingdetailsscreen(screen)_5", type=ListingDetailsScreen(Screen), multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ProfileLogoutButton(Button)_ProfileScreen(Screen): BinaryAssociation = BinaryAssociation(
    name="ProfileLogoutButton(Button)_ProfileScreen(Screen)",
    ends={
        Property(name="profilelogoutbutton(button)", type=ProfileLogoutButton(Button), multiplicity=Multiplicity(1, 1)),
        Property(name="profilescreen(screen)_3", type=ProfileScreen(Screen), multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
BuyNowButton(Button)_ListingDetailsScreen(Screen): BinaryAssociation = BinaryAssociation(
    name="BuyNowButton(Button)_ListingDetailsScreen(Screen)",
    ends={
        Property(name="buynowbutton(button)", type=BuyNowButton(Button), multiplicity=Multiplicity(1, 1)),
        Property(name="listingdetailsscreen(screen)_6", type=ListingDetailsScreen(Screen), multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ImageGallery(Image)_ListingDetailsScreen(Screen): BinaryAssociation = BinaryAssociation(
    name="ImageGallery(Image)_ListingDetailsScreen(Screen)",
    ends={
        Property(name="imagegallery(image)", type=ImageGallery(Image), multiplicity=Multiplicity(1, 1)),
        Property(name="listingdetailsscreen(screen)_1", type=ListingDetailsScreen(Screen), multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
TitleField(InputField)_CreateListeningScreen(Screen): BinaryAssociation = BinaryAssociation(
    name="TitleField(InputField)_CreateListeningScreen(Screen)",
    ends={
        Property(name="titlefield(inputfield)", type=TitleField(InputField), multiplicity=Multiplicity(1, 1)),
        Property(name="createlisteningscreen(screen)_1", type=CreateListeningScreen(Screen), multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
TitleLabel(Label)_ListingDetailsScreen(Screen): BinaryAssociation = BinaryAssociation(
    name="TitleLabel(Label)_ListingDetailsScreen(Screen)",
    ends={
        Property(name="titlelabel(label)", type=TitleLabel(Label), multiplicity=Multiplicity(1, 1)),
        Property(name="listingdetailsscreen(screen)_2", type=ListingDetailsScreen(Screen), multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
DescriptionField(InputField)_CreateListeningScreen(Screen): BinaryAssociation = BinaryAssociation(
    name="DescriptionField(InputField)_CreateListeningScreen(Screen)",
    ends={
        Property(name="descriptionfield(inputfield)", type=DescriptionField(InputField), multiplicity=Multiplicity(1, 1)),
        Property(name="createlisteningscreen(screen)_2", type=CreateListeningScreen(Screen), multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
PriceLabel(Label)_ListingDetailsScreen(Screen): BinaryAssociation = BinaryAssociation(
    name="PriceLabel(Label)_ListingDetailsScreen(Screen)",
    ends={
        Property(name="pricelabel(label)", type=PriceLabel(Label), multiplicity=Multiplicity(1, 1)),
        Property(name="listingdetailsscreen(screen)_3", type=ListingDetailsScreen(Screen), multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
PriceField(InputField)_CreateListeningScreen(Screen): BinaryAssociation = BinaryAssociation(
    name="PriceField(InputField)_CreateListeningScreen(Screen)",
    ends={
        Property(name="pricefield(inputfield)", type=PriceField(InputField), multiplicity=Multiplicity(1, 1)),
        Property(name="createlisteningscreen(screen)_3", type=CreateListeningScreen(Screen), multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
EnterAuctionButton(Button)_AuctionScreen(Screen): BinaryAssociation = BinaryAssociation(
    name="EnterAuctionButton(Button)_AuctionScreen(Screen)",
    ends={
        Property(name="auctionscreen(screen)_3", type=AuctionScreen(Screen), multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="enterauctionbutton(button)", type=EnterAuctionButton(Button), multiplicity=Multiplicity(1, 1))
    }
)
ImageUpload(InputField)_CreateListeningScreen(Screen): BinaryAssociation = BinaryAssociation(
    name="ImageUpload(InputField)_CreateListeningScreen(Screen)",
    ends={
        Property(name="imageupload(inputfield)", type=ImageUpload(InputField), multiplicity=Multiplicity(1, 1)),
        Property(name="createlisteningscreen(screen)_4", type=CreateListeningScreen(Screen), multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Module(Module)_Test123(GUIModel): BinaryAssociation = BinaryAssociation(
    name="Module(Module)_Test123(GUIModel)",
    ends={
        Property(name="module(module)_7", type=Module(Module), multiplicity=Multiplicity(1, 1)),
        Property(name="test123(guimodel)", type=Test123(GUIModel), multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
SubmitButton(Button)_CreateListeningScreen(Screen): BinaryAssociation = BinaryAssociation(
    name="SubmitButton(Button)_CreateListeningScreen(Screen)",
    ends={
        Property(name="submitbutton(button)", type=SubmitButton(Button), multiplicity=Multiplicity(1, 1)),
        Property(name="createlisteningscreen(screen)_5", type=CreateListeningScreen(Screen), multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
AuctionList(ViewContainer)_AuctionScreen(Screen): BinaryAssociation = BinaryAssociation(
    name="AuctionList(ViewContainer)_AuctionScreen(Screen)",
    ends={
        Property(name="auctionlist(viewcontainer)", type=AuctionList(ViewContainer), multiplicity=Multiplicity(1, 1)),
        Property(name="auctionscreen(screen)_1", type=AuctionScreen(Screen), multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
FilterMenu(Menu)_AuctionScreen(Screen): BinaryAssociation = BinaryAssociation(
    name="FilterMenu(Menu)_AuctionScreen(Screen)",
    ends={
        Property(name="filtermenu(menu)", type=FilterMenu(Menu), multiplicity=Multiplicity(1, 1)),
        Property(name="auctionscreen(screen)_2", type=AuctionScreen(Screen), multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="test123(guiModel)",
    types={Test123(GUIModel), Module(Module), ChatScreen(Screen), LoginScreen(Screen), HomeScreen(Screen), ListingDetailsScreen(Screen), CreateListeningScreen(Screen), AuctionScreen(Screen), ProfileScreen(Screen), InputField(InputField), SendButton(Button), MessageList(ViewContainer), UsernameField(InputField), PasswordField(InputField), LoginButton(Button), MainMenu(Menu), ProfileButton(Button), HomeLogoutButton(Button), ProfileMenu(Menu), EditProfileButton(Button), ProfileLogoutButton(Button), ImageGallery(Image), TitleLabel(Label), PriceLabel(Label), BidInput(InputField), BidButton(Button), BuyNowButton(Button), TitleField(InputField), DescriptionField(InputField), PriceField(InputField), ImageUpload(InputField), SubmitButton(Button), AuctionList(ViewContainer), FilterMenu(Menu), EnterAuctionButton(Button)},
    associations={ListingDetailsScreen(Screen)_Module(Module), ProfileScreen(Screen)_Module(Module), LoginScreen(Screen)_Module(Module), ChatScreen(Screen)_Module(Module), UsernameField(InputField)_LoginScreen(Screen), CreateListeningScreen(Screen)_Module(Module), PasswordField(InputField)_LoginScreen(Screen), AuctionScreen(Screen)_Module(Module), LoginButton(Button)_LoginScreen(Screen), HomeScreen(Screen)_Module(Module), MainMenu(Menu)_HomeScreen(Screen), SendButton(Button)_ChatScreen(Screen), ProfileButton(Button)_HomeScreen(Screen), InputField(InputField)_ChatScreen(Screen), HomeLogoutButton(Button)_HomeScreen(Screen), MessageList(ViewContainer)_ChatScreen(Screen), ProfileMenu(Menu)_ProfileScreen(Screen), BidInput(InputField)_ListingDetailsScreen(Screen), EditProfileButton(Button)_ProfileScreen(Screen), BidButton(Button)_ListingDetailsScreen(Screen), ProfileLogoutButton(Button)_ProfileScreen(Screen), BuyNowButton(Button)_ListingDetailsScreen(Screen), ImageGallery(Image)_ListingDetailsScreen(Screen), TitleField(InputField)_CreateListeningScreen(Screen), TitleLabel(Label)_ListingDetailsScreen(Screen), DescriptionField(InputField)_CreateListeningScreen(Screen), PriceLabel(Label)_ListingDetailsScreen(Screen), PriceField(InputField)_CreateListeningScreen(Screen), EnterAuctionButton(Button)_AuctionScreen(Screen), ImageUpload(InputField)_CreateListeningScreen(Screen), Module(Module)_Test123(GUIModel), SubmitButton(Button)_CreateListeningScreen(Screen), AuctionList(ViewContainer)_AuctionScreen(Screen), FilterMenu(Menu)_AuctionScreen(Screen)},
    generalizations={},
    metadata=None
)


######################
# PROJECT DEFINITION #
######################

from besser.BUML.metamodel.project import Project
from besser.BUML.metamodel.structural.structural import Metadata

metadata = Metadata(description="New project")
project = Project(
    name="TACS",
    models=[domain_model],
    owner="Eduardo Areias",
    metadata=metadata
)
