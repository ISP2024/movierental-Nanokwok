import re
import unittest
from customer import Customer
from rental import Rental
from movie import Movie


class CustomerTest(unittest.TestCase):
    """ Tests of the Customer class"""

    def setUp(self):
        """Test fixture contains:

        c = a customer
    	movies = list of some movies
    	"""
        self.c = Customer("Movie Mogul")
        self.new_movie = Movie("Mulan", 2024, ["Action"])  # New release
        self.regular_movie = Movie("CitizenFour", 2020, ["Drama"])  # Regular movie
        self.childrens_movie = Movie("Frozen", 2013, ["Children"])  # Children's movie

    @unittest.skip("No convenient way to test")
    def test_billing(self):
        # no convenient way to test billing since its buried in the statement() method.
        pass

    def test_statement(self):
        stmt = self.c.statement()
        # get total charges from statement using a regex
        pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
        matches = re.match(pattern, stmt, flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("0.00", matches[1])
        # add a rental
        self.c.add_rental(Rental(self.new_movie, 4))  # days
        stmt = self.c.statement()
        matches = re.match(pattern, stmt.replace('\n', ''), flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("12.00", matches[1])

    def test_total_amount(self):
        """Test total_amount calculation for multiple rentals."""

        # No rentals, total should be 0
        self.assertEqual(self.c.total_amount(), 0.0)

        # New release for 4 days = 12
        self.c.add_rental(Rental(self.new_movie, 4))
        self.assertEqual(self.c.total_amount(), 12.0)

        # Regular movie for 3 days = 3.5
        self.c.add_rental(Rental(self.regular_movie, 3))
        self.assertEqual(self.c.total_amount(), 12.0 + 3.5)

        # Children's movie for 5 days = 4.5
        self.c.add_rental(Rental(self.childrens_movie, 5))
        self.assertEqual(self.c.total_amount(), 12.0 + 3.5 + 4.5)

    def test_total_rental_points(self):
        """Test total rental points calculation for multiple rentals."""

        # No rentals, total points should be 0
        self.assertEqual(self.c.total_rental_points(), 0)

        # Add new release rental for 4 days
        rental_new_release = Rental(self.new_movie, 4)  # 4 points for 4 days
        self.c.add_rental(rental_new_release)
        self.assertEqual(self.c.total_rental_points(), 4)  # 4 points

        # Add regular movie rental for 3 days
        rental_regular = Rental(self.regular_movie, 3)  # 1 point for any rental
        self.c.add_rental(rental_regular)
        self.assertEqual(self.c.total_rental_points(), 4 + 1)  # 5 points

        # Add children's movie rental for 5 days
        rental_childrens = Rental(self.childrens_movie, 5)  # 1 point for any rental
        self.c.add_rental(rental_childrens)
        self.assertEqual(self.c.total_rental_points(), 5 + 1)  # 6 points
