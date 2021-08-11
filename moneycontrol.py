import requests
from bs4 import BeautifulSoup


page = requests.get("https://www.moneycontrol.com/india/stockpricequote/trading/mmtc/MMT")
soup = BeautifulSoup(page.content, 'html.parser')

t = soup.find_all(id='mainprice')
mmtc = t[0].find(class_="inid_name").get_text()
print(mmtc)
mmtc1 = t[0].find(class_='indimprice').get_text()
print(mmtc1)

t1 = soup.find_all(class_='indprirange')
print(t1[0].find(class_='drang MT10').get_text())
day_range = t1[0].find(class_='rangamount clearfix').get_text()
print(day_range)
print(t1[0].find(class_='drang MT20').get_text())
print(t1[0].find(class_='FL nseL52').get_text())
print(t1[0].find(class_='FR nseH52').get_text())
print(t1[0].find(class_='clearfix MT20').get_text())

t2 = soup.find_all(class_='nsestock_overview bsestock_overview')
print(t2[0].find(class_='mob-hide').get_text())