import os

import requests


class Waifu:
    def __init__(self, waifu_obj, site):
        self.url = waifu_obj['jpeg_url']
        self.id = waifu_obj['id']
        self.site = site

    def print_waifu(self):
        print('ID is {0}, JPEG Link is {1}'
              .format(self.id, self.url)
              )

    def download_picture(self):
        self.print_waifu()
        picture_location = './cache/{0}-{1}.jpg'.format(self.site, self.id)

        if not os.path.isfile(picture_location):
            print('File {0} not exist'.format(picture_location))
            # if file not exist then download photo
            resp = requests.get(self.url)
            if resp.status_code == 200:
                f = open(picture_location.format(self.id), 'wb')
                f.write(resp.content)
                f.close()

        return picture_location
