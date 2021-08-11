import pandas as pd
import requests
from bs4 import BeautifulSoup

# FLIPKART
page = requests.get('https://www.flipkart.com/')
soup = BeautifulSoup(page.content, 'html.parser')

t = soup.find_all(class_='_6WQwDJ')
x1 = t[0].find(class_='_3LU4EM')
x2 = t[0].find(class_='_2tDhp2')
x3 = t[0].find(class_='_3khuHA')
print(x1.get_text())
print(x2.get_text())
print(x3.get_text())

deals = [item.find(class_='_3LU4EM').get_text() for item in t]
print(deals)
discounts = [item.find(class_='_2tDhp2').get_text() for item in t]
print(discounts)
#brands = [item.find(class_='_3khuHA').get_text() for item in t]
#print(brands)

table = pd.DataFrame({'deals': deals, 'discounts': discounts})
print(table)