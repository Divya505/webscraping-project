from bs4 import BeautifulSoup
import requests
import re

print("please select 1br or 2br")
wanted = input("choose from the above option: ")
url = "https://kent.craigslist.org/search/apa"
result = requests.get(url).text
soup = BeautifulSoup(result, 'lxml')
properties = soup.find_all('li', class_ = "result-row")

for property in properties:
    room = property.find("span", text=re.compile(wanted))
    if room is None:
        continue
    rent = property.find("span", text=re.compile('[£€]')).text
    room = room.text.replace(" ","")
    more_info = property.div.h3.a['href']
    print(room)
    print(rent)
    print(more_info)


