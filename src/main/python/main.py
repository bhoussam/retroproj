# Python program to scrape table from website

# import libraries selenium and time
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Create webdriver object
driver = webdriver.Chrome()

# Get the website
driver.get("https://leretroprojecteur.com")

# Make Python sleep for some time
sleep(2)

# Obtain the number of rows in body
table = driver.find_elements(By.XPATH, '//*[@id="userdata"]/tbody')[0]


for tr in table.find_elements(By.TAG_NAME, "tr"):
    print(tr.text)