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

# Enumerations
TransactionStatus: Enumeration = Enumeration(
    name="TransactionStatus",
    literals={
            EnumerationLiteral(name="WAITING"),
			EnumerationLiteral(name="OPEN"),
			EnumerationLiteral(name="CONCLUDED"),
			EnumerationLiteral(name="CANCELLED")
    }
)

Condition: Enumeration = Enumeration(
    name="Condition",
    literals={
            EnumerationLiteral(name="New"),
			EnumerationLiteral(name="Used")
    }
)

ColorScheme: Enumeration = Enumeration(
    name="ColorScheme",
    literals={
            EnumerationLiteral(name="Light"),
			EnumerationLiteral(name="Dark")
    }
)

Role: Enumeration = Enumeration(
    name="Role",
    literals={
            EnumerationLiteral(name="ADMIN"),
			EnumerationLiteral(name="MEMBER")
    }
)

Status: Enumeration = Enumeration(
    name="Status",
    literals={
            EnumerationLiteral(name="ACTIVE"),
			EnumerationLiteral(name="PENDING"),
			EnumerationLiteral(name="BANNED")
    }
)

# Classes
User = Class(name="User")
Community = Class(name="Community")
Membership = Class(name="Membership")
Item = Class(name="Item")
Report = Class(name="Report")
Transaction = Class(name="Transaction", is_abstract=True)
Sale = Class(name="Sale")
Exchange = Class(name="Exchange")
Bid = Class(name="Bid")
ChatThread = Class(name="ChatThread")
Message = Class(name="Message")
Review = Class(name="Review")
Auction = Class(name="Auction")
Category = Class(name="Category")
PhotoUrl = Class(name="PhotoUrl")

# User class attributes and methods
User_id: Property = Property(name="id", type=IntegerType)
User_displayName: Property = Property(name="displayName", type=StringType)
User_email: Property = Property(name="email", type=StringType)
User_avatarUrl: Property = Property(name="avatarUrl", type=StringType)
User_description: Property = Property(name="description", type=StringType)
User_reputationScore: Property = Property(name="reputationScore", type=IntegerType)
User_fullName: Property = Property(name="fullName", type=StringType)
User_nickname: Property = Property(name="nickname", type=StringType)
User_address: Property = Property(name="address", type=StringType)
User_age: Property = Property(name="age", type=IntegerType)
User_m_createItem: Method = Method(name="createItem", parameters={})
User_m_editProfile: Method = Method(name="editProfile", parameters={})
User_m_joinCommunity: Method = Method(name="joinCommunity", parameters={})
User_m_createCommunity: Method = Method(name="createCommunity", parameters={})
User.attributes={User_nickname, User_reputationScore, User_age, User_email, User_displayName, User_id, User_address, User_description, User_fullName, User_avatarUrl}
User.methods={User_m_joinCommunity, User_m_createItem, User_m_createCommunity, User_m_editProfile}

# Community class attributes and methods
Community_logo: Property = Property(name="logo", type=StringType)
Community_description: Property = Property(name="description", type=StringType)
Community_maxUsers: Property = Property(name="maxUsers", type=IntegerType)
Community_rules: Property = Property(name="rules", type=StringType)
Community_defaultLanguage: Property = Property(name="defaultLanguage", type=StringType)
Community_color: Property = Property(name="color", type=StringType)
Community_colorScheme: Property = Property(name="colorScheme", type=ColorScheme)
Community_fontFamily: Property = Property(name="fontFamily", type=StringType)
Community_backgroundImage: Property = Property(name="backgroundImage", type=StringType)
Community_id: Property = Property(name="id", type=IntegerType)
Community_name: Property = Property(name="name", type=StringType)
Community_locale: Property = Property(name="locale", type=StringType)
Community_m_addMember: Method = Method(name="addMember", parameters={})
Community_m_removeMember: Method = Method(name="removeMember", parameters={})
Community_m_changeRoles: Method = Method(name="changeRoles", parameters={})
Community.attributes={Community_locale, Community_logo, Community_description, Community_colorScheme, Community_fontFamily, Community_name, Community_id, Community_maxUsers, Community_backgroundImage, Community_rules, Community_color, Community_defaultLanguage}
Community.methods={Community_m_removeMember, Community_m_addMember, Community_m_changeRoles}

