# Generated by Django 5.1.6 on 2025-02-20 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_room_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='code',
            field=models.CharField(default='AAAAAA', max_length=8, unique=True),
        ),
    ]
