from abc import ABC, abstractmethod


class PriceStrategy(ABC):
    """Base class for price strategies."""

    @abstractmethod
    def get_price(self, days_rented):
        """Calculate price based on the number of days rented."""
        pass

    @abstractmethod
    def get_rental_points(self, days_rented):
        """Calculate rental points based on the number of days rented."""
        pass


class RegularPrice(PriceStrategy):
    def get_price(self, days_rented):
        amount = 2.0
        if days_rented > 2:
            amount += 1.5 * (days_rented - 2)
        return amount

    def get_rental_points(self, days_rented):
        return 1


class NewReleasePrice(PriceStrategy):
    def get_price(self, days_rented):
        return 3 * days_rented

    def get_rental_points(self, days_rented):
        return days_rented


class ChildrenPrice(PriceStrategy):
    def get_price(self, days_rented):
        amount = 1.5
        if days_rented > 3:
            amount += 1.5 * (days_rented - 3)
        return amount

    def get_rental_points(self, days_rented):
        return 1


class Movie:
    """
    A movie available for rent.
    """
    # The types of movies (price_code).
    REGULAR = RegularPrice()
    NEW_RELEASE = NewReleasePrice()
    CHILDRENS = ChildrenPrice()

    def __init__(self, title, price_strategy):
        self.title = title
        self.price_strategy = price_strategy

    def get_price(self, days_rented):
        """Calculate the price based on the price strategy."""
        return self.price_strategy.get_price(days_rented)

    def get_rental_points(self, days_rented):
        """Calculate rental points based on the price strategy."""
        return self.price_strategy.get_rental_points(days_rented)

    def get_title(self):
        return self.title

    def __str__(self):
        return self.title
