from random import randint

from wxpy import *

# import search engine
from search import *

# init bot
bot = Bot(cache_path=True)  # Enable cache_path to improve test efficiency


@bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
    # Accept friend request by keyword
    if 'I need waifu' in msg.text.lower():
        # Accept (msg.card is the user object)
        new_friend = bot.accept_friend(msg.card)
        new_friend.send('你现在可以通过 "关键词.waifu" 来找动漫人物照片啦')


# Not only group chat
# @bot.register(chats=Group, msg_types=TEXT)
@bot.register(msg_types=TEXT)
def reply(msg):
    print('{0} said "{1}"'.format(msg.sender, msg.text))
    if msg.text[-6:] in '.waifu':
        print('{0} triggered get waifu photo function'.format(msg.sender))

        # We can now reply a single yande.re pic url
        keyword = msg.text[:-6]
        # we now support yande.re and konachan
        waifu_list = Yandere(keyword).get_waifu_obj_list()
        # waifu_list = Konachan(keyword).get_waifu_obj_list()

        # Random Photo with random integer. RandInt range from 0 to the length of the list
        _rand = randint(0, len(waifu_list))
        _waifu = waifu_list.pop(_rand)

        msg.reply_image(_waifu.download_picture())
        print('Send waifu image successful')
        # write a mod that get img file and send the img location string here
        # return '@img@{0}'.format(url.download_picture())


# Keep running
embed()
