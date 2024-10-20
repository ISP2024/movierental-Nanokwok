from abc import ABC, abstractmethod


class PriceStrategy(ABC):
    """Base class for price strategies."""

    _instances = {}

    def __new__(cls, *args, **kwargs):
        """Implement Singleton pattern."""
        if cls not in cls._instances:
            cls._instances[cls] = super(PriceStrategy, cls).__new__(cls)
        return cls._instances[cls]

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
