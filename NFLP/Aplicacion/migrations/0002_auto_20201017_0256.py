# Generated by Django 3.1.1 on 2020-10-17 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='equipos',
            options={'verbose_name_plural': 'Equipos'},
        ),
        migrations.RemoveField(
            model_name='jugadores',
            name='id',
        ),
        migrations.AlterField(
            model_name='jugadores',
            name='Numero_Jugador',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]