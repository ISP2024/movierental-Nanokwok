import logging

from movie import Movie


class Rental:
    """
    A rental of a movie by customer.
    From Fowler's refactoring example.

    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated.
    For simplicity of this application only days_rented is recorded.
    """

    def __init__(self, movie, days_rented):
        """Initialize a new movie rental object for
           a movie with known rental period (daysRented).
        """
        self.movie = movie
        self.days_rented = days_rented

    def get_movie(self):
        return self.movie

    def get_days_rented(self):
        return self.days_rented

    def get_price(self):
        # compute rental change
        amount = 0
        if self.movie.get_price_code() == Movie.REGULAR:
            # Two days for $2, additional days 1.50 per day.
            amount = 2.0
            if self.get_days_rented() > 2:
                amount += 1.5 * (self.days_rented - 2)
        elif self.movie.get_price_code() == Movie.CHILDRENS:
            # Three days for $1.50, additional days 1.50 per day.
            amount = 1.5
            if self.get_days_rented() > 3:
                amount += 1.5 * (self.days_rented - 3)
        elif self.movie.get_price_code() == Movie.NEW_RELEASE:
            # Straight $3 per day charge
            amount = 3 * self.days_rented
        else:
            log = logging.getLogger()
            log.error(
                f"Movie {self.movie} has unrecognized priceCode {self.movie.get_price_code()}")
        return amount

    def get_rental_points(self, frequent_renter_points):
        if self.get_movie().get_price_code() == Movie.NEW_RELEASE:
            # New release earns 1 point per day rented
            frequent_renter_points += self.get_days_rented()
        else:
            # Other rentals get only 1 point
            frequent_renter_points += 1
        return frequent_renter_points
