# Generated by Django 2.2.3 on 2019-10-15 17:14

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0002_auto_20191007_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comunicacion',
            name='descripcion',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
