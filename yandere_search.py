"""Search Yande.re With tag
and return json"""
import json
import requests
from bs4 import BeautifulSoup


def get_waifu_url_list(json_obj):
    result = []
    for waifu in json_obj:
        if waifu['rating'] == 's':  # Safe filter: we only send safe photo
            result.append(waifu['jpeg_url'])

    return result


def get_waifu_list(keyword):
    # you can set what pages, the max limit, or even tags
    url = requests.get("https://yande.re/post.json", dict(pages=1, limit=15, tags=keyword))
    # Get json data by using BeautifulSoup
    soup = BeautifulSoup(url.text, "html.parser")
    # Using json to load to the data as dict
    return get_waifu_url_list(json.loads(str(soup)))


def print_waifu(waifu):
    print('ID is {0}, Author is {1}, JPEG Link is {2}'
          .format(waifu['id'], waifu['author'], waifu['jpeg_url'])
          )

# only for debug
# search_value = input('Please input one or multiple keyword(s): (e.g thighhighs seifuku kantoku) \n')
# search_value = 'thighhighs seifuku kantoku'
#
# print(get_waifu_list(search_value).pop(0))
