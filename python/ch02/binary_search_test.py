from binary_search import binary_search

import unittest


class BinarySearchTests(unittest.TestCase):
    def test_simple(self):
        items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        x = 5
        self.assertEqual(4, binary_search(items, x))

    def test_not_in_the_list(self):
        items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        x = 0
        self.assertEqual(None, binary_search(items, x))

    def test_first_item(self):
        items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        x = 1
        self.assertEqual(0, binary_search(items, x))

    def test_last_item(self):
        items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        x = 9
        self.assertEqual(8, binary_search(items, x))


def main():
    unittest.main()


if __name__ == '__main__':
    main()
