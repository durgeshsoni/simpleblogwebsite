# Generated by Django 3.2.3 on 2021-11-07 15:52

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='desc',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
