# Generated by Django 3.2.2 on 2021-05-11 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20210511_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='counter',
            field=models.IntegerField(default=0),
        ),
    ]