import unittest
from rental import Rental
from movie import Movie

class RentalTest(unittest.TestCase):

    def setUp(self):
        # Create Movie instances without using nonexistent attributes
        self.new_movie = Movie("Dune: Part Two", 2024, ["Action"])  # New release
        self.regular_movie = Movie("Air", 2020, ["Drama"])  # Regular movie
        self.childrens_movie = Movie("Frozen", 2013, ["Children"])  # Children's movie

    def test_movie_attributes(self):
        """Trivial test to catch refactoring errors or changes in API of Movie."""
        m = Movie("Air", 2020, ["Drama"])
        self.assertEqual("Air", m.get_title())
        self.assertEqual(["Drama"], m.genres)

    def test_rental_price(self):
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_price(), 3.0)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_price(), 15.0)
        rental = Rental(self.childrens_movie, 3)
        self.assertEqual(rental.get_price(), 1.5)
        rental = Rental(self.childrens_movie, 5)
        self.assertEqual(rental.get_price(), 4.5)
        rental = Rental(self.regular_movie, 2)
        self.assertEqual(rental.get_price(), 2.0)
        rental = Rental(self.regular_movie, 4)
        self.assertEqual(rental.get_price(), 5.0)

    def test_rental_points(self):
        """Test frequent renter points calculation."""
        # Start with 0 points
        frequent_renter_points = 0

        # New release earns 1 point per day
        rental = Rental(self.new_movie, 1)
        frequent_renter_points += rental.get_rental_points()
        self.assertEqual(frequent_renter_points, 1)  # 1 day = 1 point

        rental = Rental(self.new_movie, 5)
        frequent_renter_points += rental.get_rental_points()
        self.assertEqual(frequent_renter_points, 6)  # 5 days = 5 points + previous 1

        # Regular movie earns 1 point total
        rental = Rental(self.regular_movie, 2)
        frequent_renter_points += rental.get_rental_points()
        self.assertEqual(frequent_renter_points, 7)  # +1 point

        rental = Rental(self.regular_movie, 4)
        frequent_renter_points += rental.get_rental_points()
        self.assertEqual(frequent_renter_points, 8)  # +1 point

        # Children's movie earns 1 point total
        rental = Rental(self.childrens_movie, 3)
        frequent_renter_points += rental.get_rental_points()
        self.assertEqual(frequent_renter_points, 9)  # +1 point

        rental = Rental(self.childrens_movie, 7)
        frequent_renter_points += rental.get_rental_points()
        self.assertEqual(frequent_renter_points, 10)  # +1 point
