import requests
from bs4 import BeautifulSoup
from db import insert_data


def parse():
    response = requests.get('https://www.bbc.co.uk/sounds/play/live:bbc_6music')
    bs = BeautifulSoup(response.content, 'html.parser')

    songs_artists = [artist.text for artist in bs.find_all('div', class_='sc-c-track__artist gel-pica-bold sc-u-truncate')]
    songs_titles = [song.text for song in bs.find_all('div', class_='sc-c-track__title gs-u-mt-- gel-brevier')]

    songs_artists.reverse()
    songs_titles.reverse()

    data = {
        'songs_artists': songs_artists,
        'songs_titles': songs_titles,
    }

    insert_data(data)
