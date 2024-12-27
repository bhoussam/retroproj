from datetime import datetime

from movies.imdb import _get_french_info, _split_name_year
from scraping.scraper import _get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from tqdm import tqdm
import requests
import json
import smtplib
from email.mime.text import MIMEText
from email.message import EmailMessage
from pretty_html_table import build_table


class User:

    def __init__(self, username, mail):
        self.username = username
        self.mail = mail

    def send_push(self, df_alert):
        if len(df_alert)>0:
            current_week = datetime.today()
            df = df_alert[['films', 'lieux', 'date']]
            output_table = build_table(df, "blue_light")
            email_text = """\
                <html>
                <head></head>
                <body>
                <p>Tes films de la semaine {} !! 😀</p>
                {}
                </body>
                </html>
                """.format(current_week,  output_table)

            GMAIL_USERNAME = "alert.retroproj@gmail.com"
            GMAIL_APP_PASSWORD = "wzgywarbhfzhsqyd"

            recipients = ["houssam.boulemia@yahoo.fr"]
            msg = EmailMessage()
            msg.add_alternative(email_text, subtype='html')
            msg["Subject"] = "[RETROPROJ] Un film de ta watchlist"
            msg["To"] = ", ".join(recipients)
            msg["From"] = f"{GMAIL_USERNAME}@gmail.com"

            smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            smtp_server.login(GMAIL_USERNAME, GMAIL_APP_PASSWORD)
            smtp_server.sendmail(msg["From"], recipients, msg.as_string())
            smtp_server.quit()


    def scrap_watchlist(self):
        # init driver
        driver = _get_driver()

        driver.get("https://letterboxd.com/{}/watchlist/".format(self.username))

        page = driver.find_elements(By.XPATH, '//*[@id="html"]/body')[0]

        watch_list = []

        if page.find_elements(By.XPATH, '//*[@id="content"]/div/div/section/div[2]/div[3]/ul'):
            page_lst = page.find_elements(By.XPATH, '//*[@id="content"]/div/div/section/div[2]/div[3]/ul')[0]
            nbpages = int(page_lst.find_elements(By.TAG_NAME, "a")[-1].accessible_name)

            for i, num_page in enumerate(tqdm(range(2, nbpages+2))):
                table = driver.find_elements(By.XPATH, '//*[@id="content"]/div/div/section/ul')
                for li in table[0].find_elements(By.TAG_NAME, "li"):
                    movie = li.find_elements(By.TAG_NAME, "a")[0].get_attribute('data-original-title')
                    movie_name, movie_year = _split_name_year(movie)
                    watch_list.append(_get_french_info(movie_name, movie_year))

                driver.get("https://letterboxd.com/{}/watchlist/page/{}/".format(self.username, num_page))

        else:
            table = driver.find_elements(By.XPATH, '//*[@id="content"]/div/div/section/ul')
            if table:
                for li in table[0].find_elements(By.TAG_NAME, "li"):
                    movie = li.find_elements(By.TAG_NAME, "a")[0].get_attribute('data-original-title')
                    movie_name, movie_year = _split_name_year(movie)
                    watch_list.append(_get_french_info(movie_name, movie_year))

        return watch_list



