from pricing import RegularPrice, NewReleasePrice, ChildrenPrice


class Movie:
    """
    A movie available for rent.
    """
    # The types of movies (price_code).
    REGULAR = RegularPrice()
    NEW_RELEASE = NewReleasePrice()
    CHILDRENS = ChildrenPrice()

    def __init__(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def __str__(self):
        return self.title
