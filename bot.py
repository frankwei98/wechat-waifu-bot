# import yandere_search

from wxpy import *

# 初始化机器人，扫码登陆
bot = Bot()


# 注册好友请求类消息
@bot.register(msg_types=FRIENDS)
# 自动接受验证信息中包含 'waifu' 的好友请求
def auto_accept_friends(msg):
    # 判断好友请求中的验证文本
    if 'I need waifu' in msg.text.lower():
        # 接受好友 (msg.card 为该请求的用户对象)
        new_friend = bot.accept_friend(msg.card)
        new_friend.send('你现在可以通过发送消息来找老婆的照片啦')


# Not only group chat
# @bot.register(chats=Group, msg_types=TEXT)
@bot.register(msg_types=TEXT)
def reply(msg):
    if msg.text[-6:] in '.waifu':
        return 'Your waifu {0} is shit'.format(msg.text[:-6])


# 堵塞线程
embed()
