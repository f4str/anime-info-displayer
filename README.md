# Anime Information Displayer

## Jikan API
This program creates API GET Requests to obtain Json objects using the Jikan REST-ful API. More information about [Jikan](https://jikan.docs.apiary.io/#)

API calls are done using the Python requests package. Ensure this package is installed using pip

```bash
pip install requests
```

This API can also be used by importing the Jikan class

```python
from api.jikan import Jikan

jikan = Jikan()
```

Methods can be called on the Jikan object to return Json for the resulting anime/manga/search/etc. Note that manga refers also refers light novels. Some possible uses are listed below

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
