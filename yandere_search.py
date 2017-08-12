"""Search Yande.re With tag
and return json"""
import json
import requests
import waifu as class_waifu
from bs4 import BeautifulSoup


def get_waifu_obj_list(keyword) -> class_waifu:
    """

    :param keyword: a single or multiple keywords
    :return: A Waifu Object (Yes, We are now Object-oriented Programming)
    """
    result = []
    for _waifu in get_waifu_json(keyword):
        if _waifu['rating'] == 's':  # Safe filter: we only send safe photo
            result.append(class_waifu.Waifu(_waifu))

    return result


def get_waifu_url_list(keyword):
    """

    :param keyword: a single or multiple keywords
    :return: A list with jpeg url
    """
    result = []
    for _waifu in get_waifu_json(keyword):
        if _waifu['rating'] == 's':  # Safe filter: we only send safe photo
            result.append(_waifu['jpeg_url'])

    return result


def get_waifu_json(keyword):
    # you can set what site, which pages, the max limit, or even tags
    url = requests.get("https://yande.re/post.json", dict(pages=1, limit=15, tags=keyword))
    # Get json data by using BeautifulSoup
    soup = BeautifulSoup(url.text, "html.parser")
    # Using json to load to the data as dict
    return json.loads(str(soup))

# only for test
# search_value = input('Please input one or multiple keyword(s): (e.g thighhighs seifuku kantoku) \n')
# search_value = 'thighhighs seifuku kantoku'
# #
# _waifu_obj = get_waifu_obj_list(search_value).pop(0)
# _waifu_obj.download_picture()
