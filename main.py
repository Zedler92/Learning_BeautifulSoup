import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
response.raise_for_status()
content = response.text

soup = BeautifulSoup(content, "html.parser")
title_list = soup.find_all(name="h3", class_="title")
d = []
for item in title_list:
    title = item.getText()
    if ")" in title:
        title = title.split(")")
    elif ":" in title:
        title = title.split(":")
    if title[1] == " Spirited Away":
        title[0] = "80"
    title = [int(title[0]), title[1]]
    d.append(title)

d.sort(key=lambda tup: tup[0])
with open("list_of_songs.txt", "w", encoding="utf-8") as list_songs:
    for num in range(0, len(d)):
        list_songs.write(f"{num+1}) {d[num][1]}\n")






