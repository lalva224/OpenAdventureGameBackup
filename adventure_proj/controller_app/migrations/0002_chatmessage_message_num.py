# Generated by Django 5.0.3 on 2024-04-08 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controller_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='message_num',
            field=models.IntegerField(default=0),
        ),
    ]