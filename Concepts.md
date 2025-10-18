# List of Concepts

| **Concept** | **Intrinsic (Attributes)** | **Extrinsic (Connections)** |
|--------------|-----------------------------|------------------------------|
| **User** | displayName, email, avatarUrl?, description?, reputationScore, fullName | Arbitrary number of Transactions (buyer or seller); Arbitrary number of Items; Arbitrary number of reviews (written by/about); Arbitrary number of ChatThreads; Arbitrary number of Messages; Arbitrary number of Memberships |
| **Item** | title, description, categories:list[str], photoUrls:list[str], condition:Condition | May belong to 1 or more Transactions; Owned by 1 User; |
| **Transaction (abstract)** | status:TransactionStatus, endTime:date, startAt:date, concludedAt?:date | Involves 1 Seller (User) and may have 1 Buyer (User); References 1 Item; Specialized by Sale, Exchange, and Auction |
| **Sale** | price:float | Inherits from Transaction |
| **Exchange** | — | Inherits from Transaction, Represents exchange between Items |
| **Auction** | minBid:float, currentBid?:float | Inherits from Transaction; Has arbitrary number of Bids |
| **Bid** | value:float, placedAt:date | Belongs to 1 Auction; Made by 1 User |
| **ChatThread** | id:str | Arbitrary number Messages; Between exactly 2 Users |
| **Message** | text:str, sentAt:str | Belongs to 1 ChatThread; Sent by 1 User |
| **Review** | score:int, comment:str, createdAt:date | Written by 1 User; Written about 1 User |
| **Community** | id:str, name:str, locale?:string, avatarUrl?:str, description?:str | Arbitrary number of Memberships; Contains arbitrary number of Users indirectly through Membership |
| **Membership** | role:Role, status:Status | Links 1 User to 1 Community; May have arbitrary number of Reports |
| **Report** | description:str | References 1 Membership |
| **TransactionStatus (enum)** | {OPEN, CONCLUDED, CANCELLED, WAITING} | Used by Transaction |
| **Role (enum)** | {ADMIN, MEMBER} | Used by Membership |
| **Status (enum)** | {ACTIVE, PENDING, BANNED} | Used by Membership |
| **Condition (enum)** | {NEW, USED} | Used by Item |
