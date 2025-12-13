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
Test123 = Class(name="Test123")
Module = Class(name="Module")
ChatScreen = Class(name="ChatScreen")
LoginScreen = Class(name="LoginScreen")
HomeScreen = Class(name="HomeScreen")
ListingDetailsScreen = Class(name="ListingDetailsScreen")
CreateListingScreen = Class(name="CreateListingScreen")
AuctionScreen = Class(name="AuctionScreen")
NewMessageField = Class(name="NewMessageField")
SendButton = Class(name="SendButton")
MessageList = Class(name="MessageList")
UsernameField = Class(name="UsernameField")
PasswordField = Class(name="PasswordField")
MenuButton = Class(name="MenuButton")
ProfileButton = Class(name="ProfileButton")
LoginButton = Class(name="LoginButton")
EditProfileButton = Class(name="EditProfileButton")
ImageGallery = Class(name="ImageGallery")
TitleLabel = Class(name="TitleLabel")
PriceLabel = Class(name="PriceLabel")
BidInput = Class(name="BidInput")
BidButton = Class(name="BidButton")
BuyNowButton = Class(name="BuyNowButton")
TitleField = Class(name="TitleField")
ImagesUploaded = Class(name="ImagesUploaded")
DescriptionField = Class(name="DescriptionField")
AuctionBox = Class(name="AuctionBox")
PriceField = Class(name="PriceField")
ExchangeScreen = Class(name="ExchangeScreen")
ImageUpload = Class(name="ImageUpload")
ExchangeList = Class(name="ExchangeList")
SubmitButton = Class(name="SubmitButton")
FilterExchangesButton = Class(name="FilterExchangesButton")
AuctionList = Class(name="AuctionList")
FilterAuctionsButton = Class(name="FilterAuctionsButton")
EnterExchangeButton = Class(name="EnterExchangeButton")
EnterAuctionButton = Class(name="EnterAuctionButton")
ExchangeBox = Class(name="ExchangeBox")
MessageBox = Class(name="MessageBox")
LocationField = Class(name="LocationField")
CommonScreen = Class(name="CommonScreen")
LogoutButton = Class(name="LogoutButton", metadata=Metadata(description="Can be invisible"))
ProfileContentsBox = Class(name="ProfileContentsBox")
AppPresentationBox = Class(name="AppPresentationBox")
FooterBox = Class(name="FooterBox")
ProfileScreen = Class(name="ProfileScreen")
MainImage = Class(name="MainImage")

# Test123 class attributes and methods

# Module class attributes and methods

# ChatScreen class attributes and methods

# LoginScreen class attributes and methods

# HomeScreen class attributes and methods

# ListingDetailsScreen class attributes and methods

# CreateListingScreen class attributes and methods

# AuctionScreen class attributes and methods

# NewMessageField class attributes and methods

# SendButton class attributes and methods

# MessageList class attributes and methods

# UsernameField class attributes and methods

# PasswordField class attributes and methods

# MenuButton class attributes and methods

# ProfileButton class attributes and methods

# LoginButton class attributes and methods

# EditProfileButton class attributes and methods

# ImageGallery class attributes and methods

# TitleLabel class attributes and methods

# PriceLabel class attributes and methods

# BidInput class attributes and methods

# BidButton class attributes and methods

# BuyNowButton class attributes and methods

# TitleField class attributes and methods

# ImagesUploaded class attributes and methods

# DescriptionField class attributes and methods

# AuctionBox class attributes and methods

# PriceField class attributes and methods

# ExchangeScreen class attributes and methods

# ImageUpload class attributes and methods

# ExchangeList class attributes and methods

# SubmitButton class attributes and methods

# FilterExchangesButton class attributes and methods

# AuctionList class attributes and methods

# FilterAuctionsButton class attributes and methods

# EnterExchangeButton class attributes and methods

# EnterAuctionButton class attributes and methods

# ExchangeBox class attributes and methods

# MessageBox class attributes and methods

# LocationField class attributes and methods

# CommonScreen class attributes and methods

# LogoutButton class attributes and methods

# ProfileContentsBox class attributes and methods

# AppPresentationBox class attributes and methods

# FooterBox class attributes and methods

# ProfileScreen class attributes and methods

# MainImage class attributes and methods

