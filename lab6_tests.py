import data
import lab6
import unittest
from data import Book
from lab6 import str_translate, swap_case, selection_sort_books, histogram


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    def test_selection_sort_books_1(self):
        books = [Book(title="The Great Gatsby", authors=["F. Scott Fitzgerald"]), Book(title="1984", authors=["George Orwell"]), Book(title="To Kill a Mockingbird", authors=["Harper Lee"])]
        expected = ["1984", "The Great Gatsby", "To Kill a Mockingbird"]
        selection_sort_books(books)
        result = [book.title for book in books]
        self.assertEqual(result, expected)

    def test_selection_sort_books_2(self):
        books = []
        expected = []
        selection_sort_books(books)
        result = [book.title for book in books]
        self.assertEqual(result, expected)

    # Part 2
    def test_swap_case_1(self):
        expected = "HeLLo"
        result = swap_case("hEllO")
        self.assertEqual(result, expected)

    def test_swap_case_2(self):
        expected = "CAL poly SLO"
        result = swap_case("cal POLY slo")
        self.assertEqual(result, expected)

    # Part 3
    def test_str_translate_1(self):
        expected = 'xbcdcbx'
        result = str_translate('abcdcba', 'a', 'x')
        self.assertEqual(result, expected)

    def test_str_translate_2(self):
        expected = 'oouuoooi'
        result = str_translate('zzuuzzzi', 'z', 'o')
        self.assertEqual(result, expected)

    # Part 4
    def test_histogram_1(self):
        expected = {"hello": 3, "goodbye": 1}
        result = histogram("hello goodbye hello hello")
        self.assertEqual(result, expected)

    def test_histogram_2(self):
        expected = {"coding": 1, "is": 1, "fun": 1}
        result = histogram("coding is fun")
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
