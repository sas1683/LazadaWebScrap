from bs4 import BeautifulSoup
import requests
import time
import datetime

import smtplib
# Connect to Website and pull in data

URL = 'https://www.lazada.sg//products/i694532496-s2151926998.html?spm=a2o42.cart.0.0.345d7a93xxz4By&urlFlag=true'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1',class_='pdp-mod-product-badge-title').get_text()

price = soup2.find('span',class_='pdp-price pdp-price_type_normal pdp-price_color_orange pdp-price_size_xl').get_text()


price = price.strip()[1:]
title = title.strip()

print(title)
print(price)

import csv 


today = datetime.date.today()
header = ['Title', 'Price', 'Date']
data = [title, price, today]


with open('LazadaWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)
    
import pandas as pd

df = pd.read_csv(r'C:\Users\senthild76\LazadaWebScraperDataset.csv')

print(df)
    

def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('sas1683@gmail.com','xxxxxxxxxxxxxx')
    
    subject = "The Bread maker you want is below $70! Now is your chance to buy!"
    body = "Sas, This is the moment we have been waiting for. Now is your chance to pick up the maker of your dreams. Don't mess it up! Link here: https://www.lazada.sg//products/i694532496-s2151926998.html?spm=a2o42.cart.0.0.345d7a93xxz4By&urlFlag=true"
   
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'sas1683@gmail.com',
        msg
     
    )