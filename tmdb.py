import config as cfg
from ttictoc import TicToc
import requests
import csv
import os
from pathlib import Path
from statistics import mean
import configparser
import json 
import time
import mysql.connector

config = configparser.ConfigParser()
config.read('config.ini')


class Tmdb():
    

    def extract(self,page,api_key,year):

        cnx = mysql.connector.connect(user='predictor', password='predictor',
                              host=os.environ['DB_HOST'],
                              database='predictor')

        page = int(page)
        print('Starting The Movie Database extraction...')
        t = TicToc()

        result = requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&primary_release_year={str(year)}&page={page}").json()
        pages_total = result['total_pages']
        #pprint(result)


        while page <= pages_total:
            

            result = requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&primary_release_year={str(year)}&page={page}").json()
            
            for movie in result['results']:
                
                movie_id = movie.get("id",None)

                row = [ movie_id,
                        movie.get("title",None),
                        movie.get("original_title",None),
                        movie.get("release_date",None),
                        movie.get("popularity",None)]

                movie_page = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}").json()

                row = row + [movie_page.get('imdb_id',None)]
                movie_row_format = [item if item else ' ' for item in row]
                
                cursor = cnx.cursor()
                request = f'INSERT INTO movies (id,title,original_title,release_date,popularity,imdb_id) VALUES ({row[0]},"{row[1]}","{row[2]}","{row[3]}",{row[4]},{row[5][2:]})'
                cursor.execute(request)
                cursor.close()
                cnx.commit()

                time.sleep(3)

            print(f'Extracted page {page} out of {pages_total} ~ {round((page/pages_total)*100)}% complete')

            

            page += 1

            config.set('USER','page',str(page))
            config.set('USER','year',year)
            with open('config.ini', 'w') as configfile:
                config.write(configfile)

                

                

            