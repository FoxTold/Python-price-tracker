from bs4 import BeautifulSoup
import requests

def ceneo(url):
    html_ps5 =  requests.get(url)
    soup=BeautifulSoup(html_ps5.content,"html.parser")
    theme = soup.find("div",class_="js_searchInGoogleTooltip breadcrumbs__item")
    print(f"{theme.text}")
    cheapest =  soup.find("div",class_="layout-wrapper product-top__wrapper")
    title = cheapest.find("h1",class_="product-top__product-info__name js_product-h1-link js_product-force-scroll js_searchInGoogleTooltip default-cursor")
    shop = cheapest.find("a",class_="store-logo go-to-shop")
    shop = shop.find("img")
    price = soup.find("div",class_="product-offer-summary")
    price = price.find("span",class_="value")
    print(f"{title.text}\n Price: {price.text}zł\n Shop: {shop['alt']}")
    best_offers = soup.find("ul",class_="product-offers__list js_product-offers")
    offers = best_offers.find_all("li",class_="product-offers__list__item js_productOfferGroupItem")
    for i in offers:
        shop = i.find("img")
        topic =i.find("div",class_="product-offer__product__offer-details__name short-name")
        topic = topic.find("a")
        price = i.find("span",class_="value")
        print (f"Name: {topic['title']}\n Price: {price.text}\n Shop:{shop['alt']}\n###########################################################")


def main():
    print("Made by Tomasz Rybiński\nPrices Tracker")  
    choice = -1
    while True:
        print("\n1.Macbook air M1\n2.Playstation 5\n3.Iphone 12 / IPhone 12 mini\n4.Galaxy S21 5G\n5.IPhone SE")
        try:
            choice = int(input("\nChoice: "))
     
            if(choice == 1):
                ceneo("https://www.ceneo.pl/99105003")
            elif(choice==2):
                ceneo("https://www.ceneo.pl/86467784")
            elif(choice==3):
                ceneo("https://www.ceneo.pl/98019111")
                ceneo("https://www.ceneo.pl/98018340#tag=familyTiles")
            elif(choice ==4):
                ceneo("https://www.ceneo.pl/98143284;02514;#tag=nph_row_promotion")
            elif(choice ==5):
                ceneo("https://www.ceneo.pl/92918436")
            else:
                print("Incorrect input")

        except:
            print("Invalid input data")

      
main()

