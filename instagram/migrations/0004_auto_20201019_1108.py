# Generated by Django 3.1.2 on 2020-10-19 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20201018_1640'),
        ('instagram', '0003_auto_20201018_1547'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='Post',
        ),
    ]