from django.apps.config import AppConfig


class PaymentConfig(AppConfig):
    name = 'users'
    verbose_name = 'users'

    def ready(self):
        import users.signals.handlers
