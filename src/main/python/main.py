# Python program to scrape table from website

# import libraries selenium and time
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

import pandas as pd

# Create webdriver object
driver = webdriver.Chrome()

# Get the website
driver.get("https://leretroprojecteur.com")

# Make Python sleep for some time
sleep(2)

# Obtain the number of rows in body
table = driver.find_elements(By.XPATH, '//*[@id="userdata"]/tbody')[0]

films = []
reals = []
annees = []
lieux = []
for i, td in enumerate(table.find_elements(By.TAG_NAME, "td")):
    if i%2 == 0:
        contenu = td.text.split(',')
        film = contenu[0]
        real = contenu[1] 
        films.append(film)
        reals.append(real)
    else:
        contenu = td.text
        lieux.append(contenu)

df = pd.DataFrame(
    {
        "films": films,
        "reals": reals,
        "lieux": lieux,
    }
)

1