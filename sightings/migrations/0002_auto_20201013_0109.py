# Generated by Django 3.1.2 on 2020-10-13 01:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='squirrel',
            old_name='longitude',
            new_name='longitude',
        ),
    ]
