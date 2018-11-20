# Anime Information Displayer

## Using the Jikan API
Creates API GET Requests to obtain Json objects using the Jikan REST-ful API. More information about [Jikan](https://jikan.docs.apiary.io/#)

To use import the API from the Jikan class
```python
from api.jikan import Jikan

jikan = Jikan()
```

Methods can be called on the Jikan object to return Json for the resulting anime/manga/search/etc. Possible uses are listed below, brackets indicate optional paramters.

```python
anime_json = jikan.anime(anime_id, request)

manga_json = jikan.manga(manga_id, request)

person_json = ikan.person(person_id)

character_json = jikan.character(character_id)

seasonal_anime = jikan.season(year, season)

seasons_archive = jikan.archive()

anime_schedule = jikan.schedule(day)

top_anime = jikan.top("anime", page, subtype)

top_manga = jikan.top("manga", page, subtype)

top_anime_genre = jikan.genre("anime", genre, page)

top_manga_genre = jikan.genre("manga", genre, page)

search = jikan.search(category, name)
```
