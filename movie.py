from typing import Collection

from pricing import RegularPrice, NewReleasePrice, ChildrenPrice


class Movie:
    """
    A movie available for rent.
    """
    # The types of movies (price_code).
    REGULAR = RegularPrice()
    NEW_RELEASE = NewReleasePrice()
    CHILDRENS = ChildrenPrice()

    def __init__(self, title: str, year: int, genre: Collection[str]):
        self.title = title
        self.year = year
        self.genres = genre

    def get_title(self):
        return self.title

    def is_genre(self, genre: str) -> bool:
        return genre.lower() in self.genres

    def __str__(self):
        return f"{self.title} ({self.year})"
