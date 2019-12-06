FROM python:3.7-buster

RUN pip install argparse mysql-connector-python requests config pathlib pprint ttictoc statistics configparser

COPY . /usr/src/TMDB/

WORKDIR /usr/src/TMDB/

CMD python /usr/src/TMDB/app.py

#winpty docker run -it --rm nlyo bash