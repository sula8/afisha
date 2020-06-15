from django.contrib import admin

from places.models import Place, PlaceImage


class PlaceImageInline(admin.TabularInline):
	model = PlaceImage

	readonly_fields = ['image_preview']


@admin.register(Place)
class AdminPlace(admin.ModelAdmin):
	inlines = [
		PlaceImageInline,
	]
