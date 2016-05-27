from selenium.webdriver.common.by import By


class CommonPageLocators(object):
    NAME_INPUT = (By.NAME, 'name')
    EMAIL_INPUT = (By.NAME, 'email_address')
    PASSWORD_INPUT = (By.NAME, 'password')
    CONTINUE_BUTTON = (By.CLASS_NAME, 'button')
    H1 = (By.TAG_NAME, 'H1')


class MainPageLocators(object):
    SETUP_ACCOUNT_BUTTON = (By.CLASS_NAME, 'button')


class SignUpPageLocators(object):
    MOBILE_INPUT = (By.NAME, 'mobile_number')


class TwoFactorPageLocators(object):
    SMS_INPUT = (By.NAME, 'sms_code')


class AddServicePageLocators(object):
    SERVICE_INPUT = (By.NAME, 'name')
    ADD_SERVICE_BUTTON = (By.CLASS_NAME, 'button')


class DashboardPageLocators(object):
    H2 = (By.CLASS_NAME, 'navigation-service-name')
    SMS_TEMPLATES_LINK = (By.LINK_TEXT, 'Text message templates')
    EMAIL_TEMPLATES_LINK = (By.LINK_TEXT, 'Email templates')
    TEAM_MEMBERS_LINK = (By.LINK_TEXT, 'Team members')
    API_KEYS_LINK = (By.LINK_TEXT, 'API keys')


class NavigationLocators(object):
    SIGN_OUT_LINK = (By.LINK_TEXT, 'Sign out')


class TemplatePageLocators(object):
    SEND_TEST_MESSAGES_LINK = (By.LINK_TEXT, 'Send text messages')
    SEND_EMAIL_LINK = (By.LINK_TEXT, 'Send emails')
    NEW_TEMPLATE_LINK = (By.LINK_TEXT, 'Add new template')
    EDIT_TEMPLATE_LINK = (By.LINK_TEXT, 'Edit template')


class EditTemplatePageLocators(object):
    TEMPLATE_SUBJECT_INPUT = (By.NAME, 'subject')
    TEMPLATE_CONTENT_INPUT = (By.NAME, 'template_content')
    SAVE_BUTTON = (By.CLASS_NAME, 'button')


class UploadCsvLocators(object):
    FILE_INPUT = (By.ID, 'file')
    SEND_BUTTON = (By.CLASS_NAME, 'button')


class TeamMembersPageLocators(object):
    H1 = (By.TAG_NAME, 'h1')
    INVITE_TEAM_MEMBER_BUTTON = (By.CLASS_NAME, 'button')


class InviteUserPageLocators(object):
    SEND_MESSAGES_CHECKBOX = (By.NAME, 'send_messages')
    MANAGE_SERVICES_CHECKBOX = (By.NAME, 'manage_services')
    MANAGE_API_KEYS_CHECKBOX = (By.NAME, 'manage_api_keys')
    SEND_INVITATION_BUTTON = (By.CLASS_NAME, 'button')


class ApiKeysPageLocators(object):
    KEY_NAME_INPUT = (By.NAME, 'key_name')
    CREATE_KEY_LINK = (By.LINK_TEXT, 'Create an API key')
    API_KEY_ELEMENT = (By.CLASS_NAME, 'api-key-key')
