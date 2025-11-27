from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class LanguageCode(Enum):
    en = "en"
    pt = "pt"
class AuthMode(Enum):
    None = "None"
    Email = "Email"
    Google = "Google"
class ModerationMode(Enum):
    None = "None"
    ReportOnly = "ReportOnly"
    AdminApproval = "AdminApproval"
class ColorScheme(Enum):
    Light = "Light"
    Dark = "Dark"
    Custom = "Custom"
class ExchangeType(Enum):
    Free = "Free"
    Exchange = "Exchange"
    BuyNow = "BuyNow"
    Auction = "Auction"
class Types(Enum):
    int = "int"
    str = "str"
    double = "double"
    bool = "bool"


############################################
# Definition of Classes
############################################

class User_fields_list:

    def __init__(self, full_name: bool, address: bool, age: bool, nickname: bool, requireEmailVerification: bool, appcustomization_4: "AppCustomization" = None, additional_fields_2: set["Additional_fields"] = None):
        self.full_name = full_name
        self.address = address
        self.age = age
        self.nickname = nickname
        self.requireEmailVerification = requireEmailVerification
        self.appcustomization_4 = appcustomization_4
        self.additional_fields_2 = additional_fields_2 if additional_fields_2 is not None else set()
        
    @property
    def nickname(self) -> bool:
        return self.__nickname

    @nickname.setter
    def nickname(self, nickname: bool):
        self.__nickname = nickname

    @property
    def full_name(self) -> bool:
        return self.__full_name

    @full_name.setter
    def full_name(self, full_name: bool):
        self.__full_name = full_name

    @property
    def address(self) -> bool:
        return self.__address

    @address.setter
    def address(self, address: bool):
        self.__address = address

    @property
    def age(self) -> bool:
        return self.__age

    @age.setter
    def age(self, age: bool):
        self.__age = age

    @property
    def requireEmailVerification(self) -> bool:
        return self.__requireEmailVerification

    @requireEmailVerification.setter
    def requireEmailVerification(self, requireEmailVerification: bool):
        self.__requireEmailVerification = requireEmailVerification

    @property
    def appcustomization_4(self):
        return self.__appcustomization_4

    @appcustomization_4.setter
    def appcustomization_4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User_fields_list__appcustomization_4", None)
        self.__appcustomization_4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user_fields_list"):
                opp_val = getattr(old_value, "user_fields_list", None)
                if opp_val == self:
                    setattr(old_value, "user_fields_list", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user_fields_list"):
                opp_val = getattr(value, "user_fields_list", None)
                setattr(value, "user_fields_list", self)

    @property
    def additional_fields_2(self):
        return self.__additional_fields_2

    @additional_fields_2.setter
    def additional_fields_2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User_fields_list__additional_fields_2", None)
        self.__additional_fields_2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user_fields_list_1"):
                    opp_val = getattr(item, "user_fields_list_1", None)
                    
                    if opp_val == self:
                        setattr(item, "user_fields_list_1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user_fields_list_1"):
                    opp_val = getattr(item, "user_fields_list_1", None)
                    
                    setattr(item, "user_fields_list_1", self)
                    

class Features:

    def __init__(self, enableChat: bool, enableRatings: bool, enableNotifications: bool, moderationMode: ModerationMode, authMode: AuthMode, enableAnalytics: bool, enableItemCategories: bool, appcustomization_1: "AppCustomization" = None):
        self.enableChat = enableChat
        self.enableRatings = enableRatings
        self.enableNotifications = enableNotifications
        self.moderationMode = moderationMode
        self.authMode = authMode
        self.enableAnalytics = enableAnalytics
        self.enableItemCategories = enableItemCategories
        self.appcustomization_1 = appcustomization_1
        
    @property
    def enableChat(self) -> bool:
        return self.__enableChat

    @enableChat.setter
    def enableChat(self, enableChat: bool):
        self.__enableChat = enableChat

    @property
    def moderationMode(self) -> ModerationMode:
        return self.__moderationMode

    @moderationMode.setter
    def moderationMode(self, moderationMode: ModerationMode):
        self.__moderationMode = moderationMode

    @property
    def enableRatings(self) -> bool:
        return self.__enableRatings

    @enableRatings.setter
    def enableRatings(self, enableRatings: bool):
        self.__enableRatings = enableRatings

    @property
    def enableNotifications(self) -> bool:
        return self.__enableNotifications

    @enableNotifications.setter
    def enableNotifications(self, enableNotifications: bool):
        self.__enableNotifications = enableNotifications

    @property
    def enableAnalytics(self) -> bool:
        return self.__enableAnalytics

    @enableAnalytics.setter
    def enableAnalytics(self, enableAnalytics: bool):
        self.__enableAnalytics = enableAnalytics

    @property
    def enableItemCategories(self) -> bool:
        return self.__enableItemCategories

    @enableItemCategories.setter
    def enableItemCategories(self, enableItemCategories: bool):
        self.__enableItemCategories = enableItemCategories

    @property
    def authMode(self) -> AuthMode:
        return self.__authMode

    @authMode.setter
    def authMode(self, authMode: AuthMode):
        self.__authMode = authMode

    @property
    def appcustomization_1(self):
        return self.__appcustomization_1

    @appcustomization_1.setter
    def appcustomization_1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Features__appcustomization_1", None)
        self.__appcustomization_1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "features"):
                opp_val = getattr(old_value, "features", None)
                if opp_val == self:
                    setattr(old_value, "features", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "features"):
                opp_val = getattr(value, "features", None)
                setattr(value, "features", self)

