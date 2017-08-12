import requests


class Waifu:
    def __init__(self, waifu_obj):
        self.url = waifu_obj['jpeg_url']
        self.id = waifu_obj['id']

    def print_waifu(self):
        print('ID is {0}, JPEG Link is {1}'
              .format(self.id, self.url)
              )

    def download_picture(self):
        resp = requests.get(self.url)
        if resp.status_code == 200:
            picture_location = './cache/{0}.jpg'.format(self.id)
            f = open(picture_location.format(self.id), 'wb')
            f.write(resp.content)
            f.close()
            return picture_location
