## TACS Report

This report highlights the inspiration behind the Structural, DSML and GUI metamodels and explains the choices made during their development.  

### 1. Structural Metamodel

Our structural metamodel represents the conceptual structure for a community-based application where users can share, sell or auction their items. 

The whole metamodel revolves around the User and Item interactions, where a User can be part of many communities and act as seller, buyer or participate in actions such as messages, reviewing or community membership.

The Item class abstracts an item of choice and is linked to the transactional layer through ownership, where the item's lifecycle is defined as Waiting (if Item still not published), Open, Concluded (or Sold) and Canceled. Each transaction has distinct subtypes, it can be a Sale, Auction, or Exchange, allowing the user to display their item most conveniently.

The communication subsystem is critical for negotiating communities, comprised of a ChatThread between two users. Additionally, Reviews and Reports are also present, supporting accountability and reliability within the platform. This structure enables and encourages safe social interactions and long-term trustworthiness.

Enumerations such as TransactionStatus, Role, Status and Condition were integrated to constraint attribute values in a predifined consistent way, without overcomplicating and keeping the model focused on simple but structural representations.

The model aims to balance conceptual generality with applicable specificity to create a descriptive yet not overly complex structure. 


The main methods were also added, particularly for the most important classes in the model.For instance, the User class will be able to create an item, edit his profile or join/create a community. Besides that, an Item can have its details updated, a Transaction can change its status and a Community possesses many methods for simple yet effective management.

Lastly, limitations and constraints were added to improve model validity.

### 2. DSML Metamodel

We started by looking into how platforms like eBay work with the concept of a User creating an account, that same user can list, check and buy items and everything that revolves around that.

First with the app customization we researched what functional and nonfunctional requirements that we need for the base app, things like name, what community it represents and what sub-communities it can have, what features make sense to be optional, what is the visual theme, and what features and functionality each entity (Item, User, Community) should have. 

Then we looked at the items and concluded that they have multiple ways of being transacted, the most common is the exchange for money but platforms like eBay also allow users to auction items or both, using this as inpiration we added the possibility for an item to be auctioned, traded for another item or just given for free as choices during customization. These features can be selected freely allowing more freedom in the personalization of the platform and allowing every platform created to handle multiple use cases.

In terms of functional and nonfunctional features we thought the best optional features would be Chat, Ratings, Moderation and Item Categories which are commonly seen features on selling websites.

For this delivery we kept GUI customization were kept to a single class (ThemeConfig) which allows the user simple customization of the platform such as, the color schema(Light, Darl, Custom) to be used, the primary color and accent color of the website and mobile app, the font and finnaly the background image.

With all this considerations we arrived at the following DSML model which gives the user a flexible way to customize their platform.


### 3. GUI Metamodel

We designed the GUI metamodel in order to provide a flexible but structured basis for the visual, interactive layer of our application. The structural model defines core entities such as User, Item, Community, and Transaction, but the GUI metamodel describes how the user visually navigates and interacts with these concepts. We grounded our design in component-driven UI architectures such as MVC, React, and Angular by dividing the interface into screens, containers, and smaller reusable components, in order to achieve separation of concerns, maintainability, and consistency.

At the center lies the GUIModel class, which is responsible for structuring screens such as LoginScreen, HomeScreen, CreateListingScreen, ListingDetailScreen, AuctionScreen, ProfileScreen, SearchResultsScreen, and ChatScreen. Each screen represents an important function of the system, which is structured by the structural model. Screens are composed of ViewContainers and ViewComponents (such as buttons, forms, and images) in order to be modular and reusable. Specific components, such as Image, Menu, and Form, are used for specific marketplace functionality. Optional components use the “?” notation, in order to handle dynamic contexts; for example, showing a duration field only for an auction listing.

We also standardized component properties using enumerations, such as ScreenType, InputFieldType, and ButtonActionType, for a consistent design vocabulary.

### Model to Model 

The Model-to-Model transformation stage was designed to function as the bridge between DSML and technical requirements for code generation (B-UML). During the Model-to-Model transformation stage, we developed two distinct transformations pipelines: one for converting the DSML metamodel into Structural model, and another one for GUI model, both implemented in Python. These programs take the JSON output from the Blockly and the BESSER metamodels to generate a fully defined Domain Model.

The transformation process involves a linear pipeline where it takes a file exported by the Blockly editor and then the program reads and finds the root block to extract global configurations, feature flags and exchange types. Based on the enabled features, the program will instantiate the corresponding classes and set their attributes from the base metamodels and injecting them into a new Domain Model instance. The final output is a validated B-UML Domain Model.

The structure process main goal is to ensure that the backend database only contains tables and relationships relevant to the user's specific configuration. Some of these examples are the dynamic exchange types where the user can select "Auction" and/or "BuyNow" and the it will retrieve the classes from the metamodel and add them to the domain model. Other great example is the the setting to enable chat, which injects ChatThread and Message classes into the final domain model. Aside from adding or removing classes, it can also do attribute modifications such as enabling ratings which adds the reputation score attribute to the User class. To finish, the constraints defined in the metamodels are also injected into the final domain model to ensure validity and integrity.

The GUI transformation process builds a visual hierarchy of the application. This focuses on the screen flow and component composition. The program is able to distinguish between the core elements and dynamic elements. Similarly to the structural transformation, it can detect if any feature is enabled and will inject these components. 

### Model to Text

The Model-to-Text transformation is the final stage of the pipeline, where the abstract models and configurations are converted into actual code files that can be executed. This stage is highly important as it functions as the bridge between the high-level design and pratical implementation. The implementation was done by using 2 distinct generators: a BESSER based generator for the the structural HTML views and a lightweight configuration generator for runtime settings.

For the HTML Generation, the core of that strategy is the Gui Generator class, which extends the BESSER GeneratorInterface. Instead of generating generic code, this generator focuses on the specific DomainModel produced by the previous Model-to-Model transformation, which ensures that only the screens and components relevant to the specific community configuration are generated. The generator will then traverse through all classes in the domain model that are related to Screens. For each screen class, it will do Template Matching, which involves resolving the class name to a corresponding Jinja2 template file (example is ListingDetailsScreen mapping to listing_details.jinja2). After doing that, it will gather all relevant information, such as class object, domain model and DSML configurations into the template context, allowing the template to dynamically render the HTML structure based on the specific attributes and relationships defined in the model. To facilitate the prototyping and testing without a live and functional backend, the generator optionally loads JSON mock data corresponding to each screen, allowing the generated HTML to display realistic content during development, allowing for better visualization and user testing.

For the Runtime Configuration Generation, while the HTML structure is done by the HTML Generation process, the stylistic and funcitonal parameters are handled by a separate configuration generator. This generator functions as the bridge between the complex DSML block structure and the frontend application. The program parses the raw JSON export and extracts specific block inputs that define visual themes (colors, fonts, backgrounds) and functional features (enabled modules, transaction types). It goes through the JSON file to retrieve theme settings such as primary colors, font families, logo paths and background images. It also extracts constraints, such as business rules like maximum and minimum number of photos allowed per item. Finally, it also extracts text context such as global text variables like application name and community descriptions. 

The final output is a clean JSON configuration file that encapsulates all these settings in a structured format, which allows for frontend application to consume these settings at runtime, enabling dynamic theming and feature toggling based on user preferences defined in the DSML.
