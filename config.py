import os


class Config(object):
    ENVIRONMENT = os.environ['ENVIRONMENT']
    NOTIFY_ADMIN_URL = os.environ[os.environ['ENVIRONMENT'] + '_NOTIFY_ADMIN_URL']
    NOTIFY_API_URL = os.environ[os.environ['ENVIRONMENT'] + '_NOTIFY_API_URL']
    TEST_NUMBER = os.environ[os.environ['ENVIRONMENT'] + '_TEST_NUMBER']
    FUNCTIONAL_TEST_NAME = os.environ['ENVIRONMENT'] + '_Functional Test_'
    FUNCTIONAL_TEST_EMAIL = os.environ[os.environ['ENVIRONMENT']+'_FUNCTIONAL_TEST_EMAIL']
    FUNCTIONAL_TEST_PASSWORD = os.environ[os.environ['ENVIRONMENT'] + '_FUNCTIONAL_TEST_PASSWORD']
    FUNCTIONAL_TEST_EMAIL_PASSWORD = os.environ[os.environ['ENVIRONMENT'] + '_FUNCTIONAL_TEST_EMAIL_PASSWORD']
    EMAIL_NOTIFICATION_LABEL = 'notify'
    REGISTRATION_EMAIL_LABEL = 'registration'
    INVITATION_EMAIL_LABEL = 'invite'
    EMAIL_TRIES = 36
    EMAIL_DELAY = 5
    FUNCTIONAL_TEST_SERVICE_NAME = os.environ['ENVIRONMENT'] + '_Functional Test Service_'
    NOTIFY_SERVICE_ID = os.environ[os.environ['ENVIRONMENT'] + '_NOTIFY_SERVICE_ID']
    NOTIFY_SERVICE_API_KEY = os.environ[os.environ['ENVIRONMENT'] + '_NOTIFY_SERVICE_API_KEY']


class StagingConfig(Config):
    FUNCTIONAL_TEST_SERVICE_NAME = 'Staging FunctionalTest'
    SMS_TEMPLATE_ID = os.environ.get('staging_SMS_TEMPLATE_ID')
    EMAIL_TEMPLATE_ID = os.environ.get('staging_EMAIL_TEMPLATE_ID')
    SERVICE_ID = os.environ.get('staging_SERVICE_ID')
    SERVICE_API_KEY = os.environ.get('staging_API_KEY')


class LiveConfig(Config):
    FUNCTIONAL_TEST_SERVICE_NAME = 'Live FunctionalTest'
    SMS_TEMPLATE_ID = os.environ.get('live_SMS_TEMPLATE_ID')
    EMAIL_TEMPLATE_ID = os.environ.get('live_EMAIL_TEMPLATE_ID')
    SERVICE_ID = os.environ.get('live_SERVICE_ID')
    SERVICE_API_KEY = os.environ.get('live_API_KEY')
