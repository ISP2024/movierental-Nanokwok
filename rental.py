from movie import Movie
from pricing import PriceStrategy
from datetime import datetime
from pricing import RegularPrice, NewReleasePrice, ChildrenPrice


def price_code_for_movie(movie: Movie) -> PriceStrategy:
    """
    Determines the price strategy for a given movie.
    """
    current_year = datetime.now().year

    if movie.year == current_year:
        return NewReleasePrice()

    for genre in movie.genres:
        if genre.lower() in ["children", "childrens"]:
            return ChildrenPrice()

    return RegularPrice()


class Rental:
    """
    A rental of a movie by customer.
    From Fowler's refactoring example.

    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated.
    For simplicity of this application only days_rented is recorded.
    """

    def __init__(self, movie, days_rented, price_code: PriceStrategy):
        """Initialize a new movie rental object for
           a movie with known rental period (daysRented).
        """
        self.movie = movie
        self.days_rented = days_rented
        self.price_code = price_code

    def get_movie(self):
        return self.movie

    def get_days_rented(self):
        return self.days_rented

    def get_price(self):
        return self.price_code.get_price(self.days_rented)

    def get_rental_points(self):
        return self.price_code.get_rental_points(self.days_rented)

    def get_price_code(self):
        return self.price_code
