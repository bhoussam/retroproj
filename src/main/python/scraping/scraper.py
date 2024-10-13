from selenium import webdriver
from selenium.webdriver.common.by import By
from tqdm import tqdm
from time import sleep

import pandas as pd


def populate_df(nb_days):
    # Create webdriver object
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(options=op)
    driver.implicitly_wait(10)

    # Get the website
    driver.get("https://leretroprojecteur.com")

    films = []
    reals = []
    annees = []
    lieux = []
    dates = []
    for clicker in tqdm(range(nb_days)):
        sleep(1)

        table = driver.find_elements(By.XPATH, "//div[@class='flex group']")
        date = driver.find_elements(By.XPATH,'/html/body/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div[2]')[0].text + ' ' + str(pd.to_datetime('today').year)

        for div in tqdm(table):
            text = div.text
            films.append(text.split('\n')[0].rsplit(',', 1)[0])
            reals.append(text.split('\n')[0].rsplit(',', 1)[1].split('(')[0])
            annees.append(text.split('\n')[0].rsplit(',', 1)[1].split('(')[1].replace(')', ''))
            lieux.append(' '.join(text.split('\n')[1:]))
            dates.append(date)


        driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div[3]/div').click()
        # Make Python sleep for some time
        sleep(.1)

    df = pd.DataFrame(
        {
            "films": films,
            "reals": reals,
            "annees": annees,
            "lieux": lieux,
            "date": dates
        }
    )

    return df

def scrap_watchlsit():
    pass