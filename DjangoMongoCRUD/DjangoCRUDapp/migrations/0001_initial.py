# Generated by Django 3.0.5 on 2021-04-14 15:17

import DjangoCRUDapp.models
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=30)),
                ('subgenero', models.CharField(blank=True, max_length=20)),
                ('decada', models.CharField(blank=True, max_length=20)),
                ('canciones', djongo.models.fields.ArrayField(model_container=DjangoCRUDapp.models.Cancion, model_form_class=DjangoCRUDapp.models.CancionForm)),
            ],
        ),
    ]
