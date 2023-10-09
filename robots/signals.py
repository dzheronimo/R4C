from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver


from .models import Robot
from orders.models import WaitingList


@receiver(post_save, sender=Robot)
def check_waiting_list_and_send_notification(
        sender, instance, created, **kwargs):
    if created:
        print('Сигнал получен ...')
        waiting_list = WaitingList.objects.filter(
            order__robot_serial=instance.serial)
        if waiting_list.exists():
            print('Запись в БД создана ..')
            model = instance.model
            version = instance.version
            send_mail(
                'Ваш заказ в наличии!',
                (f'Добрый день!\n'
                 f'Недавно вы интересовались нашим '
                 f'роботом модели {model}, версии {version}.\n'
                 f'Этот робот теперь в наличии. '
                 f'Если вам подходит этот вариант - '
                 f'пожалуйста, свяжитесь с нами'),
                'sale@robots.org',
                ['consumer@yandex.ru'],
                fail_silently=False
            )
            print('Письмо отправлено')
