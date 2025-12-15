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
Frontend = Class(name="Frontend")
CommonScreen = Class(name="CommonScreen")
ChatScreen = Class(name="ChatScreen")
LoginScreen = Class(name="LoginScreen")
HomeScreen = Class(name="HomeScreen")
NewMessageField = Class(name="NewMessageField")
SendButton = Class(name="SendButton")
MessageListComponent = Class(name="MessageListComponent")
UsernameField = Class(name="UsernameField")
PasswordField = Class(name="PasswordField")
LoginButton = Class(name="LoginButton")
EditProfileButton = Class(name="EditProfileButton")
MessageCardComponent = Class(name="MessageCardComponent")
TransactionHistoryScreen = Class(name="TransactionHistoryScreen")
ProfileContentsComponent = Class(name="ProfileContentsComponent")
TransactionListComponent = Class(name="TransactionListComponent")
AppPresentationComponent = Class(name="AppPresentationComponent")
TransactionCardComponent = Class(name="TransactionCardComponent")
FooterComponent = Class(name="FooterComponent")
ListingsScreen = Class(name="ListingsScreen")
ProfileScreen = Class(name="ProfileScreen")
ListingsListComponent = Class(name="ListingsListComponent")
NotFoundScreen = Class(name="NotFoundScreen")
ReviewScreen = Class(name="ReviewScreen")
EnterListingComponent = Class(name="EnterListingComponent")
NewReviewFormComponent = Class(name="NewReviewFormComponent")
ListingsFilterButton = Class(name="ListingsFilterButton")
ReviewCardComponent = Class(name="ReviewCardComponent")
SaleCardComponent = Class(name="SaleCardComponent")
ReviewListComponent = Class(name="ReviewListComponent")
AuctionCardComponent = Class(name="AuctionCardComponent")
ExchangeCardComponent = Class(name="ExchangeCardComponent")
ListingDetailsScreen = Class(name="ListingDetailsScreen")
ReportScreen = Class(name="ReportScreen")
SaleDetailsComponent = Class(name="SaleDetailsComponent")
ExchangeDetailsComponent = Class(name="ExchangeDetailsComponent")
NewReportFormComponent = Class(name="NewReportFormComponent")
ReportCardComponent = Class(name="ReportCardComponent")
AuctionDetailsComponent = Class(name="AuctionDetailsComponent")
ReportManagementComponent = Class(name="ReportManagementComponent")
CreateListingScreen = Class(name="CreateListingScreen")
ProductTitleField = Class(name="ProductTitleField")
LocationField = Class(name="LocationField")
ProductDescriptionField = Class(name="ProductDescriptionField")
MultipleImagesUploadComponent = Class(name="MultipleImagesUploadComponent")
SingleImageUploadComponent = Class(name="SingleImageUploadComponent")
SubmitListingButton = Class(name="SubmitListingButton")
ListingTypeSelector = Class(name="ListingTypeSelector")
CheckboxesComponent = Class(name="CheckboxesComponent")
AuctionClosingTimeField = Class(name="AuctionClosingTimeField")
PriceField = Class(name="PriceField")
ProfileButton = Class(name="ProfileButton")
PreferedExchangeTypeField = Class(name="PreferedExchangeTypeField")
LogoutButton = Class(name="LogoutButton", metadata=Metadata(description="Can be invisible"))
ImageGalleryComponent = Class(name="ImageGalleryComponent")
TopBarComponent = Class(name="TopBarComponent")
ProductTitleLabel = Class(name="ProductTitleLabel")
ViewAuctionsButton = Class(name="ViewAuctionsButton")
PriceLabel = Class(name="PriceLabel")
ViewSalesButton = Class(name="ViewSalesButton")
BidField = Class(name="BidField")
BidNowButton = Class(name="BidNowButton")
ViewExchangesButton = Class(name="ViewExchangesButton")
BuyNowButton = Class(name="BuyNowButton")
SaleCheckbox = Class(name="SaleCheckbox")
MainImageComponent = Class(name="MainImageComponent")
AuctionCheckbox = Class(name="AuctionCheckbox")
ExchangeNowButton = Class(name="ExchangeNowButton")
ExchangeCheckbox = Class(name="ExchangeCheckbox")
ProductDescriptionLabel = Class(name="ProductDescriptionLabel")
ProposedExchangeField = Class(name="ProposedExchangeField")
MenuButton = Class(name="MenuButton")

