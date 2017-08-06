"""Search Yande.re With tag
and return json"""
import json
import requests
from bs4 import BeautifulSoup


def get_random_waifu():
    return get_waifu('')


def get_waifu(keyword):
    url = requests.get("https://yande.re/post.json", {'pages': 1, 'limit': 5, 'tags': keyword})
    # Get json data by using BeautifulSoup
    soup = BeautifulSoup(url.text, "html.parser")
    # Using json to load to the data as dict
    return json.loads(str(soup))


def print_waifu(waifu_list):
    for waifu in waifu_list:
        if waifu['rating'] == 's':
            print(
                'ID is {0}, Author is {1}, JPEG Link is {2}'.format(waifu['id'], waifu['author'], waifu['jpeg_url']))


def download_waifu(file, *urls):
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            file.write(response.content)
            file.flush()
            return


search_value = input('Please input one or multiple keyword(s): (e.g thighhighs seifuku kantoku) \n')
print_waifu(get_waifu(search_value))
