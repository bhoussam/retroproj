from selenium import webdriver
from selenium.webdriver.common.by import By
from tqdm import tqdm
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd
import streamlit as st
import os

@st.cache_data()
def populate_df():
    st.write('Attends 2sc stp')
    # Create webdriver object
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    service = webdriver.ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(options=op, service=service)

    # Get the website
    driver.get("https://leretroprojecteur.com")

    # Make Python sleep for some time
    sleep(2)

    films = []
    reals = []
    annees = []
    lieux = []
    dates = []
    for clicker in range(8):
        # Obtain the number of rows in body
        table = ""
        table = driver.find_elements(By.XPATH, '//*[@id="userdata"]/tbody')[0]

        for i, td in enumerate(tqdm(table.find_elements(By.TAG_NAME, "td"))):
            if i % 2 == 0:
                contenu = td.text.rsplit(',', 1)
                film = contenu[0]
                real = contenu[1]
                films.append(film)
                reals.append(real)
            else:
                contenu = td.text
                lieux.append(contenu)
                dates.append(driver.find_element(By.XPATH, '//*[@id="date_of_today"]').text)

        driver.find_element(By.XPATH, '//*[@id="move_date_forward"]').click()
        # Make Python sleep for some time
        sleep(.1)

    df = pd.DataFrame(
        {
            "films": films,
            "reals": reals,
            "lieux": lieux,
            "date": dates
        }
    )

    return df