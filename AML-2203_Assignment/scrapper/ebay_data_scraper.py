# imports
import requests
from bs4 import BeautifulSoup
import json
import time
import random

i = 1
final_object_list = []

# define headers to select and navigate HTML elements
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}

# render the file with links to iterate 
with open(r'C:\Users\Kaswala\Desktop\Term2_Lambton\Python_2203\scraping\bestbuy\ebay_laptop_link.txt', 'r') as file:
    links = [line.strip() for line in file]

for link in links:
    # parse HTML code of the link by using request library get() method
    mainSoup = BeautifulSoup(requests.get(link, headers=headers).content, 'html.parser')
    # set break of random float second to avoid captcha
    random_float = random.uniform(1,4)
    time.sleep(random_float)
    try:
        # from HTML parse code find the tag which has asked attribute

        # collect text of name of product
        name = mainSoup.find("span",{"class":"ux-textspans ux-textspans--BOLD"}).text
        # collect text of price of product
        price = mainSoup.find("div",{"class":"x-price-primary"}).text

        try:
            # collect text of condition of product
            condition = mainSoup.find_all("span",{"data-testid":"ux-textual-display"})[0].text
        except:
            condition = ""

        try:
            # collect text of category of product
            category = mainSoup.find_all("a",{"class":"seo-breadcrumb-text"})[1].text
        except:
            category = ""

        try:
            # collect text of sub category of product
            sub_category = mainSoup.find_all("a",{"class":"seo-breadcrumb-text"})[2].text
        except:
            sub_category = ""

        try:
            # collect text of rating of product
            rating = mainSoup.find("div",{"class":"d-stores-info-categories__container__info__section__item"}).find("span").text
        except:
            rating = ""

        try:
            # collect text of overview of product
            overview = mainSoup.find("div",{"data-testid":"ux-layout-section-module-evo"}).text
        except:
            overview = ""

        try:
            # collect text of count of reviews of product
            review_count = mainSoup.find("span",{"class":"SECONDARY"}).text
        except:
            review_count = "0"

        try:
            # collect text of feedbacks of product
            feedback_tag = mainSoup.find_all("div",{"class":"fdbk-container__details__comment"})
            feedback = [each.text for each in feedback_tag]
        except:
            feedback = []

        temp_dict = {
                    "url":link,
                    "category":category,
                    "sub_category":sub_category,
                    "name":name,
                    "price":price,
                    "review_count":review_count,
                    "condition":condition,
                    "overview":overview,
                    "rating":rating,
                    "feedback":feedback
                    }
        final_object_list.append(temp_dict)

        # dump dictionary into json
        data = json.dumps(final_object_list, indent=4)  
        # write dumped data into json file
        with open("ebay_laptop_data.json", "w", encoding='utf-8') as outfile:
            outfile.write(data, )
        print(i," Successfully scraped: ",link)
        i+=1
    except:
        print("Error expected!!!!", link)

        # whichever links will not be scraped, will be stored into a file to analyze the reason
        with open("error_ebay_laptop.txt", "a") as f:
            f.write(link+'\n')
