from binary_search import binary_search

import unittest


class BinarySearchTests(unittest.TestCase):
    def test_simple(self):
        items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        x = 5
        self.assertEqual(binary_search(x, items), 4)

    def test_not_in_the_list(self):
        items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        x = 0
        self.assertEqual(binary_search(x, items), None)

    def test_first_item(self):
        items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        x = 1
        self.assertEqual(binary_search(x, items), 0)

    def test_last_item(self):
        items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        x = 9
        self.assertEqual(binary_search(x, items), 8)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
