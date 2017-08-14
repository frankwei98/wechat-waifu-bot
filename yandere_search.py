# @Deprecated
# THIS IS A DEPRECATED SEARCH FILE
# MAYBE DELETED SOME DAY
#
#
# """
# Search Yande.re With tag
# and return json
# """
# import json
# import requests
# from waifu import Waifu
# from bs4 import BeautifulSoup
#
#
# def get_waifu_obj_list(keyword):
#     """
#     :param keyword: a single or multiple keywords
#     :return: A List with Waifu Object(s) (Yes, We are now Object-oriented Programming :) )
#     """
#     result = []
#     for _waifu in get_waifu_json(keyword):
#         if _waifu['rating'] == 's':  # Safe filter: we only send safe photo
#             result.append(Waifu(_waifu, 'yandere'))  # Append Waifu Object to the list
#
#     print('GET KEYWORD {0} waifu list '.format(keyword))
#     return result
#
#
# def get_waifu_url_list(keyword):
#     """
#
#     :param keyword: a single or multiple keywords
#     :return: A list with jpeg url(s)
#     """
#     result = []
#     for _waifu in get_waifu_json(keyword):
#         if _waifu['rating'] == 's':  # Safe filter: we only send safe photo
#             result.append(_waifu['jpeg_url'])
#
#     return result
#
#
# def get_waifu_json(keyword):
#     """
#     :param keyword: a single or multiple keywords for search
#     :return: A Dict with deserialized json data
#     """
#     # you can set what site, which pages, the max limit, or even tags
#     url = requests.get("https://yande.re/post.json", dict(pages=1, limit=15, tags=keyword))
#     # Get json data by using BeautifulSoup
#     soup = BeautifulSoup(url.text, "html.parser")
#     # Using json to load to the data as dict
#     return json.loads(str(soup))
#
# # only for test
# # search_value = input('Please input one or multiple keyword(s): (e.g thighhighs seifuku kantoku) \n')
# # search_value = 'thighhighs seifuku kantoku'
# # #
# # _waifu_obj = get_waifu_obj_list(search_value).pop(0)
# # _waifu_obj.download_picture()
