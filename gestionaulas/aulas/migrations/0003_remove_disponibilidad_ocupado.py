# Generated by Django 2.2 on 2019-04-30 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aulas', '0002_auto_20190430_2230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disponibilidad',
            name='ocupado',
        ),
    ]
