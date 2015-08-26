from linear_search import linear_search

import unittest


class InsertionSortTests(unittest.TestCase):
    def test_simple(self):
        items = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        x = 5
        self.assertEqual(linear_search(x, items), 4)

    def test_not_in_the_list(self):
        items = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        x = 0
        self.assertEqual(linear_search(x, items), None)


def main():
    unittest.main()


if __name__ == '__main__':
    main()