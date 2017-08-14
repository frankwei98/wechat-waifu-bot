import json
import requests
from bs4 import BeautifulSoup
from waifu import Waifu


class Search:
    def __init__(self, keyword, site_name):
        self.keyword = keyword
        self.site_name = site_name

    def get_waifu_obj_list(self):
        """
        :return: A List with Waifu Object(s) (Yes, We are now Object-oriented Programming :) )
        """
        result = []
        for _waifu in self.get_waifu_json():
            if _waifu['rating'] == 's':  # Safe filter: we only send safe photo
                result.append(Waifu(_waifu, self.site_name))  # Append Waifu Object to the list

        print('GET keyword {0} waifu list '.format(self.keyword))
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
        # you can set what site, which pages, the max limit, or even tags
        url = self.send_request()
        # Get json data by using BeautifulSoup
        soup = BeautifulSoup(url.text, "html.parser")
        # Using json to load to the data as dict
        return json.loads(str(soup))

    def send_request(self):
        # normal is yandere
        # wait for override
        return requests.get("https://yande.re/post.json", dict(pages=1, limit=15, tags=self.keyword))


class Yandere(Search):
    def __init__(self, keyword):
        super().__init__(keyword, 'Yandere')

    def send_request(self):
        return requests.get("https://yande.re/post.json", dict(pages=1, limit=15, tags=self.keyword))


class Konachan(Search):
    def __init__(self, keyword):
        super().__init__(keyword, 'Konachan')

    def send_request(self):
        return requests.get("https://konachan.com/post.json", dict(pages=1, limit=15, tags=self.keyword))


        # for _waifu in Konachan('seifuku').get_waifu_url_list():
        #     print(_waifu)
