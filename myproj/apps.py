from django.apps import AppConfig


class BackendConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myproj'

    def ready(self):
        """
        Импортируем сигналы
        """