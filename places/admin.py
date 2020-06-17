from django.contrib import admin

from adminsortable2.admin import SortableInlineAdminMixin

from places.models import Place, PlaceImage


class PlaceImageInline(SortableInlineAdminMixin, admin.TabularInline):
	model = PlaceImage

	readonly_fields = ['image_preview']


@admin.register(Place)
class AdminPlace(admin.ModelAdmin):
	inlines = [PlaceImageInline, ]
	search_fields = ['title']
