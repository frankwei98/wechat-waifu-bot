import yandere_search as search

from wxpy import *

# init bot
bot = Bot(cache_path=True)  # Enable cache_path to improve test efficiency


@bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
    # Accept friend request by keyword
    if 'I need waifu' in msg.text.lower():
        # Accept (msg.card is the user object)
        new_friend = bot.accept_friend(msg.card)
        new_friend.send('你现在可以通过 「关键词.waifu」 来找老婆的照片啦')


# Not only group chat
# @bot.register(chats=Group, msg_types=TEXT)
@bot.register(msg_types=TEXT)
def reply(msg):
    if msg.text[-6:] in '.waifu':
        # We can now reply a single yande.re pic url
        keyword = msg.text[:-6]
        url = search.get_waifu_url_list(keyword).pop(0)
        # write a mod that get img file and send the img location string

        return url


# Keep running
embed()
