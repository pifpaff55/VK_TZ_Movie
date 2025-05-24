from typing import Dict, List, Iterator, Optional


class Movie:
    def __init__(self, title: str, genre: str, year: int):
        self.title = title
        self.genre = genre
        self.year = year

    def __str__(self) -> str:
        return f"{self.title} ({self.year}) - {self.genre}"


class MovieCollection:
    def __init__(self):
        self.movies: Dict[str, Movie] = {}
        self.custom_collections: Dict[str, List[Movie]] = {}

    def add_movie(self, movie: Movie) -> None:
        self.movies[movie.title] = movie

    def remove_movie(self, title: str) -> None:
        if title in self.movies:
            del self.movies[title]
        for collection in self.custom_collections.values():
            collection[:] = [m for m in collection if m.title != title]

    def get_movie(self, title: str) -> Optional[Movie]:
        return self.movies.get(title)

    def add_to_collection(self, collection_name: str, title: str) -> None:
        movie = self.get_movie(title)
        if movie:
            self.custom_collections.setdefault(collection_name, []).append(movie)

    def remove_from_collection(self, collection_name: str, title: str) -> None:
        if collection_name in self.custom_collections:
            self.custom_collections[collection_name] = [
                m for m in self.custom_collections[collection_name] if m.title != title
            ]

    def search_by_genre(self, genre: str) -> List[Movie]:
        return [m for m in self.movies.values() if m.genre.lower() == genre.lower()]

    def search_by_year(self, year: int) -> List[Movie]:
        return [m for m in self.movies.values() if m.year == year]

    def search_by_keyword(self, keyword: str) -> List[Movie]:
        return [m for m in self.movies.values() if keyword.lower() in m.title.lower()]

    def list_collections(self) -> None:
        for name, movies in self.custom_collections.items():
            print(f"\nКоллекция: {name}")
            for movie in movies:
                print(f" - {movie}")

    def __iter__(self) -> Iterator[Movie]:
        return iter(self.movies.values())