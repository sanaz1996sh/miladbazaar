# Generated by Django 4.2.4 on 2023-08-26 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market_app', '0008_rename_text_contactcls_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='blogcls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_pic', models.CharField(max_length=50)),
                ('blog_title', models.CharField(max_length=100)),
                ('blog_dic', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='officecls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('off_name', models.CharField(max_length=50)),
                ('off_pic', models.CharField(max_length=50)),
                ('off_web', models.CharField(max_length=50)),
            ],
        ),
    ]
