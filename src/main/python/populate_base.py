import locale

from scraping.scraper import populate_df
import pandas as pd

# set to french locale in order to parse date
locale.setlocale(category=locale.LC_ALL, locale='fr_FR.utf8')

# scrap the website & cast to datetime
data = populate_df(nb_days=1)
data['date2'] = pd.to_datetime(data['date'].str.title(), format='%A %d %B %Y')

# save data
data.to_csv('data/base.csv')

