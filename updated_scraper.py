from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Webdriver
browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

scraped_data = []

def scrape():
    soup = BeautifulSoup(browser.page_source, "html.parser")
    bright_star_table =soup.find("table",sttrs=("class","wikitable"))
    table_body = bright_star_table,find('tbody')
    table_rows =table_body.find_all('tr')
    for row in table_rows:
        table_cols =row.find_all('td')
        temp_list = []
        for col_data in table_cols:
            data= col_data.text.strip() 
            temp_list.append(data)
            scraped_data.append(temp_list)   


   
          
# Calling Method
scrape()

for i in range(0,len(scraped_data)):
    star_names =scraped_data[i][1]
    Distance = scraped_data[i][3]
    mass = scraped_data[i][5]
    Radius = scraped_data[i][6]
    Lum = scraped_data[i][7]

    requires_data  = [star_names, Distance,Mass , Radius,Lum]
    stars_data.append(required_data)

# Define Header
headers= ["name", "distance", "mass", "radius", "luminosity"]

# Define pandas DataFrame 
star_df_1 = pd.DataFrame(stars_data, columns=headers)

# Convert to CSV
star_df_1.to_csv('scraped_data.csv',index=True, index_label="id")