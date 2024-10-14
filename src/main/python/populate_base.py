import locale

from scraping.scraper import populate_df
from user.user import User
import pandas as pd

# set to french locale in order to parse date
locale.setlocale(category=locale.LC_ALL, locale='fr_FR.utf8')

# Get user wishlist
# spacelessvoid
# amyhensarling
user = User("amyhensarling", "")
watch_list = user.scrap_watchlist()

# scrap the website & cast to datetime
data = populate_df(nb_days=1)
data['date2'] = pd.to_datetime(data['date'].str.title(), format='%A %d %B %Y')

# save data
data.to_csv('data/base.csv')

