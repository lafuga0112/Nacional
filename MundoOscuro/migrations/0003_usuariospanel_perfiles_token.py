# Generated by Django 5.0.4 on 2024-04-16 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MundoOscuro', '0002_alter_perfiles_estad'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsuariosPanel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('Url_Contador', models.CharField(max_length=200)),
                ('Url_CPA', models.CharField(max_length=200)),
                ('token', models.CharField(default=0, max_length=200)),
                ('plantilla', models.CharField(default=0, max_length=200)),
                ('two_step', models.CharField(default=0, max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='perfiles',
            name='token',
            field=models.CharField(default=0, max_length=200),
        ),
    ]
