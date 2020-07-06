import json
import requests

from django.core.management.base import BaseCommand

from bs4 import BeautifulSoup
from io import BytesIO

from places.models import Place, PlaceImage


def get_json_urls(url):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'lxml')
    selector = "main table.files td.content a.js-navigation-open"

    links = soup.select(selector)

    raw_git_url = 'https://raw.githubusercontent.com'
    urls = []
    for link in links:
        empty_var, git_acc, repo, some_var, branch, folder, file = link['href'].split('/')
        url = f'{raw_git_url}/{git_acc}/{repo}/{branch}/{folder}/{file}'
        urls.append(url)

    return urls


def add_place(url):
    response = requests.get(url)
    json_data = json.loads(response.text)

    place, ans = Place.objects.get_or_create(
        title=json_data.get('title'),
        short_description=json_data.get('short_description'),
        long_description=json_data.get('long_description'),
        lng=json_data.get('coordinates').get('lng'),
        lat=json_data.get('coordinates').get('lat')
    )

    if ans:
        img_urls = json_data.get('imgs')
        for img_url in img_urls:
            add_image(place, img_url)


def add_image(place, img_url):
    img_request = requests.get(img_url)
    img_content = BytesIO(img_request.content)
    img_name = img_url.split('/')[-1]

    place_image = PlaceImage.objects.create(place=place)
    place_image.image.save(img_name, img_content, save=True)


class Command(BaseCommand):
    help = 'Provide link'

    def add_arguments(self, parser):
        parser.add_argument('parsed_url', type=str)

    def handle(self, *args, **options):
        parsed_url = options['parsed_url']

        if '.json' in parsed_url:

            if ('github.com' in parsed_url) and ('raw' not in parsed_url):
                raw_git_url = 'https://raw.githubusercontent.com'
                protocol, empty_var, domain, git_acc, repo, some_var, branch, folder, file = parsed_url.split('/')
                parsed_url = f'{raw_git_url}/{git_acc}/{repo}/{branch}/{folder}/{file}'

            add_place(parsed_url)

        else:
            for url in get_json_urls(parsed_url):
                add_place(url)

        self.stdout.write(self.style.SUCCESS('Successfully added!'))
