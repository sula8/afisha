# Generated by Django 3.0.7 on 2020-06-15 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_auto_20200615_1436'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='placeimage',
            options={'verbose_name': 'Изображение места', 'verbose_name_plural': 'Изображения места'},
        ),
        migrations.RemoveField(
            model_name='placeimage',
            name='sort',
        ),
    ]