# Frontend class attributes and methods

# CommonScreen class attributes and methods

# ChatScreen class attributes and methods

# LoginScreen class attributes and methods

# HomeScreen class attributes and methods

# NewMessageField class attributes and methods

# SendButton class attributes and methods

# MessageListComponent class attributes and methods

# UsernameField class attributes and methods

# PasswordField class attributes and methods

# LoginButton class attributes and methods

# EditProfileButton class attributes and methods

# MessageCardComponent class attributes and methods

# TransactionHistoryScreen class attributes and methods

# ProfileContentsComponent class attributes and methods

# TransactionListComponent class attributes and methods

# AppPresentationComponent class attributes and methods

# TransactionCardComponent class attributes and methods

# FooterComponent class attributes and methods

# ListingsScreen class attributes and methods

# ProfileScreen class attributes and methods

# ListingsListComponent class attributes and methods

# NotFoundScreen class attributes and methods

# ReviewScreen class attributes and methods

# EnterListingComponent class attributes and methods

# NewReviewFormComponent class attributes and methods

# ListingsFilterButton class attributes and methods

# ReviewCardComponent class attributes and methods

# SaleCardComponent class attributes and methods

# ReviewListComponent class attributes and methods

# AuctionCardComponent class attributes and methods

# ExchangeCardComponent class attributes and methods

# ListingDetailsScreen class attributes and methods

# ReportScreen class attributes and methods

# SaleDetailsComponent class attributes and methods

# ExchangeDetailsComponent class attributes and methods

# NewReportFormComponent class attributes and methods

# ReportCardComponent class attributes and methods

# AuctionDetailsComponent class attributes and methods

# ReportManagementComponent class attributes and methods

# CreateListingScreen class attributes and methods

# ProductTitleField class attributes and methods

# LocationField class attributes and methods

# ProductDescriptionField class attributes and methods

# MultipleImagesUploadComponent class attributes and methods

# SingleImageUploadComponent class attributes and methods

# SubmitListingButton class attributes and methods

# ListingTypeSelector class attributes and methods

# CheckboxesComponent class attributes and methods

# AuctionClosingTimeField class attributes and methods

# PriceField class attributes and methods

# ProfileButton class attributes and methods

# PreferedExchangeTypeField class attributes and methods

# LogoutButton class attributes and methods

# ImageGalleryComponent class attributes and methods

# TopBarComponent class attributes and methods

# ProductTitleLabel class attributes and methods

# ViewAuctionsButton class attributes and methods

# PriceLabel class attributes and methods

# ViewSalesButton class attributes and methods

# BidField class attributes and methods

# BidNowButton class attributes and methods

# ViewExchangesButton class attributes and methods

# BuyNowButton class attributes and methods

# SaleCheckbox class attributes and methods

# MainImageComponent class attributes and methods

# AuctionCheckbox class attributes and methods

# ExchangeNowButton class attributes and methods

# ExchangeCheckbox class attributes and methods

# ProductDescriptionLabel class attributes and methods

# ProposedExchangeField class attributes and methods

# MenuButton class attributes and methods

