import locale
import os

from scraping.scraper import populate_df
from movies.imdb import _get_french_info
from user.user import User
import pandas as pd
from utils.tools import Config, custom_logger

conf = Config(os.getenv("CONF_PATH"))
DATA_PATH = conf.get_property('DATA_PATH')
log = custom_logger()

log.info("Begin")
log.info("set to french locale in order to parse date")
locale.setlocale(category=locale.LC_ALL, locale='fr_FR.utf8')

# scrap the website & cast to datetime
data = populate_df(nb_days=1)
data['date2'] = pd.to_datetime(data['date'].str.title(), format='%A %d %B %Y')
imdb = pd.json_normalize(data.apply(lambda x: _get_french_info(x.films, int(x.annees)), axis=1))
data = pd.concat([data, imdb], axis=1)

# save data
data.to_csv(os.path.join(DATA_PATH, 'base.csv'))

# Get user wishlist
df_users = pd.read_csv(os.path.join(DATA_PATH, 'users.csv'))

for username in df_users['user']:
    user = User(username, "")
    watch_list = user.scrap_watchlist()
    alert = pd.DataFrame(watch_list)
    alert.to_csv(os.path.join(DATA_PATH, '{}.csv'.format(username)))

    alert = pd.read_csv('/home/houssam/projects/retroproj/data/yndi.csv')
    data = pd.read_csv('/home/houssam/projects/retroproj/data/base.csv')
    df_alert = pd.merge(alert, data, on=['imdb_name_fr', 'imdb_date_sortie', 'imdb_director'])
    user.send_push(df_alert)

