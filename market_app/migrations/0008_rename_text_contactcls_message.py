# Generated by Django 4.2.4 on 2023-08-25 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market_app', '0007_contactcls'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactcls',
            old_name='text',
            new_name='message',
        ),
    ]
