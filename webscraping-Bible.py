import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

chapters = list(range(1,22))

random_chapter = random.choice(chapters)

if random_chapter < 10:
    random_chapter = '0' + str(random_chapter)
else:
    random_chapter = str(random_chapter)





webpage = 'https://ebible.org/asv/JHN' + random_chapter + '.htm'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

print(soup.title.text)

page_verses = soup.findAll("div", class_="main")
print(len(page_verses))

for v in page_verses:
    verse_list = v.text.split(".")

myverses = verse_list[:-5]

mychoice = random.choice(myverses)

print(f'Chapter: {random_chapter}')
print(mychoice)

import keys
from twilio.rest import Client
client = Client(keys.accountSID, keys.auth_token)

TWnum = '+1 507 570 5273'
myphone = "+19366356523"

textmsg = client.messages.create(to=myphone, from_=TWnum, body=mychoice)
print(textmsg.status)