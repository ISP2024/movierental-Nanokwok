from pricing import RegularPrice, NewReleasePrice, ChildrenPrice


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