# Membership class attributes and methods
Membership_role: Property = Property(name="role", type=Role)
Membership_status: Property = Property(name="status", type=Status)
Membership_id: Property = Property(name="id", type=IntegerType)
Membership.attributes={Membership_id, Membership_role, Membership_status}

# Item class attributes and methods
Item_id: Property = Property(name="id", type=IntegerType)
Item_title: Property = Property(name="title", type=StringType)
Item_description: Property = Property(name="description", type=StringType)
Item_condition: Property = Property(name="condition", type=Condition)
Item_location: Property = Property(name="location", type=StringType)
Item_m_updateDetails: Method = Method(name="updateDetails", parameters={})
Item.attributes={Item_location, Item_condition, Item_id, Item_title, Item_description}
Item.methods={Item_m_updateDetails}

# Report class attributes and methods
Report_description: Property = Property(name="description", type=StringType)
Report_id: Property = Property(name="id", type=IntegerType)
Report.attributes={Report_id, Report_description}

# Transaction class attributes and methods
Transaction_status: Property = Property(name="status", type=TransactionStatus)
Transaction_endTime: Property = Property(name="endTime", type=DateType)
Transaction_startAt: Property = Property(name="startAt", type=DateType)
Transaction_concludedAt: Property = Property(name="concludedAt", type=DateType)
Transaction_id: Property = Property(name="id", type=IntegerType)
Transaction_enableBidding: Property = Property(name="enableBidding", type=BooleanType)
Transaction_enableSale: Property = Property(name="enableSale", type=BooleanType)
Transaction_m_open: Method = Method(name="open", parameters={})
Transaction_m_cancel: Method = Method(name="cancel", parameters={})
Transaction_m_conclude: Method = Method(name="conclude", parameters={})
Transaction.attributes={Transaction_enableBidding, Transaction_status, Transaction_concludedAt, Transaction_id, Transaction_enableSale, Transaction_endTime, Transaction_startAt}
Transaction.methods={Transaction_m_conclude, Transaction_m_open, Transaction_m_cancel}

# Sale class attributes and methods
Sale_price: Property = Property(name="price", type=FloatType)
Sale.attributes={Sale_price}

# Exchange class attributes and methods

# Bid class attributes and methods
Bid_value: Property = Property(name="value", type=FloatType)
Bid_placedAt: Property = Property(name="placedAt", type=DateType)
Bid_id: Property = Property(name="id", type=IntegerType)
Bid.attributes={Bid_id, Bid_placedAt, Bid_value}

# ChatThread class attributes and methods
ChatThread_id: Property = Property(name="id", type=StringType)
ChatThread_m_sendMessage: Method = Method(name="sendMessage", parameters={})
ChatThread.attributes={ChatThread_id}
ChatThread.methods={ChatThread_m_sendMessage}

# Message class attributes and methods
Message_id: Property = Property(name="id", type=IntegerType)
Message_sentAt: Property = Property(name="sentAt", type=StringType)
Message_text: Property = Property(name="text", type=StringType)
Message.attributes={Message_text, Message_id, Message_sentAt}

# Review class attributes and methods
Review_score: Property = Property(name="score", type=IntegerType)
Review_comment: Property = Property(name="comment", type=StringType)
Review_createdAt: Property = Property(name="createdAt", type=DateType)
Review_id: Property = Property(name="id", type=IntegerType)
Review.attributes={Review_comment, Review_id, Review_score, Review_createdAt}

# Auction class attributes and methods
Auction_minBid: Property = Property(name="minBid", type=FloatType)
Auction_currentBid: Property = Property(name="currentBid", type=FloatType)
Auction.attributes={Auction_currentBid, Auction_minBid}

# Category class attributes and methods
Category_name: Property = Property(name="name", type=StringType)
Category_id: Property = Property(name="id", type=IntegerType)
Category.attributes={Category_name, Category_id}

# PhotoUrl class attributes and methods
PhotoUrl_url: Property = Property(name="url", type=StringType)
PhotoUrl_id: Property = Property(name="id", type=IntegerType)
PhotoUrl.attributes={PhotoUrl_id, PhotoUrl_url}

