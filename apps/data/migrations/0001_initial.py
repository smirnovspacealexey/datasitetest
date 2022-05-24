# Generated by Django 4.0.4 on 2022-05-23 14:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='datetime')),
            ],
        ),
        migrations.CreateModel(
            name='Row',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=550, verbose_name='title')),
                ('description', models.CharField(default='', max_length=550, verbose_name='description')),
                ('form_type', models.CharField(choices=[('input', 'input'), ('textarea', 'textarea'), ('select', 'select')], default='', max_length=550, verbose_name='type')),
                ('form', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rows', to='data.form')),
            ],
        ),
    ]
