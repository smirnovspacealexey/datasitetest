# Generated by Django 4.0.4 on 2022-05-24 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.TextField(blank=True, null=True, verbose_name='text')),
                ('row', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='result', to='data.row')),
            ],
        ),
    ]
