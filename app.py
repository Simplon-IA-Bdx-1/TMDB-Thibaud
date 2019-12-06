import argparse
from tmdb import Tmdb
import configparser
import os
import mysql.connector
import socket
import time

config = configparser.ConfigParser()
config.read('config.ini')

# API key config

if config['USER']['key_tmdb'] == '0':

    print('Please paste your TMBD api key into the config file')
    exit()

# Year config

if config['USER']['year'] == '0':
    
    print('Please enter the extraction year into the config file')
    exit()

# Page config

if config['USER']['page'] == '0':
    config.set('USER', 'page', '1')

# Connection SQL

def isOpen(ip,port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      s.connect((ip, int(port)))
      s.shutdown(2)
      return True
   except:
      return False


def connectToDatabase():
    host=os.environ["DB_HOST"]

    while isOpen(host, 3306) == False:
        time.sleep(5)
        print("Waiting for Database")
    return mysql.connector.connect(user='predictor', password='predictor',
                              host=host,
                              database='predictor')

connectToDatabase()

# Extraction

T = Tmdb()
T.extract(config['USER']['page'], config['USER']['key_tmdb'], config['USER']['year'])