# Relationships
PasswordField_LoginScreen: BinaryAssociation = BinaryAssociation(
    name="PasswordField_LoginScreen",
    ends={
        Property(name="passwordfield", type=PasswordField, multiplicity=Multiplicity(1, 1)),
        Property(name="loginscreen_1", type=LoginScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ImageGallery_ListingDetailsScreen: BinaryAssociation = BinaryAssociation(
    name="ImageGallery_ListingDetailsScreen",
    ends={
        Property(name="imagegallery", type=ImageGallery, multiplicity=Multiplicity(1, 1)),
        Property(name="listingdetailsscreen", type=ListingDetailsScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
TitleLabel_ListingDetailsScreen: BinaryAssociation = BinaryAssociation(
    name="TitleLabel_ListingDetailsScreen",
    ends={
        Property(name="titlelabel", type=TitleLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="listingdetailsscreen_1", type=ListingDetailsScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
SendButton_ChatScreen: BinaryAssociation = BinaryAssociation(
    name="SendButton_ChatScreen",
    ends={
        Property(name="sendbutton", type=SendButton, multiplicity=Multiplicity(1, 1)),
        Property(name="chatscreen", type=ChatScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
PriceLabel_ListingDetailsScreen: BinaryAssociation = BinaryAssociation(
    name="PriceLabel_ListingDetailsScreen",
    ends={
        Property(name="pricelabel", type=PriceLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="listingdetailsscreen_2", type=ListingDetailsScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
NewMessageField_ChatScreen: BinaryAssociation = BinaryAssociation(
    name="NewMessageField_ChatScreen",
    ends={
        Property(name="newmessagefield", type=NewMessageField, multiplicity=Multiplicity(1, 1)),
        Property(name="chatscreen_1", type=ChatScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
BidInput_ListingDetailsScreen: BinaryAssociation = BinaryAssociation(
    name="BidInput_ListingDetailsScreen",
    ends={
        Property(name="bidinput", type=BidInput, multiplicity=Multiplicity(1, 1)),
        Property(name="listingdetailsscreen_3", type=ListingDetailsScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
MessageList_ChatScreen: BinaryAssociation = BinaryAssociation(
    name="MessageList_ChatScreen",
    ends={
        Property(name="messagelist", type=MessageList, multiplicity=Multiplicity(1, 1)),
        Property(name="chatscreen_2", type=ChatScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
BidButton_ListingDetailsScreen: BinaryAssociation = BinaryAssociation(
    name="BidButton_ListingDetailsScreen",
    ends={
        Property(name="bidbutton", type=BidButton, multiplicity=Multiplicity(1, 1)),
        Property(name="listingdetailsscreen_4", type=ListingDetailsScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
UsernameField_LoginScreen: BinaryAssociation = BinaryAssociation(
    name="UsernameField_LoginScreen",
    ends={
        Property(name="usernamefield", type=UsernameField, multiplicity=Multiplicity(1, 1)),
        Property(name="loginscreen", type=LoginScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
BuyNowButton_ListingDetailsScreen: BinaryAssociation = BinaryAssociation(
    name="BuyNowButton_ListingDetailsScreen",
    ends={
        Property(name="buynowbutton", type=BuyNowButton, multiplicity=Multiplicity(1, 1)),
        Property(name="listingdetailsscreen_5", type=ListingDetailsScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
SubmitButton_CreateListingScreen: BinaryAssociation = BinaryAssociation(
    name="SubmitButton_CreateListingScreen",
    ends={
        Property(name="createlistingscreen_4", type=CreateListingScreen, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="submitbutton", type=SubmitButton, multiplicity=Multiplicity(1, 1))
    }
)
TitleField_CreateListingScreen: BinaryAssociation = BinaryAssociation(
    name="TitleField_CreateListingScreen",
    ends={
        Property(name="titlefield", type=TitleField, multiplicity=Multiplicity(1, 1)),
        Property(name="createlistingscreen", type=CreateListingScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
AuctionList_AuctionScreen: BinaryAssociation = BinaryAssociation(
    name="AuctionList_AuctionScreen",
    ends={
        Property(name="auctionlist", type=AuctionList, multiplicity=Multiplicity(1, 1)),
        Property(name="auctionscreen", type=AuctionScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
DescriptionField_CreateListingScreen: BinaryAssociation = BinaryAssociation(
    name="DescriptionField_CreateListingScreen",
    ends={
        Property(name="descriptionfield", type=DescriptionField, multiplicity=Multiplicity(1, 1)),
        Property(name="createlistingscreen_1", type=CreateListingScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
FilterAuctionsButton_AuctionScreen: BinaryAssociation = BinaryAssociation(
    name="FilterAuctionsButton_AuctionScreen",
    ends={
        Property(name="filterauctionsbutton", type=FilterAuctionsButton, multiplicity=Multiplicity(1, 1)),
        Property(name="auctionscreen_1", type=AuctionScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
PriceField_CreateListingScreen: BinaryAssociation = BinaryAssociation(
    name="PriceField_CreateListingScreen",
    ends={
        Property(name="pricefield", type=PriceField, multiplicity=Multiplicity(1, 1)),
        Property(name="createlistingscreen_2", type=CreateListingScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
EnterAuctionButton_AuctionScreen: BinaryAssociation = BinaryAssociation(
    name="EnterAuctionButton_AuctionScreen",
    ends={
        Property(name="enterauctionbutton", type=EnterAuctionButton, multiplicity=Multiplicity(1, 1)),
        Property(name="auctionscreen_2", type=AuctionScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Module_Test123: BinaryAssociation = BinaryAssociation(
    name="Module_Test123",
    ends={
        Property(name="module", type=Module, multiplicity=Multiplicity(1, 1)),
        Property(name="test123", type=Test123, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ImageUpload_CreateListingScreen: BinaryAssociation = BinaryAssociation(
    name="ImageUpload_CreateListingScreen",
    ends={
        Property(name="imageupload", type=ImageUpload, multiplicity=Multiplicity(1, 1)),
        Property(name="createlistingscreen_3", type=CreateListingScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
MessageBox_MessageList: BinaryAssociation = BinaryAssociation(
    name="MessageBox_MessageList",
    ends={
        Property(name="messagebox", type=MessageBox, multiplicity=Multiplicity(0, 9999)),
        Property(name="messagelist_1", type=MessageList, multiplicity=Multiplicity(1, 1))
    }
)
AppPresentationBox_HomeScreen: BinaryAssociation = BinaryAssociation(
    name="AppPresentationBox_HomeScreen",
    ends={
        Property(name="apppresentationbox", type=AppPresentationBox, multiplicity=Multiplicity(1, 1)),
        Property(name="homescreen", type=HomeScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
FooterBox_HomeScreen: BinaryAssociation = BinaryAssociation(
    name="FooterBox_HomeScreen",
    ends={
        Property(name="footerbox", type=FooterBox, multiplicity=Multiplicity(1, 1)),
        Property(name="homescreen_1", type=HomeScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
LoginButton_LoginScreen: BinaryAssociation = BinaryAssociation(
    name="LoginButton_LoginScreen",
    ends={
        Property(name="loginbutton", type=LoginButton, multiplicity=Multiplicity(1, 1)),
        Property(name="loginscreen_2", type=LoginScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
LoginScreen_Module: BinaryAssociation = BinaryAssociation(
    name="LoginScreen_Module",
    ends={
        Property(name="loginscreen_3", type=LoginScreen, multiplicity=Multiplicity(1, 1)),
        Property(name="module_1", type=Module, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ProfileButton_CommonScreen: BinaryAssociation = BinaryAssociation(
    name="ProfileButton_CommonScreen",
    ends={
        Property(name="profilebutton", type=ProfileButton, multiplicity=Multiplicity(1, 1)),
        Property(name="commonscreen", type=CommonScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ChatScreen_Module: BinaryAssociation = BinaryAssociation(
    name="ChatScreen_Module",
    ends={
        Property(name="chatscreen_3", type=ChatScreen, multiplicity=Multiplicity(1, 1)),
        Property(name="module_2", type=Module, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
MenuButton_CommonScreen: BinaryAssociation = BinaryAssociation(
    name="MenuButton_CommonScreen",
    ends={
        Property(name="menubutton", type=MenuButton, multiplicity=Multiplicity(1, 1)),
        Property(name="commonscreen_1", type=CommonScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
HomeScreen_Module: BinaryAssociation = BinaryAssociation(
    name="HomeScreen_Module",
    ends={
        Property(name="homescreen_2", type=HomeScreen, multiplicity=Multiplicity(1, 1)),
        Property(name="module_3", type=Module, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ProfileScreen_Module: BinaryAssociation = BinaryAssociation(
    name="ProfileScreen_Module",
    ends={
        Property(name="profilescreen_2", type=ProfileScreen, multiplicity=Multiplicity(1, 1)),
        Property(name="module_4", type=Module, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
LogoutButton_CommonScreen: BinaryAssociation = BinaryAssociation(
    name="LogoutButton_CommonScreen",
    ends={
        Property(name="logoutbutton", type=LogoutButton, multiplicity=Multiplicity(1, 1)),
        Property(name="commonscreen_2", type=CommonScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
MainImage_ListingDetailsScreen: BinaryAssociation = BinaryAssociation(
    name="MainImage_ListingDetailsScreen",
    ends={
        Property(name="mainimage", type=MainImage, multiplicity=Multiplicity(1, 1)),
        Property(name="listingdetailsscreen_6", type=ListingDetailsScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ImagesUploaded_CreateListingScreen: BinaryAssociation = BinaryAssociation(
    name="ImagesUploaded_CreateListingScreen",
    ends={
        Property(name="imagesuploaded", type=ImagesUploaded, multiplicity=Multiplicity(1, 1)),
        Property(name="createlistingscreen_5", type=CreateListingScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ProfileContentsBox_ProfileScreen: BinaryAssociation = BinaryAssociation(
    name="ProfileContentsBox_ProfileScreen",
    ends={
        Property(name="profilecontentsbox", type=ProfileContentsBox, multiplicity=Multiplicity(1, 1)),
        Property(name="profilescreen", type=ProfileScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
EditProfileButton_ProfileScreen: BinaryAssociation = BinaryAssociation(
    name="EditProfileButton_ProfileScreen",
    ends={
        Property(name="editprofilebutton", type=EditProfileButton, multiplicity=Multiplicity(1, 1)),
        Property(name="profilescreen_1", type=ProfileScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
AuctionBox_AuctionList: BinaryAssociation = BinaryAssociation(
    name="AuctionBox_AuctionList",
    ends={
        Property(name="auctionbox", type=AuctionBox, multiplicity=Multiplicity(1, 1)),
        Property(name="auctionlist_1", type=AuctionList, multiplicity=Multiplicity(0, 9999))
    }
)
ExchangeBox_ExchangeList: BinaryAssociation = BinaryAssociation(
    name="ExchangeBox_ExchangeList",
    ends={
        Property(name="exchangelist_1", type=ExchangeList, multiplicity=Multiplicity(0, 9999)),
        Property(name="exchangebox", type=ExchangeBox, multiplicity=Multiplicity(1, 1))
    }
)
ExchangeList_ExchangeScreen: BinaryAssociation = BinaryAssociation(
    name="ExchangeList_ExchangeScreen",
    ends={
        Property(name="exchangelist", type=ExchangeList, multiplicity=Multiplicity(1, 1)),
        Property(name="exchangescreen", type=ExchangeScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
LocationField_CreateListingScreen: BinaryAssociation = BinaryAssociation(
    name="LocationField_CreateListingScreen",
    ends={
        Property(name="locationfield", type=LocationField, multiplicity=Multiplicity(1, 1)),
        Property(name="createlistingscreen_6", type=CreateListingScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
FilterExchangesButton_ExchangeScreen: BinaryAssociation = BinaryAssociation(
    name="FilterExchangesButton_ExchangeScreen",
    ends={
        Property(name="filterexchangesbutton", type=FilterExchangesButton, multiplicity=Multiplicity(1, 1)),
        Property(name="exchangescreen_1", type=ExchangeScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ListingDetailsScreen_Module: BinaryAssociation = BinaryAssociation(
    name="ListingDetailsScreen_Module",
    ends={
        Property(name="listingdetailsscreen_7", type=ListingDetailsScreen, multiplicity=Multiplicity(1, 1)),
        Property(name="module_5", type=Module, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
EnterExchangeButton_ExchangeScreen: BinaryAssociation = BinaryAssociation(
    name="EnterExchangeButton_ExchangeScreen",
    ends={
        Property(name="enterexchangebutton", type=EnterExchangeButton, multiplicity=Multiplicity(1, 1)),
        Property(name="exchangescreen_2", type=ExchangeScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
CreateListingScreen_Module: BinaryAssociation = BinaryAssociation(
    name="CreateListingScreen_Module",
    ends={
        Property(name="createlistingscreen_7", type=CreateListingScreen, multiplicity=Multiplicity(1, 1)),
        Property(name="module_6", type=Module, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
AuctionScreen_Module: BinaryAssociation = BinaryAssociation(
    name="AuctionScreen_Module",
    ends={
        Property(name="auctionscreen_3", type=AuctionScreen, multiplicity=Multiplicity(1, 1)),
        Property(name="module_7", type=Module, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ExchangeScreen_Module: BinaryAssociation = BinaryAssociation(
    name="ExchangeScreen_Module",
    ends={
        Property(name="exchangescreen_3", type=ExchangeScreen, multiplicity=Multiplicity(1, 1)),
        Property(name="module_8", type=Module, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_CommonScreen_ChatScreen = Generalization(general=ChatScreen, specific=CommonScreen)
gen_CommonScreen_HomeScreen = Generalization(general=HomeScreen, specific=CommonScreen)
gen_CommonScreen_ListingDetailsScreen = Generalization(general=ListingDetailsScreen, specific=CommonScreen)
gen_CommonScreen_CreateListingScreen = Generalization(general=CreateListingScreen, specific=CommonScreen)
gen_CommonScreen_AuctionScreen = Generalization(general=AuctionScreen, specific=CommonScreen)
gen_CommonScreen_ProfileScreen = Generalization(general=ProfileScreen, specific=CommonScreen)
gen_CommonScreen_ExchangeScreen = Generalization(general=ExchangeScreen, specific=CommonScreen)

# Domain Model
domain_model = DomainModel(
    name="test123_(guiModel)",
    types={Test123, Module, ChatScreen, LoginScreen, HomeScreen, ListingDetailsScreen, CreateListingScreen, AuctionScreen, NewMessageField, SendButton, MessageList, UsernameField, PasswordField, MenuButton, ProfileButton, LoginButton, EditProfileButton, ImageGallery, TitleLabel, PriceLabel, BidInput, BidButton, BuyNowButton, TitleField, ImagesUploaded, DescriptionField, AuctionBox, PriceField, ExchangeScreen, ImageUpload, ExchangeList, SubmitButton, FilterExchangesButton, AuctionList, FilterAuctionsButton, EnterExchangeButton, EnterAuctionButton, ExchangeBox, MessageBox, LocationField, CommonScreen, LogoutButton, ProfileContentsBox, AppPresentationBox, FooterBox, ProfileScreen, MainImage},
    associations={PasswordField_LoginScreen, ImageGallery_ListingDetailsScreen, TitleLabel_ListingDetailsScreen, SendButton_ChatScreen, PriceLabel_ListingDetailsScreen, NewMessageField_ChatScreen, BidInput_ListingDetailsScreen, MessageList_ChatScreen, BidButton_ListingDetailsScreen, UsernameField_LoginScreen, BuyNowButton_ListingDetailsScreen, SubmitButton_CreateListingScreen, TitleField_CreateListingScreen, AuctionList_AuctionScreen, DescriptionField_CreateListingScreen, FilterAuctionsButton_AuctionScreen, PriceField_CreateListingScreen, EnterAuctionButton_AuctionScreen, Module_Test123, ImageUpload_CreateListingScreen, MessageBox_MessageList, AppPresentationBox_HomeScreen, FooterBox_HomeScreen, LoginButton_LoginScreen, LoginScreen_Module, ProfileButton_CommonScreen, ChatScreen_Module, MenuButton_CommonScreen, HomeScreen_Module, ProfileScreen_Module, LogoutButton_CommonScreen, MainImage_ListingDetailsScreen, ImagesUploaded_CreateListingScreen, ProfileContentsBox_ProfileScreen, EditProfileButton_ProfileScreen, AuctionBox_AuctionList, ExchangeBox_ExchangeList, ExchangeList_ExchangeScreen, LocationField_CreateListingScreen, FilterExchangesButton_ExchangeScreen, ListingDetailsScreen_Module, EnterExchangeButton_ExchangeScreen, CreateListingScreen_Module, AuctionScreen_Module, ExchangeScreen_Module},
    generalizations={gen_CommonScreen_ChatScreen, gen_CommonScreen_HomeScreen, gen_CommonScreen_ListingDetailsScreen, gen_CommonScreen_CreateListingScreen, gen_CommonScreen_AuctionScreen, gen_CommonScreen_ProfileScreen, gen_CommonScreen_ExchangeScreen},
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
