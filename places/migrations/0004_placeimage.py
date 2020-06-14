# Generated by Django 3.0.7 on 2020-06-14 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_remove_place_imgs'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.Place', verbose_name='Изображение места')),
            ],
        ),
    ]