# Generated by Django 3.2.13 on 2023-09-21 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appdojoao', '0002_rename_title_cups_place'),
    ]

    operations = [
        migrations.RenameField(
            model_name='individual_awards',
            old_name='title',
            new_name='year',
        ),
    ]