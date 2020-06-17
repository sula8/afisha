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
        place_serialized = {
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

        places_geojson['features'].append(place_serialized)

    return places_geojson


def place_details(request, pk):
    place = get_object_or_404(Place, pk=int(pk))

    response_data = {
        "title": place.title,
        "imgs": [],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lat": place.lat,
            "lng": place.lng
        }
    }

    for img in place.images.all():
        response_data["imgs"].append(img.image.url)

    return JsonResponse(response_data, safe=False, json_dumps_params={'ensure_ascii': False})


def index(request):
    data = {
        'places_data': get_geojson()
    }
    return render(request, 'index.html', context=data)