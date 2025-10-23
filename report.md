## Report

This report highlights the inspiration behind the Structural, DSML and GUI metamodels and explains the choices made during their development.  

### Structural Metamodel

Our structural metamodel represents the conceptual structure for a community-based application where users can share, sell or auction their items. 

The whole metamodel revolves around the User and Item interactions, where a User can be part of many communities and act as seller, buyer or participate in actions such as messages, reviewing or community membership.

The Item class abstracts an item of choice and is linked to the transactional layer through ownership, where the item's lifecycle is defined as Waiting (if Item still not published), Open, Concluded (or Sold) and Canceled. Each transaction has distinct subtypes, it can be a Sale, Auction, or Exchange, allowing the user to display their item most conveniently.

The communication subsystem is critical for negotiating communities, comprised of a ChatThread between two user. Additionally, Reviews and Reports are also present, supporting accountability and reliability within the platform. This structure enables and encourages safe social interactions and long-term trustworthiness.

Enumerations such as TransactionStatus, Role, Status and Condition were integrated to constraint attribute values in a predifined consistent way, without overcomplicating and keeping the model focused on simple but structural representations.

The model aims to balance conceptual generality with applicable specificity to create a descriptive yet not overly complex structure. 

