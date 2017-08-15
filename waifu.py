import os

import requests


class Waifu:
    def __init__(self, waifu_obj, site):
        # konachan's url starts with '//' cause problem for download_picture function
        if waifu_obj['jpeg_url'].startswith('//'):
            self.url = 'http:' + waifu_obj['jpeg_url']
        else:
            self.url = waifu_obj['jpeg_url']
        self.id = waifu_obj['id']
        self.site = site

    def print_waifu(self):
        print('ID is {0}, JPEG Link is {1}'
              .format(self.id, self.url)
              )

    def download_picture(self):
        # print waifu info
        self.print_waifu()
        # define the format rule
        file_location = './cache/{0}-{1}.jpg'.format(self.site, self.id)

        # if file not exist then download photo
        if not os.path.isfile(file_location):
            print('File {0} not exist'.format(file_location))
            resp = requests.get(self.url)
            if resp.status_code == 200:
                f = open(file_location, 'wb')
                f.write(resp.content)
                f.close()

        return file_location
