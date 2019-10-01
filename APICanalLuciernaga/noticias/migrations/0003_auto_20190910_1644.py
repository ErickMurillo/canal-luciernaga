# Generated by Django 2.2.3 on 2019-09-10 16:44

from django.db import migrations
import taggit_autosuggest.managers


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0002_auto_20190827_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comunicacion',
            name='tags',
            field=taggit_autosuggest.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]