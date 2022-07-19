import os

from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from configs.celery import app

from core.enums.template_enum import TemplateEnum
from core.services.jwt_service import ActivateToken, JwtService, RecoveryToken

UserModel = get_user_model()


class EmailService:
    @staticmethod
    @app.task
    def _send_email(to: str, template_name: str, context: dict, subject='') -> None:
        template = get_template(template_name)
        html_content = template.render(context)
        msg = EmailMultiAlternatives(subject, from_email=os.environ.get('EMAIL_HOST_USER'), to=[to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    @classmethod
    def register_email(cls, user):
        token = JwtService.create_token(user, ActivateToken)
        url = f'{os.environ.get("FRONTEND_URL")}/activate/{token}'
        cls._send_email.delay(user.email, TemplateEnum.REGISTER.value, {'name': user.profile.name, 'link': url},
                              'Register')

    @classmethod
    def recovery_email(cls, user):
        token = JwtService.create_token(user, RecoveryToken)
        url = f'{os.environ.get("FRONTEND_URL")}/recovery/{token}'
        cls._send_email.delay(user.email, TemplateEnum.RECOVERY.value, {'name': user.profile.name, 'link': url},
                              'Recovery')

    @staticmethod
    @app.task
    def spam():
        for user in UserModel.objects.all():
            EmailService._send_email(user.email, TemplateEnum.SPAM.value, {}, 'SPAM')
