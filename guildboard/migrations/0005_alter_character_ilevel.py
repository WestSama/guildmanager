# Generated by Django 4.0.1 on 2022-02-03 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guildboard', '0004_alter_character_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='iLevel',
            field=models.IntegerField(default=''),
        ),
    ]
