from typing import Dict, List, Iterator, Optional

#Класс фильма
class Movie:
    def __init__(self, title: str, genre: str, year: int):
        self.title = title
        self.genre = genre
        self.year = year

    def __str__(self) -> str:
        return f"{self.title} ({self.year}) - {self.genre}"


class MovieCollection:
    def __init__(self):
        self.movies: Dict[str, Movie] = {} #словарь фильмов основной коллекции, где ключ - название фильма, значение - объект фильма
        self.custom_collections: Dict[str, List[Movie]] = {} #словарь пользовательских коллекций, ключ - имя коллекции, значение -
        #- список фильмов в этой коллекции

    def add_movie(self, movie: Movie) -> None: #Добавляем фильм в основную коллекцию
        self.movies[movie.title] = movie

    def remove_movie(self, title: str) -> None: #удаляем фильм из основной коллекции и пользовательских коллекций
        if title in self.movies:
            del self.movies[title]
        for collection in self.custom_collections.values():
            collection[:] = [m for m in collection if m.title != title]

    def get_movie(self, title: str) -> Optional[Movie]: #получаем объект фильма по названию
        return self.movies.get(title)

    def add_to_collection(self, collection_name: str, title: str) -> None: #получаем объект фильма и добавляем фильм в пользовательскую коллекцию
        #если коллекция не существует - создается новая
        movie = self.get_movie(title)
        if movie:
            self.custom_collections.setdefault(collection_name, []).append(movie)

    def remove_from_collection(self, collection_name: str, title: str) -> None: #удаляем фильм из пользовательской коллекции
        if collection_name in self.custom_collections:
            self.custom_collections[collection_name] = [
                m for m in self.custom_collections[collection_name] if m.title != title
            ]
    #поиск фильма по жанру
    def search_by_genre(self, genre: str) -> List[Movie]:
        return [m for m in self.movies.values() if m.genre.lower() == genre.lower()]

    #поиск фильма по году выпуска
    def search_by_year(self, year: int) -> List[Movie]:
        return [m for m in self.movies.values() if m.year == year]

    #поиск по ключевому слову в названии фильма
    def search_by_keyword(self, keyword: str) -> List[Movie]:
        return [m for m in self.movies.values() if keyword.lower() in m.title.lower()]

    #вывод списка всех коллекций и соответствующих им фильмов
    def list_collections(self) -> None:
        for name, movies in self.custom_collections.items():
            print(f"\nКоллекция: {name}")
            for movie in movies:
                print(f" - {movie}")

    def __iter__(self) -> Iterator[Movie]:
        return iter(self.movies.values())