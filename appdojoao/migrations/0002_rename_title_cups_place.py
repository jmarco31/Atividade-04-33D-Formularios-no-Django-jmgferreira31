# Generated by Django 3.2.13 on 2023-09-20 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appdojoao', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cups',
            old_name='title',
            new_name='place',
        ),
    ]
