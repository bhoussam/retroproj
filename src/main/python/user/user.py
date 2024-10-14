from src.main.python.scraping.scraper import _get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from tqdm import tqdm
from time import sleep


class User:

    def __init__(self, username, mail):
        self.username = username
        self.mail = mail

    def send_mail(self):
        pass

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
                    watch_list.append(movie)

                driver.get("https://letterboxd.com/{}/watchlist/page/{}/".format(self.username, num_page))

        else:
            table = driver.find_elements(By.XPATH, '//*[@id="content"]/div/div/section/ul')
            if table:
                for li in table[0].find_elements(By.TAG_NAME, "li"):
                    movie = li.find_elements(By.TAG_NAME, "a")[0].get_attribute('data-original-title')
                    watch_list.append(movie)

        return watch_list