# Relationships
Transaction_User_1: BinaryAssociation = BinaryAssociation(
    name="Transaction_User_1",
    ends={
        Property(name="transaction_2", type=Transaction, multiplicity=Multiplicity(0, 9999)),
        Property(name="seller", type=User, multiplicity=Multiplicity(1, 1))
    }
)
Bid_User: BinaryAssociation = BinaryAssociation(
    name="Bid_User",
    ends={
        Property(name="from", type=Bid, multiplicity=Multiplicity(0, 9999)),
        Property(name="user_1", type=User, multiplicity=Multiplicity(1, 1))
    }
)
Exchange_Item: BinaryAssociation = BinaryAssociation(
    name="Exchange_Item",
    ends={
        Property(name="offeredItems", type=Exchange, multiplicity=Multiplicity(0, 9999)),
        Property(name="item_1", type=Item, multiplicity=Multiplicity(0, 9999))
    }
)
Report_Membership: BinaryAssociation = BinaryAssociation(
    name="Report_Membership",
    ends={
        Property(name="report", type=Report, multiplicity=Multiplicity(0, 9999)),
        Property(name="membership", type=Membership, multiplicity=Multiplicity(1, 1))
    }
)
Item_ChatThread: BinaryAssociation = BinaryAssociation(
    name="Item_ChatThread",
    ends={
        Property(name="item_2", type=Item, multiplicity=Multiplicity(1, 1)),
        Property(name="chatthread", type=ChatThread, multiplicity=Multiplicity(0, 9999))
    }
)
Transaction_Item: BinaryAssociation = BinaryAssociation(
    name="Transaction_Item",
    ends={
        Property(name="transaction", type=Transaction, multiplicity=Multiplicity(1, 1)),
        Property(name="item", type=Item, multiplicity=Multiplicity(1, 1))
    }
)
ChatThread_User: BinaryAssociation = BinaryAssociation(
    name="ChatThread_User",
    ends={
        Property(name="chatthread_1", type=ChatThread, multiplicity=Multiplicity(0, 9999)),
        Property(name="participants", type=User, multiplicity=Multiplicity(2, 2))
    }
)
Item_User: BinaryAssociation = BinaryAssociation(
    name="Item_User",
    ends={
        Property(name="ownedBy", type=Item, multiplicity=Multiplicity(0, 9999)),
        Property(name="user", type=User, multiplicity=Multiplicity(1, 1))
    }
)
Message_ChatThread: BinaryAssociation = BinaryAssociation(
    name="Message_ChatThread",
    ends={
        Property(name="message", type=Message, multiplicity=Multiplicity(1, 1)),
        Property(name="chatthread_2", type=ChatThread, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
Transaction_User: BinaryAssociation = BinaryAssociation(
    name="Transaction_User",
    ends={
        Property(name="transaction_1", type=Transaction, multiplicity=Multiplicity(0, 9999)),
        Property(name="buyer", type=User, multiplicity=Multiplicity(1, 1))
    }
)
User_Message: BinaryAssociation = BinaryAssociation(
    name="User_Message",
    ends={
        Property(name="user_2", type=User, multiplicity=Multiplicity(1, 1)),
        Property(name="message_1", type=Message, multiplicity=Multiplicity(0, 9999))
    }
)
Category_Item: BinaryAssociation = BinaryAssociation(
    name="Category_Item",
    ends={
        Property(name="category", type=Category, multiplicity=Multiplicity(0, 9999)),
        Property(name="item_3", type=Item, multiplicity=Multiplicity(0, 9999))
    }
)
Review_User: BinaryAssociation = BinaryAssociation(
    name="Review_User",
    ends={
        Property(name="review", type=Review, multiplicity=Multiplicity(0, 9999)),
        Property(name="writenBy", type=User, multiplicity=Multiplicity(1, 1))
    }
)
PhotoUrl_Item: BinaryAssociation = BinaryAssociation(
    name="PhotoUrl_Item",
    ends={
        Property(name="photourl", type=PhotoUrl, multiplicity=Multiplicity(1, 9999)),
        Property(name="item_4", type=Item, multiplicity=Multiplicity(1, 1))
    }
)
Review_User_1: BinaryAssociation = BinaryAssociation(
    name="Review_User_1",
    ends={
        Property(name="review_1", type=Review, multiplicity=Multiplicity(0, 9999)),
        Property(name="writenAbout", type=User, multiplicity=Multiplicity(1, 1))
    }
)
Auction_Bid: BinaryAssociation = BinaryAssociation(
    name="Auction_Bid",
    ends={
        Property(name="auction", type=Auction, multiplicity=Multiplicity(1, 1)),
        Property(name="bid", type=Bid, multiplicity=Multiplicity(0, 9999))
    }
)
User_Membership: BinaryAssociation = BinaryAssociation(
    name="User_Membership",
    ends={
        Property(name="user_3", type=User, multiplicity=Multiplicity(1, 9999)),
        Property(name="membership_1", type=Membership, multiplicity=Multiplicity(1, 9999))
    }
)
Membership_Community: BinaryAssociation = BinaryAssociation(
    name="Membership_Community",
    ends={
        Property(name="membership_2", type=Membership, multiplicity=Multiplicity(1, 9999)),
        Property(name="community", type=Community, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_Sale_Transaction = Generalization(general=Transaction, specific=Sale)
gen_Exchange_Transaction = Generalization(general=Transaction, specific=Exchange)
gen_Auction_Transaction = Generalization(general=Transaction, specific=Auction)


# OCL Constraints
constraint_User_0_1: Constraint = Constraint(
    name="constraint_User_0_1",
    context=User,
    expression="Context User inv RepScorePositive:  self.reputationScore >= 0 and self.reputationScore <= 5Context User inv NamesNotEmpty:  self.displayName.size() > 0 and self.fullName.size() > 0 and self.email.size() > 0Context User inv UniqueId:  User.allInstances()->isUnique(id)Context User inv UniqueEmail:  User.allInstances()->isUnique(email)Context User inv DescriptionLength:  self.description.isDefined() implies self.description.size() <= 1000",
    language="OCL"
)
constraint_Item_1_1: Constraint = Constraint(
    name="constraint_Item_1_1",
    context=Item,
    expression="Context Item inv UniqueId:  Item.allInstances()->isUnique(id)Context Item inv TextNotEmpty:  self.title.size() > 0 and self.description.size() > 0Context Item inv HasAtLeastOneCategory:  self.categories->notEmpty()Context Item inv HasAtLeastOnePhoto:  self.photoUrls->notEmpty()Context Item inv CategoryStringsNotEmpty:  self.categories->forAll(c | c.size() > 0)Context Item inv PhotoStringsNotEmpty:  self.photoUrls->forAll(p | p.size() > 0)Context Item inv UniqueCategories:  self.categories->size() = self.categories->asSet()->size()",
    language="OCL"
)
constraint_ChatThread_2_1: Constraint = Constraint(
    name="constraint_ChatThread_2_1",
    context=ChatThread,
    expression="Context ChatThread inv UniqueId:  ChatThread.allInstances()->isUnique(id)Context ChatThread inv IdNotEmpty:  self.id.size() > 0Context ChatThread inv DistinctUsers:  self.participants->size() = 2Context ChatThread inv OwnerIsParticipant:  self.participants->includes(self.item.owner)",
    language="OCL"
)
constraint_Transaction_3_1: Constraint = Constraint(
    name="constraint_Transaction_3_1",
    context=Transaction,
    expression="Context Transaction inv EndAfterStart:  self.endTime > self.startAtContext Transaction inv NoSelfTransaction:  self.seller <> self.buyerContext Transaction inv ConcludedLogic:  (self.status = TransactionStatus::CONCLUDED implies self.concludedAt.isDefined()) and  (self.status <> TransactionStatus::CONCLUDED implies not self.concludedAt.isDefined())Context Transaction inv SellerMustBeOwner:  self.item.owner = self.sellerContext Transaction inv CannotBidAndSell:  not (self.enableBidding and self.enableSale)",
    language="OCL"
)
constraint_Sale_4_1: Constraint = Constraint(
    name="constraint_Sale_4_1",
    context=Sale,
    expression="Context Sale inv PositivePrice:  self.price > 0",
    language="OCL"
)
constraint_Auction_5_1: Constraint = Constraint(
    name="constraint_Auction_5_1",
    context=Auction,
    expression="Context Auction inv PositiveMinBid:  self.minBid > 0Context Auction inv CurrentBidValid:  self.currentBid.isDefined() implies self.currentBid >= self.minBid",
    language="OCL"
)
constraint_Exchange_6_1: Constraint = Constraint(
    name="constraint_Exchange_6_1",
    context=Exchange,
    expression="Context Exchange inv OfferedItemsOwnedByBuyer:  self.offeredItems->forAll(i | i.owner = self.buyer)",
    language="OCL"
)
constraint_Bid_7_1: Constraint = Constraint(
    name="constraint_Bid_7_1",
    context=Bid,
    expression="Context Bid inv PositiveValue:  self.value > 0Context Bid inv ValueAtLeastMinBid:  self.value >= self.auction.minBidContext Bid inv BidWithinAuctionTime:  self.placedAt >= self.auction.startAt and self.placedAt <= self.auction.endTimeContext Bid inv BidderNotSeller:  self.from <> self.auction.seller",
    language="OCL"
)
constraint_Message_8_1: Constraint = Constraint(
    name="constraint_Message_8_1",
    context=Message,
    expression="Context Message inv TextNotEmpty:  self.text.size() > 0Context Message inv SentAtNotEmpty:  self.sentAt.size() > 0Context Message inv SenderIsParticipant:  self.chatThread.participants->includes(self.sender)",
    language="OCL"
)
constraint_Review_9_1: Constraint = Constraint(
    name="constraint_Review_9_1",
    context=Review,
    expression="Context Review inv ScoreRange:  self.score >= 1 and self.score <= 5Context Review inv CommentNotEmpty:  self.comment.size() > 0Context Review inv NoSelfReview:  self.writtenBy <> self.writtenAboutContext Review inv CreatedAtNotEmpty:  self.createdAt.size() > 0",
    language="OCL"
)
constraint_Community_10_1: Constraint = Constraint(
    name="constraint_Community_10_1",
    context=Community,
    expression="Context Community inv UniqueId:  Community.allInstances()->isUnique(id)Context Community inv UniqueName:  Community.allInstances()->isUnique(name)Context Community inv RequiredFieldsNotEmpty:  self.id.size() > 0 and self.name.size() > 0Context Community inv DescriptionLength:  self.description.isDefined() implies self.description.size() <= 2000",
    language="OCL"
)
constraint_Membership_11_1: Constraint = Constraint(
    name="constraint_Membership_11_1",
    context=Membership,
    expression="Context Membership inv BannedNotAdmin:  self.status = Status::BANNED implies self.role <> Role::ADMIN",
    language="OCL"
)
constraint_Report_12_1: Constraint = Constraint(
    name="constraint_Report_12_1",
    context=Report,
    expression="Context Report inv DescriptionNotEmpty:  self.description.size() > 0",
    language="OCL"
)

# Domain Model
domain_model = DomainModel(
    name="Class_Diagram",
    types={User, Community, Membership, Item, Report, Transaction, Sale, Exchange, Bid, ChatThread, Message, Review, Auction, Category, PhotoUrl, TransactionStatus, Condition, ColorScheme, Role, Status},
    associations={Transaction_User_1, Bid_User, Exchange_Item, Report_Membership, Item_ChatThread, Transaction_Item, ChatThread_User, Item_User, Message_ChatThread, Transaction_User, User_Message, Category_Item, Review_User, PhotoUrl_Item, Review_User_1, Auction_Bid, User_Membership, Membership_Community},
    constraints={constraint_User_0_1, constraint_Item_1_1, constraint_ChatThread_2_1, constraint_Transaction_3_1, constraint_Sale_4_1, constraint_Auction_5_1, constraint_Exchange_6_1, constraint_Bid_7_1, constraint_Message_8_1, constraint_Review_9_1, constraint_Community_10_1, constraint_Membership_11_1, constraint_Report_12_1},
    generalizations={gen_Sale_Transaction, gen_Exchange_Transaction, gen_Auction_Transaction},
    metadata=None
)


######################
# PROJECT DEFINITION #
######################

from besser.BUML.metamodel.project import Project
from besser.BUML.metamodel.structural.structural import Metadata

metadata = Metadata(description="TACS project")
project = Project(
    name="structural_metamodel",
    models=[domain_model],
    owner="User",
    metadata=metadata
)
