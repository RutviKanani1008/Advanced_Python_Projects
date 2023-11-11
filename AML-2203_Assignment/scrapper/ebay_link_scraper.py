# imports
import requests
from bs4 import BeautifulSoup
import time
import random

# define headers to select and navigate HTML elements
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}

for i in range(1,41):
    link = f"https://www.ebay.ca/b/Computer-Monitors-Projectors-Accessories/162497/bn_1636723?_pgn={i}"
    # parse HTML code of the link by using request library get() method
    mainSoup = BeautifulSoup(requests.get(link, headers=headers).content, 'html.parser')

    # from HTML parse code find the tag which has asked attribute
    all_div_tag = mainSoup.find_all("div",{"class":"s-item__info clearfix"})

    for each in all_div_tag:
        # get href from the tag
        href = each.find("a").get("href")
        # write that url into a .txt file
        with open("ebay_monitors_link.txt", "a") as f:
            f.write(href+'\n')
    print("page",i,"done")

    # set break of random float second to avoid captcha
    random_float = random.uniform(1,4)
    time.sleep(random_float)
