from django.apps import AppConfig


class StudentinfoConfig(AppConfig):
    name = 'studentinfo'

    def ready(self):
        import studentinfo.signals
