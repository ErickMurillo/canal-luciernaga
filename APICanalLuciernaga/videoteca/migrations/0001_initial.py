# Generated by Django 2.2.3 on 2019-07-22 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lugar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('fecha_nacimiento', models.DateField()),
            ],
            options={
                'verbose_name': 'Director',
                'verbose_name_plural': 'Directores',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=225)),
                ('sinopsis', models.TextField()),
                ('fecha', models.DateField()),
                ('produccion', models.CharField(max_length=255)),
                ('duracion', models.TimeField()),
                ('url', models.URLField(blank=True, null=True)),
                ('slug', models.SlugField(editable=False, max_length=250, unique=True)),
                ('categoria', models.ManyToManyField(to='videoteca.Categoria')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videoteca.Director')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lugar.Pais')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videoteca.Tipo')),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videos',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Temporada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temporada', models.IntegerField(choices=[(1, 'Temporada 1'), (2, 'Temporada 2'), (3, 'Temporada 3'), (4, 'Temporada 4'), (5, 'Temporada 5')])),
                ('info_video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videoteca.Video')),
            ],
            options={
                'verbose_name': 'Temporada',
                'verbose_name_plural': 'Temporadas',
            },
        ),
        migrations.CreateModel(
            name='Episodio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(max_length=225)),
                ('titulo', models.CharField(max_length=225)),
                ('sinopsis', models.CharField(max_length=225)),
                ('duracion', models.TimeField()),
                ('slug', models.SlugField(editable=False, max_length=250, unique=True)),
                ('temporada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episodio_temporada', to='videoteca.Temporada')),
            ],
            options={
                'verbose_name': 'Episodio',
                'verbose_name_plural': 'Episodios',
            },
        ),
    ]