class Waifu:
    def __init__(self, waifu_obj):
        self.url = waifu_obj['jpeg_url']
        self.id = waifu_obj['id']

    def print_waifu(self):
        print('ID is {0}, JPEG Link is {1}'
              .format(self.id, self.url)
              )
