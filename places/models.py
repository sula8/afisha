from django.db import models
from django.utils.html import format_html

from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField("Название места", max_length=200)
    short_description = models.CharField("Короткое описание", blank=True, null=True, max_length=600)
    long_description = HTMLField("Длинное пписание", blank=True, null=True)
    lng = models.FloatField("Долгота")
    lat = models.FloatField("Широта")

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images', verbose_name="Место")
    image = models.ImageField("Изображение")
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name="Позиция")

    def __str__(self):
        return f'Изображение #{self.id} места "{self.place.title}"'

    def image_preview(self):
        return format_html('<img src="{url}" style="height:100px" />'.format(url=self.image.url))

    class Meta:
        ordering = ['my_order']
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
