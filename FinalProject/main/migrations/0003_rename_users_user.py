# Generated by Django 3.2.25 on 2024-10-29 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_users'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='users',
            new_name='User',
        ),
    ]