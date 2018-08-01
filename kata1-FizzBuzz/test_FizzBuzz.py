import unittest
from FizzBuzz import FizzBuzz

class FizzBuzzTest(unittest.TestCase):
    def test_empty_list_is_returned_when_input_array_is_empty(self):
        fizz_buzz = FizzBuzz()

        result = fizz_buzz.fizz_buzz([])

        self.assertEqual([], result)

    def test_correct_string_is_returned_for_list_of_numbers(self):
        fizz_buzz = FizzBuzz()

        result = fizz_buzz.fizz_buzz([1, 3, 3, 5, 15, 30, 4, 8, 10])

        self.assertEqual(["1", "Fizz", "Fizz", "Buzz", "FizzBuzz", "FizzBuzz", "4", "8", "Buzz", ], result)
