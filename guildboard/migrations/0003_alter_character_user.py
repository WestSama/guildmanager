# Generated by Django 4.0.1 on 2022-02-03 18:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('guildboard', '0002_remove_character_classname_character_classe_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
