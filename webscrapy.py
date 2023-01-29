import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd


url = "https://www.jumia.co.ke/flash-sales/"
print(url)
# Def the Url function
def get_pagecontent(url):
    html_text= requests.get(url).text
    soup= BeautifulSoup(html_text,"lxml")
    return soup



#Retrieve product name
def getproductname(soup): 
    product_name= soup.find_all("h3", class_ = "name")
    product_names= []
    for product in product_name:
        product_names.append(product.text)
    # print(product_names)
    return product_names


#Retrieve Brand Name-used the first item in the product name as the Brand
def getproductbrand(soup): 
    product_brand= soup.find_all("h3", class_ = "name")
    product_brands= []
    for product in product_brand:
        prod_brand= product.text.split()[0]
        product_brands.append(prod_brand)
    print(product_brands)
    return product_brands

#Retrieve Price
def getproductprice(soup):
    product_price= soup.find_all("div", class_ = "prc")
    product_prices= []
    for product in product_price:
        product_prices.append(product.text)
    print(product_prices)
    return product_prices

#Retrieve the Discount
def getproductdiscount(soup):
    product_discount= soup.find_all("div", class_ = "bdg _dsct _sm")
    product_discounts= []
    for product in product_discount:
        product_discounts.append(product.text)
    print(product_discounts)
    return product_discounts   

#Retrieve the Number of reviews.
def getproductreviewcnt(soup):
    product_review_element= soup.find_all("div", class_ = "rev")
    product_reviewcnt= []
    for product in product_review_element:
        prod_rev= product.text.split("(")[1]
        prod_review= prod_rev.split(")")[0]
        product_reviewcnt.append(prod_review)
    print(product_reviewcnt)
    return product_reviewcnt


#Retrieve the ratings..
def getproductrating(soup):
    product_rating_elemet= soup.find_all("div", class_ = "stars _s")
    product_ratings= []
    for product in product_rating_elemet:
        product_ratings.append(product.text)
    print(product_ratings)
    return product_ratings

#Retrieve the remaining stock.
def getproductcount(soup):
    product_count= soup.find_all("div", class_ = "stk")
    product_counts= []
    for product in product_count:
        product_counts.append(product.text)
    print(product_counts)
    return product_counts  


soup = get_pagecontent (url)
name_list= getproductname (soup)
brand_list=getproductbrand (soup)
price_list=getproductprice (soup)
discount_list=getproductdiscount(soup)
reviewcnt_list=getproductreviewcnt (soup)
rating_list=getproductrating (soup)
getproductcount (soup)


list_of_lists = [name_list, brand_list, price_list, discount_list, reviewcnt_list,rating_list]


# Save and review the product data
with open('jumia_products.csv', 'w') as jumia_file:
    fieldnames = ["name", "brand", "price", "discount", "reviews", "rating"]
    
    csvwriter = csv.writer(jumia_file)
    csvwriter.writerow(fieldnames)
    first_items = []
    second_items =[]
    third_items = []
    forth_items = []
    fifth_items = []
    sixth_items = []
    
    #loop through product list to update csv file

    for product in list_of_lists:
        first_items.append(product[0])
        second_items.append(product[1])
        third_items.append(product[2])
        forth_items.append(product[3])
        fifth_items.append(product[4])
        sixth_items.append(product[5])
    my_list = [first_items,second_items,third_items,forth_items,fifth_items,sixth_items]
    for product in  my_list:
        
        csvwriter.writerow(product)
        
    print("Done! All products have been added to CSV file")

#Using pandas to do data manipulation
jumia = pd.read_csv('jumia_products.csv', sep = "\t", encoding='latin')
print(jumia.head(5))







