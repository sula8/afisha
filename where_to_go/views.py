from django.shortcuts import render

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
                    "detailsUrl": "{% static 'places/moscow_legends.json' %}"
                }
            }

        places_geojson['features'].append(place_serialized)

    return places_geojson


def index(request):
    data = {
        'places_data': get_geojson()
    }
    return render(request, 'index.html', context=data)
