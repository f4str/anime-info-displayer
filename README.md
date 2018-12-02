# Anime Parser

View useful information about anime series in one convenient and condensed location. This application will display all information that is found on MyAnimeList in a more condensed format in addition to a visual representation of all prequels, sequels, side stories, etc. in a easy to read mathematical tree format.

The backend is created using Python to make API calls to obtain information and generate the watch order tree. The front end is created using the electron framework for JavaScript, HTML, and CSS.

## Python Dependencies

Ensure Python is installed with the required packages before running this application. Install/update the Python packages for requests and sqlite3 using pip

```bash
pip install requests
pip install sqlite3
```

## Node.js Dependencies

Ensure Node.js is installed with the required libraries before running this application. Install using npm

```bash
npm install
```

Due to issues with electron and sqlite3, electron-builder must be used to resolve conflicts. After running the command to install libraries, run the electron-builder command

```bash
electron-builder install-app-deps
```

This will build sqlite3 with electron bindings to allow them to be properly compatible.

## Jikan API

This program creates API GET Requests to obtain JSON objects using the Jikan REST-ful API. More information about [Jikan](https://jikan.docs.apiary.io/#)

API calls are done using the Python requests package. Ensure this package is installed using pip

```bash
pip install requests
```

This API can also be used by importing the Jikan class

```python
from api.jikan.jikan import Jikan

jikan = Jikan()
```

Methods can be called on the Jikan object to return JSON for the resulting anime/manga/search/etc. Note that manga refers also refers light novels. Some possible uses are listed below

```python
one_punch_man = jikan.anime(30276)
fullmetal_alchemist = jikan.manga(25)

seasonal = jikan.season(2018, 'fall')
schedule = jikan.schedule()

popular_anime = jikan.top('anime', 1, 'bypopularity')
top_manga = jikan.top('manga', 4)
action_anime = jikan.genre('anime', 'action')
jojo_manga = jikan.search('manga', 'jojo')
```

## SQLite Database

This program uses SQLite to store searchable anime entries. More information about [SQLite](https://www.sqlite.org/index.html) 

Database is stored in the `/database/db.sqlite` file. These entries may become outdated so the database can be updated using the `/database/database.py` file. The database is also used in the front end using electron with Node.js.
