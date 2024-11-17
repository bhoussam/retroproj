import json
from pprint import pprint

from imdbmovies import IMDB

def _split_name_year(movie):
    if '(' in movie:
        movie_name = movie.split('(')[0]
        movie_year = int(movie.split('(')[-1][:-1])
    else:
        movie_name = movie
        movie_year = None
    return movie_name, movie_year

def _get_french_info(original_movie_name, year):
    imdb = IMDB(lang='fr')
    res = imdb.get_by_name(original_movie_name, year=year)
    if 'status' not in res:

        if 'alternateName' in res and res['alternateName']:
            name = res['alternateName']
        else:
            name = res['name']

        if res['director']:
            director = res['director'][0]['name']
        else:
            director = ''
        return {
            'imdb_name_fr': name,
            'imdb_date_sortie': res['datePublished'],
            'imdb_director': director
        }
    else:
        return {
            'imdb_name_fr': original_movie_name,
            'imdb_date_sortie': 'NC',
            'imdb_director': 'NC'
        }

if __name__ == '__main__':
    pprint(_get_french_info("to be or not to be", 1942))
    # imdb = IMDB(lang='fr')
    # pprint(imdb.get_by_name(name="toto"))
    # pprint(imdb.get_by_id('tt0116688'))
