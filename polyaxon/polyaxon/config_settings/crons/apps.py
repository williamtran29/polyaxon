from polyaxon.config_settings.apps import *
from polyaxon.config_settings.auditor_apps import AUDITOR_APPS

PROJECT_APPS = AUDITOR_APPS + (
    'crons.apps.CronsConfig',
)

INSTALLED_APPS += PROJECT_APPS