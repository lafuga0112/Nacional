# Generated by Django 5.0.4 on 2024-04-16 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MundoOscuro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfiles',
            name='estad',
            field=models.CharField(default=0, max_length=200),
        ),
    ]
