# Anime Info Displayer

View useful information about anime series in one convenient and condensed location. This application will display all information that is found on MyAnimeList in a more condensed format in addition to a visual representation of all prequels, sequels, side stories, etc. in a easy to read mathematical tree format.

The backend is created using Python to make API calls to obtain information and generate the watch order tree. The front end is created using the electron framework for JavaScript, HTML, and CSS.

## Dependencies

Ensure Python is installed with the required packages before running this application. Install/update the Python packages for requests using pip

```shell
pip install requests
```

Ensure Node.js is installed with the required libraries before running this application. The required libraries are electron and python-shell. Install all libraries using npm

```shell
npm install
```

## Jikan API

This program creates API GET Requests to obtain JSON objects using the Jikan REST-ful API. More information about [Jikan](https://jikan.docs.apiary.io/#). API calls are done using the Python requests package. Ensure this package is installed using pip. This API can also be used by importing the Jikan class from the Python module

```python
from jikan import Jikan

jikan = Jikan()
```

Methods can be called on the Jikan object to return JSON for the resulting anime/manga/search/etc. Note that manga refers also refers light novels. Some possible uses are listed below

```python
one_punch_man = jikan.anime(30276)
fullmetal_alchemist = jikan.manga(25)

seasonal = jikan.season(2018, 'fall')
schedule = jikan.schedule()

popular_anime = jikan.top('anime', 'bypopularity')
top_manga_page4 = jikan.top('manga', 4)
action_anime = jikan.genre('anime', 'action')
jojo_manga = jikan.search('manga', 'jojo')
```

## Running the Application

The front end of this program is run using the electron library for Node.js. More information about [electron](https://electronjs.org/). After ensuring all dependencies have been installed/updated, start the application by running the `run.sh` script or by using npm

```shell
npm start
```

The program will open and automatically load the table for the 50 top anime sorted by popularity. Using the search feature will search MyAnimeList for the anime by the name of the title provided. Each entry of the table will list general information and can be clicked to open a new window with more information about the anime. Multiple windows can be opened at once.
