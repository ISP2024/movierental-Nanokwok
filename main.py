# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie, MovieCatalog
from rental import Rental
from customer import Customer


def make_movies():
    """Some sample movies."""
    moviecatalog = MovieCatalog()
    movies = [
        # Movie("Air"),
        # Movie("Oppenheimer"),
        # Movie("Frozen"),
        # Movie("Bitconned"),
        # Movie("Particle Fever")
        moviecatalog.get_movie("Air"),
        moviecatalog.get_movie("Oppenheimer"),
        moviecatalog.get_movie("Frozen"),
        moviecatalog.get_movie("Bitconned"),
        moviecatalog.get_movie("Particle Fever")
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        if movie:
            customer.add_rental(Rental(movie, days))
            days = (days + 2) % 5 + 1
        else:
            print("Sorry, couldn't find that movie.")
    print(customer.statement())
    # # Get the Singleton Movie Catalog
    # catalog = MovieCatalog()
    # # Get the first movie named 'Mulan'
    # movie = catalog.get_movie("Mulan")
    # # Get 'Mulan' released in 1998
    # old_movie = catalog.get_movie("Mulan", 1998)
    # print(movie)
    # print(old_movie)