# Relationships
SendButton_ChatScreen: BinaryAssociation = BinaryAssociation(
    name="SendButton_ChatScreen",
    ends={
        Property(name="sendbutton", type=SendButton, multiplicity=Multiplicity(1, 1)),
        Property(name="chatscreen", type=ChatScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
NewMessageField_ChatScreen: BinaryAssociation = BinaryAssociation(
    name="NewMessageField_ChatScreen",
    ends={
        Property(name="newmessagefield", type=NewMessageField, multiplicity=Multiplicity(1, 1)),
        Property(name="chatscreen_1", type=ChatScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
MessageListComponent_ChatScreen: BinaryAssociation = BinaryAssociation(
    name="MessageListComponent_ChatScreen",
    ends={
        Property(name="messagelistcomponent", type=MessageListComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="chatscreen_2", type=ChatScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
UsernameField_LoginScreen: BinaryAssociation = BinaryAssociation(
    name="UsernameField_LoginScreen",
    ends={
        Property(name="usernamefield", type=UsernameField, multiplicity=Multiplicity(1, 1)),
        Property(name="loginscreen", type=LoginScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
HomeScreen_CommonScreen: BinaryAssociation = BinaryAssociation(
    name="HomeScreen_CommonScreen",
    ends={
        Property(name="homescreen_1", type=HomeScreen, multiplicity=Multiplicity(1, 1)),
        Property(name="commonscreen_3", type=CommonScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
PasswordField_LoginScreen: BinaryAssociation = BinaryAssociation(
    name="PasswordField_LoginScreen",
    ends={
        Property(name="passwordfield", type=PasswordField, multiplicity=Multiplicity(1, 1)),
        Property(name="loginscreen_1", type=LoginScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
CommonScreen_Frontend: BinaryAssociation = BinaryAssociation(
    name="CommonScreen_Frontend",
    ends={
        Property(name="commonscreen", type=CommonScreen, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend", type=Frontend, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ProfileContentsComponent_ProfileScreen: BinaryAssociation = BinaryAssociation(
    name="ProfileContentsComponent_ProfileScreen",
    ends={
        Property(name="profilecontentscomponent", type=ProfileContentsComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="profilescreen", type=ProfileScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
LoginButton_LoginScreen: BinaryAssociation = BinaryAssociation(
    name="LoginButton_LoginScreen",
    ends={
        Property(name="loginbutton", type=LoginButton, multiplicity=Multiplicity(1, 1)),
        Property(name="loginscreen_2", type=LoginScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
EditProfileButton_ProfileScreen: BinaryAssociation = BinaryAssociation(
    name="EditProfileButton_ProfileScreen",
    ends={
        Property(name="editprofilebutton", type=EditProfileButton, multiplicity=Multiplicity(1, 1)),
        Property(name="profilescreen_1", type=ProfileScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
AppPresentationComponent_HomeScreen: BinaryAssociation = BinaryAssociation(
    name="AppPresentationComponent_HomeScreen",
    ends={
        Property(name="apppresentationcomponent", type=AppPresentationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="homescreen", type=HomeScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ProfileScreen_CommonScreen: BinaryAssociation = BinaryAssociation(
    name="ProfileScreen_CommonScreen",
    ends={
        Property(name="profilescreen_2", type=ProfileScreen, multiplicity=Multiplicity(1, 1)),
        Property(name="commonscreen_4", type=CommonScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
LoginScreen_CommonScreen: BinaryAssociation = BinaryAssociation(
    name="LoginScreen_CommonScreen",
    ends={
        Property(name="loginscreen_3", type=LoginScreen, multiplicity=Multiplicity(1, 1)),
        Property(name="commonscreen_1", type=CommonScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
NotFoundScreen_CommonScreen: BinaryAssociation = BinaryAssociation(
    name="NotFoundScreen_CommonScreen",
    ends={
        Property(name="notfoundscreen", type=NotFoundScreen, multiplicity=Multiplicity(1, 1)),
        Property(name="commonscreen_5", type=CommonScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ChatScreen_CommonScreen: BinaryAssociation = BinaryAssociation(
    name="ChatScreen_CommonScreen",
    ends={
        Property(name="chatscreen_3", type=ChatScreen, multiplicity=Multiplicity(1, 1)),
        Property(name="commonscreen_2", type=CommonScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
NewReviewFormComponent_ReviewScreen: BinaryAssociation = BinaryAssociation(
    name="NewReviewFormComponent_ReviewScreen",
    ends={
        Property(name="newreviewformcomponent", type=NewReviewFormComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="reviewscreen", type=ReviewScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ReviewScreen_CommonScreen: BinaryAssociation = BinaryAssociation(
    name="ReviewScreen_CommonScreen",
    ends={
        Property(name="reviewscreen_3", type=ReviewScreen, multiplicity=Multiplicity(1, 1)),
        Property(name="commonscreen_6", type=CommonScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ReviewCardComponent_ReviewScreen: BinaryAssociation = BinaryAssociation(
    name="ReviewCardComponent_ReviewScreen",
    ends={
        Property(name="reviewcardcomponent", type=ReviewCardComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="reviewscreen_1", type=ReviewScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ReportScreen_CommonScreen: BinaryAssociation = BinaryAssociation(
    name="ReportScreen_CommonScreen",
    ends={
        Property(name="reportscreen_3", type=ReportScreen, multiplicity=Multiplicity(1, 1)),
        Property(name="commonscreen_7", type=CommonScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ReviewListComponent_ReviewScreen: BinaryAssociation = BinaryAssociation(
    name="ReviewListComponent_ReviewScreen",
    ends={
        Property(name="reviewlistcomponent", type=ReviewListComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="reviewscreen_2", type=ReviewScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
NewReportFormComponent_ReportScreen: BinaryAssociation = BinaryAssociation(
    name="NewReportFormComponent_ReportScreen",
    ends={
        Property(name="newreportformcomponent", type=NewReportFormComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="reportscreen", type=ReportScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
TransactionListComponent_TransactionHistoryScreen: BinaryAssociation = BinaryAssociation(
    name="TransactionListComponent_TransactionHistoryScreen",
    ends={
        Property(name="transactionlistcomponent", type=TransactionListComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="transactionhistoryscreen", type=TransactionHistoryScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ReportCardComponent_ReportScreen: BinaryAssociation = BinaryAssociation(
    name="ReportCardComponent_ReportScreen",
    ends={
        Property(name="reportcardcomponent", type=ReportCardComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="reportscreen_1", type=ReportScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
TransactionCardComponent_TransactionHistoryScreen: BinaryAssociation = BinaryAssociation(
    name="TransactionCardComponent_TransactionHistoryScreen",
    ends={
        Property(name="transactioncardcomponent", type=TransactionCardComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="transactionhistoryscreen_1", type=TransactionHistoryScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ReportManagementComponent_ReportScreen: BinaryAssociation = BinaryAssociation(
    name="ReportManagementComponent_ReportScreen",
    ends={
        Property(name="reportmanagementcomponent", type=ReportManagementComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="reportscreen_2", type=ReportScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
TransactionHistoryScreen_CommonScreen: BinaryAssociation = BinaryAssociation(
    name="TransactionHistoryScreen_CommonScreen",
    ends={
        Property(name="transactionhistoryscreen_2", type=TransactionHistoryScreen, multiplicity=Multiplicity(1, 1)),
        Property(name="commonscreen_8", type=CommonScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ExchangeCardComponent_ListingsListComponent: BinaryAssociation = BinaryAssociation(
    name="ExchangeCardComponent_ListingsListComponent",
    ends={
        Property(name="exchangecardcomponent", type=ExchangeCardComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="listingslistcomponent_2", type=ListingsListComponent, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ListingsListComponent_ListingsScreen: BinaryAssociation = BinaryAssociation(
    name="ListingsListComponent_ListingsScreen",
    ends={
        Property(name="listingslistcomponent", type=ListingsListComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="listingsscreen", type=ListingsScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
AuctionCardComponent_ListingsListComponent: BinaryAssociation = BinaryAssociation(
    name="AuctionCardComponent_ListingsListComponent",
    ends={
        Property(name="auctioncardcomponent", type=AuctionCardComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="listingslistcomponent_3", type=ListingsListComponent, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
EnterListingComponent_ListingsScreen: BinaryAssociation = BinaryAssociation(
    name="EnterListingComponent_ListingsScreen",
    ends={
        Property(name="enterlistingcomponent", type=EnterListingComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="listingsscreen_1", type=ListingsScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
SaleDetailsComponent_ListingDetailsScreen: BinaryAssociation = BinaryAssociation(
    name="SaleDetailsComponent_ListingDetailsScreen",
    ends={
        Property(name="saledetailscomponent", type=SaleDetailsComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="listingdetailsscreen", type=ListingDetailsScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ListingsFilterButton_ListingsScreen: BinaryAssociation = BinaryAssociation(
    name="ListingsFilterButton_ListingsScreen",
    ends={
        Property(name="listingsfilterbutton", type=ListingsFilterButton, multiplicity=Multiplicity(1, 1)),
        Property(name="listingsscreen_2", type=ListingsScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ListingsScreen_CommonScreen: BinaryAssociation = BinaryAssociation(
    name="ListingsScreen_CommonScreen",
    ends={
        Property(name="listingsscreen_3", type=ListingsScreen, multiplicity=Multiplicity(1, 1)),
        Property(name="commonscreen_9", type=CommonScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ExchangeDetailsComponent_ListingDetailsScreen: BinaryAssociation = BinaryAssociation(
    name="ExchangeDetailsComponent_ListingDetailsScreen",
    ends={
        Property(name="exchangedetailscomponent", type=ExchangeDetailsComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="listingdetailsscreen_1", type=ListingDetailsScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
AuctionDetailsComponent_ListingDetailsScreen: BinaryAssociation = BinaryAssociation(
    name="AuctionDetailsComponent_ListingDetailsScreen",
    ends={
        Property(name="auctiondetailscomponent", type=AuctionDetailsComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="listingdetailsscreen_2", type=ListingDetailsScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
SaleCardComponent_ListingsListComponent: BinaryAssociation = BinaryAssociation(
    name="SaleCardComponent_ListingsListComponent",
    ends={
        Property(name="salecardcomponent", type=SaleCardComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="listingslistcomponent_1", type=ListingsListComponent, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
CreateListingScreen_CommonScreen: BinaryAssociation = BinaryAssociation(
    name="CreateListingScreen_CommonScreen",
    ends={
        Property(name="createlistingscreen_3", type=CreateListingScreen, multiplicity=Multiplicity(1, 1)),
        Property(name="commonscreen_11", type=CommonScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ListingDetailsScreen_CommonScreen: BinaryAssociation = BinaryAssociation(
    name="ListingDetailsScreen_CommonScreen",
    ends={
        Property(name="listingdetailsscreen_3", type=ListingDetailsScreen, multiplicity=Multiplicity(1, 1)),
        Property(name="commonscreen_10", type=CommonScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
MultipleImagesUploadComponent_CreateListingScreen: BinaryAssociation = BinaryAssociation(
    name="MultipleImagesUploadComponent_CreateListingScreen",
    ends={
        Property(name="multipleimagesuploadcomponent", type=MultipleImagesUploadComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="createlistingscreen_4", type=CreateListingScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ProductTitleField_CreateListingScreen: BinaryAssociation = BinaryAssociation(
    name="ProductTitleField_CreateListingScreen",
    ends={
        Property(name="producttitlefield", type=ProductTitleField, multiplicity=Multiplicity(1, 1)),
        Property(name="createlistingscreen", type=CreateListingScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
LocationField_CreateListingScreen: BinaryAssociation = BinaryAssociation(
    name="LocationField_CreateListingScreen",
    ends={
        Property(name="locationfield", type=LocationField, multiplicity=Multiplicity(1, 1)),
        Property(name="createlistingscreen_1", type=CreateListingScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
SingleImageUploadComponent_CreateListingScreen: BinaryAssociation = BinaryAssociation(
    name="SingleImageUploadComponent_CreateListingScreen",
    ends={
        Property(name="singleimageuploadcomponent", type=SingleImageUploadComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="createlistingscreen_5", type=CreateListingScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ProductDescriptionField_CreateListingScreen: BinaryAssociation = BinaryAssociation(
    name="ProductDescriptionField_CreateListingScreen",
    ends={
        Property(name="productdescriptionfield", type=ProductDescriptionField, multiplicity=Multiplicity(1, 1)),
        Property(name="createlistingscreen_2", type=CreateListingScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
SubmitListingButton_CreateListingScreen: BinaryAssociation = BinaryAssociation(
    name="SubmitListingButton_CreateListingScreen",
    ends={
        Property(name="submitlistingbutton", type=SubmitListingButton, multiplicity=Multiplicity(1, 1)),
        Property(name="createlistingscreen_6", type=CreateListingScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
AuctionClosingTimeField_ListingTypeSelector: BinaryAssociation = BinaryAssociation(
    name="AuctionClosingTimeField_ListingTypeSelector",
    ends={
        Property(name="auctionclosingtimefield", type=AuctionClosingTimeField, multiplicity=Multiplicity(1, 1)),
        Property(name="listingtypeselector_3", type=ListingTypeSelector, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ListingTypeSelector_CreateListingScreen: BinaryAssociation = BinaryAssociation(
    name="ListingTypeSelector_CreateListingScreen",
    ends={
        Property(name="listingtypeselector", type=ListingTypeSelector, multiplicity=Multiplicity(1, 1)),
        Property(name="createlistingscreen_7", type=CreateListingScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
PreferedExchangeTypeField_ListingTypeSelector: BinaryAssociation = BinaryAssociation(
    name="PreferedExchangeTypeField_ListingTypeSelector",
    ends={
        Property(name="preferedexchangetypefield", type=PreferedExchangeTypeField, multiplicity=Multiplicity(1, 1)),
        Property(name="listingtypeselector_4", type=ListingTypeSelector, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
CheckboxesComponent_ListingTypeSelector: BinaryAssociation = BinaryAssociation(
    name="CheckboxesComponent_ListingTypeSelector",
    ends={
        Property(name="checkboxescomponent", type=CheckboxesComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="listingtypeselector_1", type=ListingTypeSelector, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
MainImageComponent_ListingDetailsScreen: BinaryAssociation = BinaryAssociation(
    name="MainImageComponent_ListingDetailsScreen",
    ends={
        Property(name="mainimagecomponent", type=MainImageComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="listingdetailsscreen_4", type=ListingDetailsScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
PriceField_ListingTypeSelector: BinaryAssociation = BinaryAssociation(
    name="PriceField_ListingTypeSelector",
    ends={
        Property(name="pricefield", type=PriceField, multiplicity=Multiplicity(1, 1)),
        Property(name="listingtypeselector_2", type=ListingTypeSelector, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ImageGalleryComponent_ListingDetailsScreen: BinaryAssociation = BinaryAssociation(
    name="ImageGalleryComponent_ListingDetailsScreen",
    ends={
        Property(name="imagegallerycomponent", type=ImageGalleryComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="listingdetailsscreen_5", type=ListingDetailsScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
PriceLabel_SaleDetailsComponent: BinaryAssociation = BinaryAssociation(
    name="PriceLabel_SaleDetailsComponent",
    ends={
        Property(name="saledetailscomponent_2", type=SaleDetailsComponent, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="pricelabel", type=PriceLabel, multiplicity=Multiplicity(1, 1))
    }
)
ProductTitleLabel_ListingDetailsScreen: BinaryAssociation = BinaryAssociation(
    name="ProductTitleLabel_ListingDetailsScreen",
    ends={
        Property(name="producttitlelabel", type=ProductTitleLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="listingdetailsscreen_6", type=ListingDetailsScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
BidNowButton_AuctionDetailsComponent: BinaryAssociation = BinaryAssociation(
    name="BidNowButton_AuctionDetailsComponent",
    ends={
        Property(name="bidnowbutton", type=BidNowButton, multiplicity=Multiplicity(1, 1)),
        Property(name="auctiondetailscomponent_1", type=AuctionDetailsComponent, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ProductDescriptionLabel_ListingDetailsScreen: BinaryAssociation = BinaryAssociation(
    name="ProductDescriptionLabel_ListingDetailsScreen",
    ends={
        Property(name="productdescriptionlabel", type=ProductDescriptionLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="listingdetailsscreen_7", type=ListingDetailsScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
BidField_AuctionDetailsComponent: BinaryAssociation = BinaryAssociation(
    name="BidField_AuctionDetailsComponent",
    ends={
        Property(name="bidfield", type=BidField, multiplicity=Multiplicity(1, 1)),
        Property(name="auctiondetailscomponent_2", type=AuctionDetailsComponent, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
BuyNowButton_SaleDetailsComponent: BinaryAssociation = BinaryAssociation(
    name="BuyNowButton_SaleDetailsComponent",
    ends={
        Property(name="buynowbutton", type=BuyNowButton, multiplicity=Multiplicity(1, 1)),
        Property(name="saledetailscomponent_1", type=SaleDetailsComponent, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ExchangeNowButton_ExchangeDetailsComponent: BinaryAssociation = BinaryAssociation(
    name="ExchangeNowButton_ExchangeDetailsComponent",
    ends={
        Property(name="exchangenowbutton", type=ExchangeNowButton, multiplicity=Multiplicity(1, 1)),
        Property(name="exchangedetailscomponent_1", type=ExchangeDetailsComponent, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
TopBarComponent_CommonScreen: BinaryAssociation = BinaryAssociation(
    name="TopBarComponent_CommonScreen",
    ends={
        Property(name="commonscreen_12", type=CommonScreen, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="topbarcomponent", type=TopBarComponent, multiplicity=Multiplicity(1, 1))
    }
)
ProposedExchangeField_ExchangeDetailsComponent: BinaryAssociation = BinaryAssociation(
    name="ProposedExchangeField_ExchangeDetailsComponent",
    ends={
        Property(name="proposedexchangefield", type=ProposedExchangeField, multiplicity=Multiplicity(1, 1)),
        Property(name="exchangedetailscomponent_2", type=ExchangeDetailsComponent, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
MessageCardComponent_MessageListComponent: BinaryAssociation = BinaryAssociation(
    name="MessageCardComponent_MessageListComponent",
    ends={
        Property(name="messagecardcomponent", type=MessageCardComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="messagelistcomponent_1", type=MessageListComponent, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
MenuButton_TopBarComponent: BinaryAssociation = BinaryAssociation(
    name="MenuButton_TopBarComponent",
    ends={
        Property(name="menubutton", type=MenuButton, multiplicity=Multiplicity(1, 1)),
        Property(name="topbarcomponent_1", type=TopBarComponent, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
FooterComponent_HomeScreen: BinaryAssociation = BinaryAssociation(
    name="FooterComponent_HomeScreen",
    ends={
        Property(name="footercomponent", type=FooterComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="homescreen_2", type=HomeScreen, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ProfileButton_TopBarComponent: BinaryAssociation = BinaryAssociation(
    name="ProfileButton_TopBarComponent",
    ends={
        Property(name="profilebutton", type=ProfileButton, multiplicity=Multiplicity(1, 1)),
        Property(name="topbarcomponent_2", type=TopBarComponent, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ViewExchangesButton_TopBarComponent: BinaryAssociation = BinaryAssociation(
    name="ViewExchangesButton_TopBarComponent",
    ends={
        Property(name="topbarcomponent_6", type=TopBarComponent, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="viewexchangesbutton", type=ViewExchangesButton, multiplicity=Multiplicity(1, 1))
    }
)
LogoutButton_TopBarComponent: BinaryAssociation = BinaryAssociation(
    name="LogoutButton_TopBarComponent",
    ends={
        Property(name="logoutbutton", type=LogoutButton, multiplicity=Multiplicity(1, 1)),
        Property(name="topbarcomponent_3", type=TopBarComponent, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
SaleCheckbox_CheckboxesComponent: BinaryAssociation = BinaryAssociation(
    name="SaleCheckbox_CheckboxesComponent",
    ends={
        Property(name="salecheckbox", type=SaleCheckbox, multiplicity=Multiplicity(1, 1)),
        Property(name="checkboxescomponent_1", type=CheckboxesComponent, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ViewAuctionsButton_TopBarComponent: BinaryAssociation = BinaryAssociation(
    name="ViewAuctionsButton_TopBarComponent",
    ends={
        Property(name="viewauctionsbutton", type=ViewAuctionsButton, multiplicity=Multiplicity(1, 1)),
        Property(name="topbarcomponent_4", type=TopBarComponent, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
AuctionCheckbox_CheckboxesComponent: BinaryAssociation = BinaryAssociation(
    name="AuctionCheckbox_CheckboxesComponent",
    ends={
        Property(name="auctioncheckbox", type=AuctionCheckbox, multiplicity=Multiplicity(1, 1)),
        Property(name="checkboxescomponent_2", type=CheckboxesComponent, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ViewSalesButton_TopBarComponent: BinaryAssociation = BinaryAssociation(
    name="ViewSalesButton_TopBarComponent",
    ends={
        Property(name="viewsalesbutton", type=ViewSalesButton, multiplicity=Multiplicity(1, 1)),
        Property(name="topbarcomponent_5", type=TopBarComponent, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ExchangeCheckbox_CheckboxesComponent: BinaryAssociation = BinaryAssociation(
    name="ExchangeCheckbox_CheckboxesComponent",
    ends={
        Property(name="exchangecheckbox", type=ExchangeCheckbox, multiplicity=Multiplicity(1, 1)),
        Property(name="checkboxescomponent_3", type=CheckboxesComponent, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="gui_metamodel",
    types={Frontend, CommonScreen, ChatScreen, LoginScreen, HomeScreen, NewMessageField, SendButton, MessageListComponent, UsernameField, PasswordField, LoginButton, EditProfileButton, MessageCardComponent, TransactionHistoryScreen, ProfileContentsComponent, TransactionListComponent, AppPresentationComponent, TransactionCardComponent, FooterComponent, ListingsScreen, ProfileScreen, ListingsListComponent, NotFoundScreen, ReviewScreen, EnterListingComponent, NewReviewFormComponent, ListingsFilterButton, ReviewCardComponent, SaleCardComponent, ReviewListComponent, AuctionCardComponent, ExchangeCardComponent, ListingDetailsScreen, ReportScreen, SaleDetailsComponent, ExchangeDetailsComponent, NewReportFormComponent, ReportCardComponent, AuctionDetailsComponent, ReportManagementComponent, CreateListingScreen, ProductTitleField, LocationField, ProductDescriptionField, MultipleImagesUploadComponent, SingleImageUploadComponent, SubmitListingButton, ListingTypeSelector, CheckboxesComponent, AuctionClosingTimeField, PriceField, ProfileButton, PreferedExchangeTypeField, LogoutButton, ImageGalleryComponent, TopBarComponent, ProductTitleLabel, ViewAuctionsButton, PriceLabel, ViewSalesButton, BidField, BidNowButton, ViewExchangesButton, BuyNowButton, SaleCheckbox, MainImageComponent, AuctionCheckbox, ExchangeNowButton, ExchangeCheckbox, ProductDescriptionLabel, ProposedExchangeField, MenuButton},
    associations={SendButton_ChatScreen, NewMessageField_ChatScreen, MessageListComponent_ChatScreen, UsernameField_LoginScreen, HomeScreen_CommonScreen, PasswordField_LoginScreen, CommonScreen_Frontend, ProfileContentsComponent_ProfileScreen, LoginButton_LoginScreen, EditProfileButton_ProfileScreen, AppPresentationComponent_HomeScreen, ProfileScreen_CommonScreen, LoginScreen_CommonScreen, NotFoundScreen_CommonScreen, ChatScreen_CommonScreen, NewReviewFormComponent_ReviewScreen, ReviewScreen_CommonScreen, ReviewCardComponent_ReviewScreen, ReportScreen_CommonScreen, ReviewListComponent_ReviewScreen, NewReportFormComponent_ReportScreen, TransactionListComponent_TransactionHistoryScreen, ReportCardComponent_ReportScreen, TransactionCardComponent_TransactionHistoryScreen, ReportManagementComponent_ReportScreen, TransactionHistoryScreen_CommonScreen, ExchangeCardComponent_ListingsListComponent, ListingsListComponent_ListingsScreen, AuctionCardComponent_ListingsListComponent, EnterListingComponent_ListingsScreen, SaleDetailsComponent_ListingDetailsScreen, ListingsFilterButton_ListingsScreen, ListingsScreen_CommonScreen, ExchangeDetailsComponent_ListingDetailsScreen, AuctionDetailsComponent_ListingDetailsScreen, SaleCardComponent_ListingsListComponent, CreateListingScreen_CommonScreen, ListingDetailsScreen_CommonScreen, MultipleImagesUploadComponent_CreateListingScreen, ProductTitleField_CreateListingScreen, LocationField_CreateListingScreen, SingleImageUploadComponent_CreateListingScreen, ProductDescriptionField_CreateListingScreen, SubmitListingButton_CreateListingScreen, AuctionClosingTimeField_ListingTypeSelector, ListingTypeSelector_CreateListingScreen, PreferedExchangeTypeField_ListingTypeSelector, CheckboxesComponent_ListingTypeSelector, MainImageComponent_ListingDetailsScreen, PriceField_ListingTypeSelector, ImageGalleryComponent_ListingDetailsScreen, PriceLabel_SaleDetailsComponent, ProductTitleLabel_ListingDetailsScreen, BidNowButton_AuctionDetailsComponent, ProductDescriptionLabel_ListingDetailsScreen, BidField_AuctionDetailsComponent, BuyNowButton_SaleDetailsComponent, ExchangeNowButton_ExchangeDetailsComponent, TopBarComponent_CommonScreen, ProposedExchangeField_ExchangeDetailsComponent, MessageCardComponent_MessageListComponent, MenuButton_TopBarComponent, FooterComponent_HomeScreen, ProfileButton_TopBarComponent, ViewExchangesButton_TopBarComponent, LogoutButton_TopBarComponent, SaleCheckbox_CheckboxesComponent, ViewAuctionsButton_TopBarComponent, AuctionCheckbox_CheckboxesComponent, ViewSalesButton_TopBarComponent, ExchangeCheckbox_CheckboxesComponent},
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
