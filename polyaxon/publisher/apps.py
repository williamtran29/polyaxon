from django.apps import AppConfig


class PublisherConfig(AppConfig):
    name = 'publisher'
    verbose_name = 'Publisher'

    def ready(self):
        from polyaxon.utils import config

        config.setup_publisher_service()
