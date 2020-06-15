from django.db import models
from django.utils.html import format_html


class Place(models.Model):
	title = models.CharField("Название", max_length=200)
	description_short = models.CharField("Короткое описание", max_length=600)
	description_long = models.TextField("Описание")
	lng = models.FloatField("Долгота")
	lat = models.FloatField("Широта")

	def __str__(self):
		return f'{self.title}'

	class Meta:
		verbose_name = 'Место'
		verbose_name_plural = 'Места'


class PlaceImage(models.Model):
	place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images', verbose_name="Изображение места")
	image = models.ImageField("Изображение")
	sorting = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name="Позиция")

	def __str__(self):
		return f'Изображение #{self.id} места "{self.place.title}"'

	def image_preview(self):
		return format_html('<img src="{url}" style="height:100px" />'.format(url=self.image.url))

	class Meta:
		verbose_name = 'Изображение места'
		verbose_name_plural = 'Изображения места'
		ordering = ['sorting']