class Community:

    def __init__(self, name: str, color: str, logo: Path, maxUsers: int, allowSubcommunities: bool, rules: str, defaultLanguage: LanguageCode, appcustomization_2: "AppCustomization" = None, parentCommunity: "Community" = None, subCommunities: set["Community"] = None, language: set["Language"] = None, domain: set["Domain"] = None):
        self.name = name
        self.color = color
        self.logo = logo
        self.maxUsers = maxUsers
        self.allowSubcommunities = allowSubcommunities
        self.rules = rules
        self.defaultLanguage = defaultLanguage
        self.appcustomization_2 = appcustomization_2
        self.parentCommunity = parentCommunity
        self.subCommunities = subCommunities if subCommunities is not None else set()
        self.language = language if language is not None else set()
        self.domain = domain if domain is not None else set()
        
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def maxUsers(self) -> int:
        return self.__maxUsers

    @maxUsers.setter
    def maxUsers(self, maxUsers: int):
        self.__maxUsers = maxUsers

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def defaultLanguage(self) -> LanguageCode:
        return self.__defaultLanguage

    @defaultLanguage.setter
    def defaultLanguage(self, defaultLanguage: LanguageCode):
        self.__defaultLanguage = defaultLanguage

    @property
    def rules(self) -> str:
        return self.__rules

    @rules.setter
    def rules(self, rules: str):
        self.__rules = rules

    @property
    def logo(self) -> Path:
        return self.__logo

    @logo.setter
    def logo(self, logo: Path):
        self.__logo = logo

    @property
    def allowSubcommunities(self) -> bool:
        return self.__allowSubcommunities

    @allowSubcommunities.setter
    def allowSubcommunities(self, allowSubcommunities: bool):
        self.__allowSubcommunities = allowSubcommunities

    @property
    def domain(self):
        return self.__domain

    @domain.setter
    def domain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Community__domain", None)
        self.__domain = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "community_2"):
                    opp_val = getattr(item, "community_2", None)
                    
                    if opp_val == self:
                        setattr(item, "community_2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "community_2"):
                    opp_val = getattr(item, "community_2", None)
                    
                    setattr(item, "community_2", self)
                    

    @property
    def parentCommunity(self):
        return self.__parentCommunity

    @parentCommunity.setter
    def parentCommunity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Community__parentCommunity", None)
        self.__parentCommunity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subCommunities"):
                opp_val = getattr(old_value, "subCommunities", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subCommunities"):
                opp_val = getattr(value, "subCommunities", None)
                if opp_val is None:
                    setattr(value, "subCommunities", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def subCommunities(self):
        return self.__subCommunities

    @subCommunities.setter
    def subCommunities(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Community__subCommunities", None)
        self.__subCommunities = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "parentCommunity"):
                    opp_val = getattr(item, "parentCommunity", None)
                    
                    if opp_val == self:
                        setattr(item, "parentCommunity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "parentCommunity"):
                    opp_val = getattr(item, "parentCommunity", None)
                    
                    setattr(item, "parentCommunity", self)
                    

    @property
    def appcustomization_2(self):
        return self.__appcustomization_2

    @appcustomization_2.setter
    def appcustomization_2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Community__appcustomization_2", None)
        self.__appcustomization_2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "community"):
                opp_val = getattr(old_value, "community", None)
                if opp_val == self:
                    setattr(old_value, "community", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "community"):
                opp_val = getattr(value, "community", None)
                setattr(value, "community", self)

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Community__language", None)
        self.__language = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "community_1"):
                    opp_val = getattr(item, "community_1", None)
                    
                    if opp_val == self:
                        setattr(item, "community_1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "community_1"):
                    opp_val = getattr(item, "community_1", None)
                    
                    setattr(item, "community_1", self)
                    

class ItemExchange:

    def __init__(self, name: ExchangeType, itemconfig_2: "ItemConfig" = None):
        self.name = name
        self.itemconfig_2 = itemconfig_2
        
    @property
    def name(self) -> ExchangeType:
        return self.__name

    @name.setter
    def name(self, name: ExchangeType):
        self.__name = name

    @property
    def itemconfig_2(self):
        return self.__itemconfig_2

    @itemconfig_2.setter
    def itemconfig_2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ItemExchange__itemconfig_2", None)
        self.__itemconfig_2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "itemexchange"):
                opp_val = getattr(old_value, "itemexchange", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "itemexchange"):
                opp_val = getattr(value, "itemexchange", None)
                if opp_val is None:
                    setattr(value, "itemexchange", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Language:

    def __init__(self, name: str, code: LanguageCode, community_1: "Community" = None):
        self.name = name
        self.code = code
        self.community_1 = community_1
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def code(self) -> LanguageCode:
        return self.__code

    @code.setter
    def code(self, code: LanguageCode):
        self.__code = code

    @property
    def community_1(self):
        return self.__community_1

    @community_1.setter
    def community_1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Language__community_1", None)
        self.__community_1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "language"):
                opp_val = getattr(old_value, "language", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "language"):
                opp_val = getattr(value, "language", None)
                if opp_val is None:
                    setattr(value, "language", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Domain:

    def __init__(self, name: str, community_2: "Community" = None):
        self.name = name
        self.community_2 = community_2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def community_2(self):
        return self.__community_2

    @community_2.setter
    def community_2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Domain__community_2", None)
        self.__community_2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domain"):
                opp_val = getattr(old_value, "domain", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domain"):
                opp_val = getattr(value, "domain", None)
                if opp_val is None:
                    setattr(value, "domain", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Path:

    def __init__(self, path: str):
        self.path = path
        
    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

class ThemeConfig:

    def __init__(self, colorScheme: ColorScheme, primaryColor: str, accentColor: str, fontFamily: str, logoPath: Path, backgroundImage: Path, appcustomization_3: "AppCustomization" = None):
        self.colorScheme = colorScheme
        self.primaryColor = primaryColor
        self.accentColor = accentColor
        self.fontFamily = fontFamily
        self.logoPath = logoPath
        self.backgroundImage = backgroundImage
        self.appcustomization_3 = appcustomization_3
        
    @property
    def fontFamily(self) -> str:
        return self.__fontFamily

    @fontFamily.setter
    def fontFamily(self, fontFamily: str):
        self.__fontFamily = fontFamily

    @property
    def logoPath(self) -> Path:
        return self.__logoPath

    @logoPath.setter
    def logoPath(self, logoPath: Path):
        self.__logoPath = logoPath

    @property
    def colorScheme(self) -> ColorScheme:
        return self.__colorScheme

    @colorScheme.setter
    def colorScheme(self, colorScheme: ColorScheme):
        self.__colorScheme = colorScheme

    @property
    def primaryColor(self) -> str:
        return self.__primaryColor

    @primaryColor.setter
    def primaryColor(self, primaryColor: str):
        self.__primaryColor = primaryColor

    @property
    def accentColor(self) -> str:
        return self.__accentColor

    @accentColor.setter
    def accentColor(self, accentColor: str):
        self.__accentColor = accentColor

    @property
    def backgroundImage(self) -> Path:
        return self.__backgroundImage

    @backgroundImage.setter
    def backgroundImage(self, backgroundImage: Path):
        self.__backgroundImage = backgroundImage

    @property
    def appcustomization_3(self):
        return self.__appcustomization_3

    @appcustomization_3.setter
    def appcustomization_3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ThemeConfig__appcustomization_3", None)
        self.__appcustomization_3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "themeconfig"):
                opp_val = getattr(old_value, "themeconfig", None)
                if opp_val == self:
                    setattr(old_value, "themeconfig", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "themeconfig"):
                opp_val = getattr(value, "themeconfig", None)
                setattr(value, "themeconfig", self)

class AppCustomization:

    def __init__(self, name: str, community: Community, features: Features, userConfig: User_fields_list, itemConfig: ItemConfig, communityConfig: Community_fields, theme: ThemeConfig, itemconfig: "ItemConfig" = None, features: "Features" = None, community: "Community" = None, themeconfig: "ThemeConfig" = None, user_fields_list: "User_fields_list" = None, community_fields: "Community_fields" = None):
        self.name = name
        self.community = community
        self.features = features
        self.userConfig = userConfig
        self.itemConfig = itemConfig
        self.communityConfig = communityConfig
        self.theme = theme
        self.itemconfig = itemconfig
        self.features = features
        self.community = community
        self.themeconfig = themeconfig
        self.user_fields_list = user_fields_list
        self.community_fields = community_fields
        
    @property
    def community(self) -> Community:
        return self.__community

    @community.setter
    def community(self, community: Community):
        self.__community = community

    @property
    def theme(self) -> ThemeConfig:
        return self.__theme

    @theme.setter
    def theme(self, theme: ThemeConfig):
        self.__theme = theme

    @property
    def userConfig(self) -> User_fields_list:
        return self.__userConfig

    @userConfig.setter
    def userConfig(self, userConfig: User_fields_list):
        self.__userConfig = userConfig

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def features(self) -> Features:
        return self.__features

    @features.setter
    def features(self, features: Features):
        self.__features = features

    @property
    def communityConfig(self) -> Community_fields:
        return self.__communityConfig

    @communityConfig.setter
    def communityConfig(self, communityConfig: Community_fields):
        self.__communityConfig = communityConfig

    @property
    def itemConfig(self) -> ItemConfig:
        return self.__itemConfig

    @itemConfig.setter
    def itemConfig(self, itemConfig: ItemConfig):
        self.__itemConfig = itemConfig

    @property
    def themeconfig(self):
        return self.__themeconfig

    @themeconfig.setter
    def themeconfig(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AppCustomization__themeconfig", None)
        self.__themeconfig = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appcustomization_3"):
                opp_val = getattr(old_value, "appcustomization_3", None)
                if opp_val == self:
                    setattr(old_value, "appcustomization_3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appcustomization_3"):
                opp_val = getattr(value, "appcustomization_3", None)
                setattr(value, "appcustomization_3", self)

    @property
    def itemconfig(self):
        return self.__itemconfig

    @itemconfig.setter
    def itemconfig(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AppCustomization__itemconfig", None)
        self.__itemconfig = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appcustomization"):
                opp_val = getattr(old_value, "appcustomization", None)
                if opp_val == self:
                    setattr(old_value, "appcustomization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appcustomization"):
                opp_val = getattr(value, "appcustomization", None)
                setattr(value, "appcustomization", self)

    @property
    def user_fields_list(self):
        return self.__user_fields_list

    @user_fields_list.setter
    def user_fields_list(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AppCustomization__user_fields_list", None)
        self.__user_fields_list = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appcustomization_4"):
                opp_val = getattr(old_value, "appcustomization_4", None)
                if opp_val == self:
                    setattr(old_value, "appcustomization_4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appcustomization_4"):
                opp_val = getattr(value, "appcustomization_4", None)
                setattr(value, "appcustomization_4", self)

    @property
    def features(self):
        return self.__features

    @features.setter
    def features(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AppCustomization__features", None)
        self.__features = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appcustomization_1"):
                opp_val = getattr(old_value, "appcustomization_1", None)
                if opp_val == self:
                    setattr(old_value, "appcustomization_1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appcustomization_1"):
                opp_val = getattr(value, "appcustomization_1", None)
                setattr(value, "appcustomization_1", self)

    @property
    def community_fields(self):
        return self.__community_fields

    @community_fields.setter
    def community_fields(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AppCustomization__community_fields", None)
        self.__community_fields = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appcustomization_5"):
                opp_val = getattr(old_value, "appcustomization_5", None)
                if opp_val == self:
                    setattr(old_value, "appcustomization_5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appcustomization_5"):
                opp_val = getattr(value, "appcustomization_5", None)
                setattr(value, "appcustomization_5", self)

    @property
    def community(self):
        return self.__community

    @community.setter
    def community(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AppCustomization__community", None)
        self.__community = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appcustomization_2"):
                opp_val = getattr(old_value, "appcustomization_2", None)
                if opp_val == self:
                    setattr(old_value, "appcustomization_2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appcustomization_2"):
                opp_val = getattr(value, "appcustomization_2", None)
                setattr(value, "appcustomization_2", self)

class ItemConfig:

    def __init__(self, enableBiddingTimer: bool, enableBuyNowPrice: bool, enableItemImages: bool, maxItemPhotos: int, enableItemLocation: bool, enableDeliveryOptions: bool, appcustomization: "AppCustomization" = None, itemexchange: set["ItemExchange"] = None, additional_fields_1: set["Additional_fields"] = None):
        self.enableBiddingTimer = enableBiddingTimer
        self.enableBuyNowPrice = enableBuyNowPrice
        self.enableItemImages = enableItemImages
        self.maxItemPhotos = maxItemPhotos
        self.enableItemLocation = enableItemLocation
        self.enableDeliveryOptions = enableDeliveryOptions
        self.appcustomization = appcustomization
        self.itemexchange = itemexchange if itemexchange is not None else set()
        self.additional_fields_1 = additional_fields_1 if additional_fields_1 is not None else set()
        
    @property
    def enableDeliveryOptions(self) -> bool:
        return self.__enableDeliveryOptions

    @enableDeliveryOptions.setter
    def enableDeliveryOptions(self, enableDeliveryOptions: bool):
        self.__enableDeliveryOptions = enableDeliveryOptions

    @property
    def maxItemPhotos(self) -> int:
        return self.__maxItemPhotos

    @maxItemPhotos.setter
    def maxItemPhotos(self, maxItemPhotos: int):
        self.__maxItemPhotos = maxItemPhotos

    @property
    def enableBuyNowPrice(self) -> bool:
        return self.__enableBuyNowPrice

    @enableBuyNowPrice.setter
    def enableBuyNowPrice(self, enableBuyNowPrice: bool):
        self.__enableBuyNowPrice = enableBuyNowPrice

    @property
    def enableItemImages(self) -> bool:
        return self.__enableItemImages

    @enableItemImages.setter
    def enableItemImages(self, enableItemImages: bool):
        self.__enableItemImages = enableItemImages

    @property
    def enableItemLocation(self) -> bool:
        return self.__enableItemLocation

    @enableItemLocation.setter
    def enableItemLocation(self, enableItemLocation: bool):
        self.__enableItemLocation = enableItemLocation

    @property
    def enableBiddingTimer(self) -> bool:
        return self.__enableBiddingTimer

    @enableBiddingTimer.setter
    def enableBiddingTimer(self, enableBiddingTimer: bool):
        self.__enableBiddingTimer = enableBiddingTimer

    @property
    def itemexchange(self):
        return self.__itemexchange

    @itemexchange.setter
    def itemexchange(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ItemConfig__itemexchange", None)
        self.__itemexchange = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "itemconfig_2"):
                    opp_val = getattr(item, "itemconfig_2", None)
                    
                    if opp_val == self:
                        setattr(item, "itemconfig_2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "itemconfig_2"):
                    opp_val = getattr(item, "itemconfig_2", None)
                    
                    setattr(item, "itemconfig_2", self)
                    

    @property
    def additional_fields_1(self):
        return self.__additional_fields_1

    @additional_fields_1.setter
    def additional_fields_1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ItemConfig__additional_fields_1", None)
        self.__additional_fields_1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "itemconfig_1"):
                    opp_val = getattr(item, "itemconfig_1", None)
                    
                    if opp_val == self:
                        setattr(item, "itemconfig_1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "itemconfig_1"):
                    opp_val = getattr(item, "itemconfig_1", None)
                    
                    setattr(item, "itemconfig_1", self)
                    

    @property
    def appcustomization(self):
        return self.__appcustomization

    @appcustomization.setter
    def appcustomization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ItemConfig__appcustomization", None)
        self.__appcustomization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "itemconfig"):
                opp_val = getattr(old_value, "itemconfig", None)
                if opp_val == self:
                    setattr(old_value, "itemconfig", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "itemconfig"):
                opp_val = getattr(value, "itemconfig", None)
                setattr(value, "itemconfig", self)

class Community_fields:

    def __init__(self, locale: bool, description: bool, appcustomization_5: "AppCustomization" = None, additional_fields: set["Additional_fields"] = None):
        self.locale = locale
        self.description = description
        self.appcustomization_5 = appcustomization_5
        self.additional_fields = additional_fields if additional_fields is not None else set()
        
    @property
    def description(self) -> bool:
        return self.__description

    @description.setter
    def description(self, description: bool):
        self.__description = description

    @property
    def locale(self) -> bool:
        return self.__locale

    @locale.setter
    def locale(self, locale: bool):
        self.__locale = locale

    @property
    def appcustomization_5(self):
        return self.__appcustomization_5

    @appcustomization_5.setter
    def appcustomization_5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Community_fields__appcustomization_5", None)
        self.__appcustomization_5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "community_fields"):
                opp_val = getattr(old_value, "community_fields", None)
                if opp_val == self:
                    setattr(old_value, "community_fields", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "community_fields"):
                opp_val = getattr(value, "community_fields", None)
                setattr(value, "community_fields", self)

    @property
    def additional_fields(self):
        return self.__additional_fields

    @additional_fields.setter
    def additional_fields(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Community_fields__additional_fields", None)
        self.__additional_fields = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "community_fields_1"):
                    opp_val = getattr(item, "community_fields_1", None)
                    
                    if opp_val == self:
                        setattr(item, "community_fields_1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "community_fields_1"):
                    opp_val = getattr(item, "community_fields_1", None)
                    
                    setattr(item, "community_fields_1", self)
                    

class Additional_fields:

    def __init__(self, type: Types, enabled: bool, mandatory: bool, name: str, community_fields_1: "Community_fields" = None, itemconfig_1: "ItemConfig" = None, user_fields_list_1: "User_fields_list" = None):
        self.type = type
        self.enabled = enabled
        self.mandatory = mandatory
        self.name = name
        self.community_fields_1 = community_fields_1
        self.itemconfig_1 = itemconfig_1
        self.user_fields_list_1 = user_fields_list_1
        
    @property
    def enabled(self) -> bool:
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled: bool):
        self.__enabled = enabled

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mandatory(self) -> bool:
        return self.__mandatory

    @mandatory.setter
    def mandatory(self, mandatory: bool):
        self.__mandatory = mandatory

    @property
    def type(self) -> Types:
        return self.__type

    @type.setter
    def type(self, type: Types):
        self.__type = type

    @property
    def user_fields_list_1(self):
        return self.__user_fields_list_1

    @user_fields_list_1.setter
    def user_fields_list_1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Additional_fields__user_fields_list_1", None)
        self.__user_fields_list_1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "additional_fields_2"):
                opp_val = getattr(old_value, "additional_fields_2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "additional_fields_2"):
                opp_val = getattr(value, "additional_fields_2", None)
                if opp_val is None:
                    setattr(value, "additional_fields_2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def community_fields_1(self):
        return self.__community_fields_1

    @community_fields_1.setter
    def community_fields_1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Additional_fields__community_fields_1", None)
        self.__community_fields_1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "additional_fields"):
                opp_val = getattr(old_value, "additional_fields", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "additional_fields"):
                opp_val = getattr(value, "additional_fields", None)
                if opp_val is None:
                    setattr(value, "additional_fields", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def itemconfig_1(self):
        return self.__itemconfig_1

    @itemconfig_1.setter
    def itemconfig_1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Additional_fields__itemconfig_1", None)
        self.__itemconfig_1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "additional_fields_1"):
                opp_val = getattr(old_value, "additional_fields_1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "additional_fields_1"):
                opp_val = getattr(value, "additional_fields_1", None)
                if opp_val is None:
                    setattr(value, "additional_fields_1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
