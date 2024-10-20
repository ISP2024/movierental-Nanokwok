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
        moviecatalog.get_movie("Air")
    ]
    return movies


if __name__ == '__main__':
    # # Create a customer with some rentals
    # customer = Customer("Edward Snowden")
    # days = 1
    # for movie in make_movies():
    #     customer.add_rental(Rental(movie, days, movie.price_strategy))
    #     days = (days + 2) % 5 + 1
    # print(customer.statement())
    # Get the Singleton Movie Catalog
    catalog = MovieCatalog()
    # Get the first movie named 'Mulan'
    movie = catalog.get_movie("Mulan")
    # Get 'Mulan' released in 1998
    old_movie = catalog.get_movie("Mulan", 1998)
    print(movie)
    print(old_movie)
