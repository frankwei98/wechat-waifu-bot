import json
import requests
from bs4 import BeautifulSoup
from waifu import Waifu


class Search:
    def __init__(self, keyword, sitename):
        self.keyword = keyword
        self.sitename = sitename

    def get_waifu_obj_list(self):
        """
        :return: A List with Waifu Object(s) (Yes, We are now Object-oriented Programming :) )
        """
        result = []
        for _waifu in self.get_waifu_json():
            if _waifu['rating'] == 's':  # Safe filter: we only send safe photo
                result.append(Waifu(_waifu, self.sitename))  # Append Waifu Object to the list

        print('GET waifu list of keyword {0} '.format(self.keyword))
        return result

    def get_waifu_url_list(self):
        """
        :return: A list with jpeg url(s)
        """
        result = []
        for _waifu in self.get_waifu_json():
            if _waifu['rating'] == 's':  # Safe filter: we only send safe photo
                result.append(_waifu['jpeg_url'])

        return result

    def get_waifu_json(self):
        """
        :return: A Dict with deserialized json data
        """
        url = self.define_search_api()
        # Get json data by using BeautifulSoup
        soup = BeautifulSoup(url.text, "html.parser")
        # Using json to load to the data as dict
        return json.loads(str(soup))

    def define_search_api(self):
        # normal is yandere
        # wait for override
        # you can set what site, which pages, the max limit, or even tags
        return requests.get("https://yande.re/post.json", dict(pages=1, limit=15, tags=self.keyword))


class Yandere(Search):
    def __init__(self, keyword):
        super().__init__(keyword, 'Yandere')

    def define_search_api(self):
        return requests.get("https://yande.re/post.json", dict(pages=1, limit=15, tags=self.keyword))


class Konachan(Search):
    def __init__(self, keyword):
        super().__init__(keyword, 'Konachan')

    def define_search_api(self):
        return requests.get("https://konachan.com/post.json", dict(pages=1, limit=30, tags=self.keyword))
