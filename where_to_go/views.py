from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from places.models import Place


def get_geojson():
    places_geojson = {
        "type": "FeatureCollection",
        "features": []
    }

    places = Place.objects.all()

    for place in places:
        serialized_place = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lng, place.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": reverse('place_details', args=[place.pk]),
            }
        }

        places_geojson['features'].append(serialized_place)

    return places_geojson


def place_details(request, pk):
    place = get_object_or_404(Place, pk=int(pk))

    imgs = [img.image.url for img in place.images.all()]

    response_data = {
        "title": place.title,
        "imgs": imgs,
        "description_short": place.short_description,
        "description_long": place.long_description,
        "coordinates": {
            "lat": place.lat,
            "lng": place.lng
        }
    }

    return JsonResponse(response_data, safe=False, json_dumps_params={'ensure_ascii': False})


def index(request):
    data = {
        'places_data': get_geojson()
    }
    return render(request, 'index.html', context=data)
