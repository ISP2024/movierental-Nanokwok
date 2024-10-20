import unittest
from movie import Movie
from pricing import RegularPrice, NewReleasePrice, ChildrenPrice
from rental import price_code_for_movie


class TestPriceCodeForMovie(unittest.TestCase):

    def setUp(self):
        """Set up common test data."""
        self.new_release_movie = Movie("Air", year=2024, genres=["Action"])
        self.children_movie = Movie("Frozen", year=2013, genres=["Children"])
        self.regular_movie = Movie("Bitconned", year=2020, genres=["Drama"])
        self.children_variation_movie = Movie("FrozenII", year=2021, genres=["Childrens"])

    def test_new_release_movie(self):
        price_strategy = price_code_for_movie(self.new_release_movie)
        self.assertIsInstance(price_strategy, NewReleasePrice)

    def test_children_movie(self):
        price_strategy = price_code_for_movie(self.children_movie)
        self.assertIsInstance(price_strategy, ChildrenPrice)

    def test_regular_movie_2020(self):
        price_strategy = price_code_for_movie(self.regular_movie)
        self.assertIsInstance(price_strategy, RegularPrice)


class TestMoviePricing(unittest.TestCase):

    def setUp(self):
        """Set up common test data for pricing."""
        self.new_release_movie = Movie("Air", year=2024, genres=["Action"])
        self.children_movie = Movie("Frozen", year=2013, genres=["Children"])
        self.regular_movie = Movie("Bitconned", year=2020, genres=["Drama"])
        self.children_variation_movie = Movie("FrozenII", year=2021, genres=["Childrens"])

    def test_new_release_price(self):
        price_strategy = price_code_for_movie(self.new_release_movie)
        price = price_strategy.get_price(3)
        self.assertEqual(price, 9.0)

    def test_children_price(self):
        price_strategy = price_code_for_movie(self.children_movie)
        price = price_strategy.get_price(5)
        self.assertEqual(price, 4.5)

    def test_regular_movie_price(self):
        price_strategy = price_code_for_movie(self.regular_movie)
        price = price_strategy.get_price(2)
        self.assertEqual(price, 2.0)
