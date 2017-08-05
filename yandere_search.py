"""Search Yande.re With tag
and return json"""
import json
import requests
from bs4 import BeautifulSoup

keyword = input('Please input keyword: (e.g thighhighs) \n')
url = requests.get("https://yande.re/post.json", {'limit': 5, 'tags': keyword})
# Get json data by using BeautifulSoup
soup = BeautifulSoup(url.text, "html.parser")
# Using json to load to the data as dict
new_list = json.loads(str(soup))
for item in new_list:
    print('ID is {0}, Author is {1}, Picture Link is {2}'.format(item['id'], item['author'], item['file_url']))
