from django.apps import AppConfig as BaseAppConfig
from importlib import import_module


class AppConfig(BaseAppConfig):

    name = "{{ project_name }}"

    def ready(self):
        import_module("{{ project_name }}.receivers")
