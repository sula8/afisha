from django.contrib import admin

from places.models import Place, PlaceImage


class AdminPlaceImage(admin.ModelAdmin):
	raw_id_fields = ['place']


admin.site.register(Place)
admin.site.register(PlaceImage, AdminPlaceImage)
