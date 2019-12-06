TMDB extracts data from The Movie Database API and exports it to a Dockerized SQL database

Pre-requisistes:
    - Docker Desktop

How to use:
    - Open the config file with Notepad or an IDE
    - Paste your The Movie Database user key into the [USER] config
    - Replace the 0 in year with the wanted year to scrap
    - Launch a "docker-compose up" in your bash in from the docker folder
    - Open localhost:8080 in your browser and access the database with the "predictor" password
    - To stop the app, simply press Crtl+C in your bash
    - To reinitialize, replace the values in [USER] with the [DEFAULT] values