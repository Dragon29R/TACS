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

TransactionStatus: Enumeration = Enumeration(
    name="TransactionStatus",
    literals={
            EnumerationLiteral(name="OPEN"),
			EnumerationLiteral(name="CONCLUDED"),
			EnumerationLiteral(name="CANCELLED"),
			EnumerationLiteral(name="WAITING")
    }
)

Condition: Enumeration = Enumeration(
    name="Condition",
    literals={
            EnumerationLiteral(name="New"),
			EnumerationLiteral(name="Used")
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
User_m_createItem: Method = Method(name="createItem", parameters={})
User_m_editProfile: Method = Method(name="editProfile", parameters={})
User_m_joinCommunity: Method = Method(name="joinCommunity", parameters={})
User_m_createCommunity: Method = Method(name="createCommunity", parameters={})
User.attributes={User_email, User_fullName, User_avatarUrl, User_displayName, User_reputationScore, User_description, User_id}
User.methods={User_m_editProfile, User_m_createItem, User_m_joinCommunity, User_m_createCommunity}

# Community class attributes and methods
Community_id: Property = Property(name="id", type=IntegerType)
Community_name: Property = Property(name="name", type=StringType)
Community_locale: Property = Property(name="locale", type=StringType)
Community_avatarUrl: Property = Property(name="avatarUrl", type=StringType)
Community_description: Property = Property(name="description", type=StringType)
Community_m_addMember: Method = Method(name="addMember", parameters={})
Community_m_removeMember: Method = Method(name="removeMember", parameters={})
Community_m_changeRoles: Method = Method(name="changeRoles", parameters={})
Community.attributes={Community_description, Community_avatarUrl, Community_locale, Community_name, Community_id}
Community.methods={Community_m_removeMember, Community_m_addMember, Community_m_changeRoles}

# Membership class attributes and methods
Membership_role: Property = Property(name="role", type=Role)
Membership_status: Property = Property(name="status", type=Status)
Membership_id: Property = Property(name="id", type=IntegerType)
Membership.attributes={Membership_status, Membership_role, Membership_id}

# Item class attributes and methods
Item_id: Property = Property(name="id", type=IntegerType)
Item_title: Property = Property(name="title", type=StringType)
Item_description: Property = Property(name="description", type=StringType)
Item_condition: Property = Property(name="condition", type=Condition)
Item_m_updateDetails: Method = Method(name="updateDetails", parameters={})
Item.attributes={Item_description, Item_id, Item_condition, Item_title}
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
Transaction_m_open: Method = Method(name="open", parameters={})
Transaction_m_cancel: Method = Method(name="cancel", parameters={})
Transaction_m_conclude: Method = Method(name="conclude", parameters={})
Transaction.attributes={Transaction_concludedAt, Transaction_startAt, Transaction_endTime, Transaction_id, Transaction_status}
Transaction.methods={Transaction_m_open, Transaction_m_conclude, Transaction_m_cancel}

# Sale class attributes and methods
Sale_price: Property = Property(name="price", type=FloatType)
Sale.attributes={Sale_price}

# Exchange class attributes and methods

# Bid class attributes and methods
Bid_value: Property = Property(name="value", type=FloatType)
Bid_placedAt: Property = Property(name="placedAt", type=DateType)
Bid_id: Property = Property(name="id", type=IntegerType)
Bid.attributes={Bid_placedAt, Bid_id, Bid_value}

# ChatThread class attributes and methods
ChatThread_id: Property = Property(name="id", type=StringType)
ChatThread_m_sendMessage: Method = Method(name="sendMessage", parameters={})
ChatThread.attributes={ChatThread_id}
ChatThread.methods={ChatThread_m_sendMessage}

# Message class attributes and methods
Message_id: Property = Property(name="id", type=IntegerType)
Message_sentAt: Property = Property(name="sentAt", type=StringType)
Message_text: Property = Property(name="text", type=StringType)
Message.attributes={Message_sentAt, Message_text, Message_id}

# Review class attributes and methods
Review_createdAt: Property = Property(name="createdAt", type=DateType)
Review_id: Property = Property(name="id", type=IntegerType)
Review_score: Property = Property(name="score", type=IntegerType)
Review_comment: Property = Property(name="comment", type=StringType)
Review.attributes={Review_id, Review_comment, Review_score, Review_createdAt}

# Auction class attributes and methods
Auction_minBid: Property = Property(name="minBid", type=FloatType)
Auction_currentBid: Property = Property(name="currentBid", type=FloatType)
Auction.attributes={Auction_minBid, Auction_currentBid}

# Category class attributes and methods
Category_name: Property = Property(name="name", type=StringType)
Category_id: Property = Property(name="id", type=IntegerType)
Category.attributes={Category_id, Category_name}

# PhotoUrl class attributes and methods
PhotoUrl_url: Property = Property(name="url", type=StringType)
PhotoUrl_id: Property = Property(name="id", type=IntegerType)
PhotoUrl.attributes={PhotoUrl_id, PhotoUrl_url}

# Relationships
Transaction_User: BinaryAssociation = BinaryAssociation(
    name="Transaction_User",
    ends={
        Property(name="transaction_1", type=Transaction, multiplicity=Multiplicity(0, 9999)),
        Property(name="buyer", type=User, multiplicity=Multiplicity(1, 1))
    }
)
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
Report_Membership: BinaryAssociation = BinaryAssociation(
    name="Report_Membership",
    ends={
        Property(name="report", type=Report, multiplicity=Multiplicity(0, 9999)),
        Property(name="membership", type=Membership, multiplicity=Multiplicity(1, 1))
    }
)
Transaction_Item: BinaryAssociation = BinaryAssociation(
    name="Transaction_Item",
    ends={
        Property(name="transaction", type=Transaction, multiplicity=Multiplicity(1, 1)),
        Property(name="item", type=Item, multiplicity=Multiplicity(1, 1))
    }
)
Exchange_Item: BinaryAssociation = BinaryAssociation(
    name="Exchange_Item",
    ends={
        Property(name="offeredItems", type=Exchange, multiplicity=Multiplicity(0, 9999)),
        Property(name="item_1", type=Item, multiplicity=Multiplicity(0, 9999))
    }
)
Item_ChatThread: BinaryAssociation = BinaryAssociation(
    name="Item_ChatThread",
    ends={
        Property(name="item_2", type=Item, multiplicity=Multiplicity(1, 1)),
        Property(name="chatthread", type=ChatThread, multiplicity=Multiplicity(0, 9999))
    }
)
Item_User: BinaryAssociation = BinaryAssociation(
    name="Item_User",
    ends={
        Property(name="ownedBy", type=Item, multiplicity=Multiplicity(0, 9999)),
        Property(name="user", type=User, multiplicity=Multiplicity(1, 1))
    }
)
ChatThread_User: BinaryAssociation = BinaryAssociation(
    name="ChatThread_User",
    ends={
        Property(name="chatthread_1", type=ChatThread, multiplicity=Multiplicity(0, 9999)),
        Property(name="participants", type=User, multiplicity=Multiplicity(2, 2))
    }
)
User_Message: BinaryAssociation = BinaryAssociation(
    name="User_Message",
    ends={
        Property(name="user_2", type=User, multiplicity=Multiplicity(1, 1)),
        Property(name="message_1", type=Message, multiplicity=Multiplicity(0, 9999))
    }
)
Message_ChatThread: BinaryAssociation = BinaryAssociation(
    name="Message_ChatThread",
    ends={
        Property(name="message", type=Message, multiplicity=Multiplicity(1, 1)),
        Property(name="chatthread_2", type=ChatThread, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
Review_User: BinaryAssociation = BinaryAssociation(
    name="Review_User",
    ends={
        Property(name="review", type=Review, multiplicity=Multiplicity(0, 9999)),
        Property(name="writenBy", type=User, multiplicity=Multiplicity(1, 1))
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
Category_Item: BinaryAssociation = BinaryAssociation(
    name="Category_Item",
    ends={
        Property(name="category", type=Category, multiplicity=Multiplicity(0, 9999)),
        Property(name="item_3", type=Item, multiplicity=Multiplicity(0, 9999))
    }
)
PhotoUrl_Item: BinaryAssociation = BinaryAssociation(
    name="PhotoUrl_Item",
    ends={
        Property(name="photourl", type=PhotoUrl, multiplicity=Multiplicity(1, 9999)),
        Property(name="item_4", type=Item, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_Sale_Transaction = Generalization(general=Transaction, specific=Sale)
gen_Exchange_Transaction = Generalization(general=Transaction, specific=Exchange)
gen_Auction_Transaction = Generalization(general=Transaction, specific=Auction)

# Domain Model
domain_model = DomainModel(
    name="Class_Diagram",
    types={User, Community, Membership, Item, Report, Transaction, Sale, Exchange, Bid, ChatThread, Message, Review, Auction, Category, PhotoUrl, Role, Status, TransactionStatus, Condition},
    associations={Transaction_User, Transaction_User_1, Bid_User, Report_Membership, Transaction_Item, Exchange_Item, Item_ChatThread, Item_User, ChatThread_User, User_Message, Message_ChatThread, Review_User, Review_User_1, Auction_Bid, User_Membership, Membership_Community, Category_Item, PhotoUrl_Item},
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
    name="structural_model",
    models=[domain_model],
    owner="User",
    metadata=metadata
)
