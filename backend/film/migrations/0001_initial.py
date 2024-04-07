# Generated by Django 4.0 on 2024-04-07 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Nome')),
                ('director_name', models.CharField(max_length=120, verbose_name='Diretor')),
                ('duration', models.IntegerField(verbose_name='Duração (Min)')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('film_type', models.CharField(choices=[('horror', 'Terror'), ('action', 'Ação'), ('drama', 'Drama'), ('comedy', 'Comédia'), ('romance', 'Romance'), ('fantasy', 'Fantasy'), ('science_fiction', 'Ficção Científica')], max_length=80)),
            ],
        ),
    ]
