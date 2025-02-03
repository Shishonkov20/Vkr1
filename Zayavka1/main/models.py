from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import Signal

user_registrated = Signal()


class AdvUser(AbstractUser):
    CHOOSE = (
        ('Сотрудник', 'Сотрудник'),
        ('Руководитель', 'Руководитель'),
    )
    status = models.CharField('статус', max_length=512, choices=CHOOSE, default='Сотрудник')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.username

    def get_current_user(request):
        user = request.user
        return user

    def delete(self, *args, **kwargs):
        for bb in self.additionalimage_set.all():
            bb.delete()
        super().delete(*args, **kwargs)


class TypeObr(models.Model):
    name = models.CharField('Вид обращения', max_length=255)

    class Meta:
        verbose_name = 'Вид обращения'
        verbose_name_plural = 'Виды обращений'

    def __str__(self):
        return self.name


class Client(models.Model):
    fio = models.CharField("ФИО", max_length=255)
    address = models.CharField("Адрес", max_length=255)
    phone = models.CharField("Номер телефона", max_length=30)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.fio


class TypeWork(models.Model):
    name = models.CharField('Вид работы', max_length=255)

    class Meta:
        verbose_name = 'Вид работы'
        verbose_name_plural = 'Виды работ'

    def __str__(self):
        return self.name


class Obr(models.Model):
    STATUS_CHOICE = (
        ('В работе', 'В работе'),
        ('Закрыт', 'Закрыт'),
    )
    dat = models.DateField("Дата")
    client = models.ForeignKey(Client, verbose_name='Клиент', on_delete=models.CASCADE)
    type_obr = models.ForeignKey(TypeObr, verbose_name='Вид обращения', on_delete=models.CASCADE)
    status = models.CharField('Статус', choices=STATUS_CHOICE, max_length=50)
    description = models.TextField("Описание", blank=True, null=True)

    class Meta:
        verbose_name = "Обращение"
        verbose_name_plural = "Обращения"

    def __str__(self):
        return f"обращение {self.pk}"


class WordByObr(models.Model):
    obr = models.ForeignKey(Obr, verbose_name='Обращение', on_delete=models.CASCADE)
    type_work = models.ForeignKey(TypeWork, verbose_name='Вид работы', on_delete=models.CASCADE)
    worker = models.ForeignKey(AdvUser, verbose_name='Сотрудник', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Работы по обращению"
        verbose_name_plural = "Работы по обращению"