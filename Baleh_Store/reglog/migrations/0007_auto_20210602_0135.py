# Generated by Django 2.2.4 on 2021-06-01 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reglog', '0006_auto_20210531_1038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.DeleteModel(
            name='thought',
        ),
    ]