from django.db import models
from django.utils import timezone


class Form(models.Model):
    datetime = models.DateTimeField('datetime', default=timezone.now)

    def __str__(self):
        return f'{self.pk} - {self.datetime.strftime("%Y-%m-%d %H:%M")}'


class Row(models.Model):
    name = models.CharField('title', max_length=550, default='')
    description = models.CharField('description', max_length=550, default='')
    form_type = models.CharField('type', max_length=550, default='',
                                 choices=(('input', 'input'), ('textarea', 'textarea'), ('select', 'select')))
    form = models.ForeignKey(Form, related_name='rows', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.form_type}'


class Result(models.Model):
    result = models.TextField('text', null=True, blank=True)
    row = models.OneToOneField(Row, related_name='result', on_delete=models.CASCADE, blank=True, null=True)



