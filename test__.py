import pytest
from classes import Movie, MovieCollection
from data_test_cinema import movies


#тест функции добавления фильмов
def test_add_multiple_movies():
    collection = MovieCollection()
    for movie in movies:
        collection.add_movie(movie)
    #проверяем, что все фильмы добавлены
    for movie in movies:
        assert movie.title in collection.movies
        assert collection.movies[movie.title].genre == movie.genre

#тест функции поиска по жанру
def test_search_by_genre():
    collection = MovieCollection()
    for movie in movies:
        collection.add_movie(movie)
    # ищем фильм по жанру "Ужасы"
    result = collection.search_by_genre("Ужасы")
    assert result[0].title == "Фильм 5"