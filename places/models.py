from django.db import models


class Place(models.Model):
	title = models.CharField("Название", max_length=200)
	description_short = models.CharField("Короткое описание", max_length=600)
	description_long = models.TextField("Описание")
	lng = models.FloatField("Долгота")
	lat = models.FloatField("Широта")

	def __str__(self):
		return f'{self.title}'


class PlaceImage(models.Model):
	place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images', verbose_name="Изображение места")
	image = models.ImageField("Изображение")

	def __str__(self):
		return f'Изображение #{self.id} места "{self.place.title}"'

	def sort_imgs(self):
		return