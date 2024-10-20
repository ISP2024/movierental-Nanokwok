from typing import Collection

from pricing import PriceStrategy
from dataclasses import dataclass
from typing import Collection


@dataclass(frozen=True)
class Movie:
    """
    A movie available for rent.
    """
    title: str
    price_strategy: PriceStrategy
    year: int
    genres: Collection[str]

    def get_title(self):
        return self.title

    def is_genre(self, genre: str) -> bool:
        return genre.lower() in self.genres

    def __str__(self):
        return f"{self.title} ({self.year})"
