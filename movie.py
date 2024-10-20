from typing import Collection
from pricing import PriceStrategy
from dataclasses import dataclass
import csv

@dataclass(frozen=True)
class Movie:
    """
    A movie available for rent.
    """

    title: str
    year: int
    genres: Collection[str]

    def get_title(self) -> str:
        """
        Retrieve the title of the movie.
        """
        return self.title

    def is_genre(self, string: str) -> bool:
        """
        Check if the movie belongs to a specific genre.
        """
        return string.lower() in self.genres

    def __str__(self) -> str:
        """
        String representation of the Movie instance.
        """
        return f" {self.title} ({self.year})"
    
class MovieCatalog:
    """
    A singleton class that manages a catalog of movies.
    """

    __instances = None

    def __new__(cls):
        """
        Create a new instance of MovieCatalog or return the existing instance.
        """
        if cls.__instances is None:
            cls.__instances = super(MovieCatalog, cls).__new__(cls)
            cls.__instances._movie_list = cls.__load_data()
        return cls.__instances

    @staticmethod
    def __load_data():
        """
        Load movie data from a CSV file and create Movie instances.
        """
        movies = []
        with open("movies.csv", encoding="utf-8") as movie:
            reader = csv.DictReader(movie)
            next(reader)
            for movie_, movie_data in enumerate(reader):
                try:
                    movie = Movie(
                        movie_data['title'],
                        int(movie_data['year']),
                        movie_data['genres'].split('|'))
                    movies.append(movie)
                except (TypeError, ValueError):
                    continue
        return movies

    def get_movie(self, title, year=None):
        """
        Retrieve a movie by its title and optional release year.
        """
        for movie in self._movie_list:
            if title.lower() == movie.title.lower() and (not year or year == movie.year):
                return movie
        return None