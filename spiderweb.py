from lib.getHtml import getTitle
from lib.getHtml import getLinks
import random
import datetime

url = "https://en.wikipedia.org/wiki/Kevin_Bacon"

title = getTitle(url)

if title is None:
    print("URL not found")
else:
    print(title)

random.seed(datetime.datetime.now())
article ="/wiki/Kevin_Bacon"
links = getLinks(article)
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)
