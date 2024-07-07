import requests
from bs4 import BeautifulSoup

url = "https://www.flickr.com/search/?text=vicky+kaushal&view_all=0"
html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")
img_tags = soup.find_all("img")

for i in range(len(img_tags)):
    tag = img_tags[i]['src']
    final_url = "http://" + tag[2:]
    t = requests.get(final_url).content
    with open(f"./images/{i}.jpg", 'wb') as file:
        file.write(t)

# from random import choice
#
# emojis = ["😃", "😄", "😁", "😆", "😅", "😂", "🤣", "🥲", "🥹", "☺️", "😊", "😇", "🙂", "🙃", "😉", "😌", "😍", "🥰", "😘", "😗", "😙",
#           "😚", "😋", "😛", "😝", "😜", "🤪", "🤨", "🧐", "🤓", "😎", "🥸", "🤩", "🥳", "🙂‍↕️", "😏", "😒", "🙂‍↔️"]
#
#
#
# for i in range(50):
#     random_emoji = choice(emojis)
#     print(random_emoji)