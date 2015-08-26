from selection_sort import selection_sort

import unittest


class SelectionSortTests(unittest.TestCase):
    def test_reverse_order(self):
        self.assertEqual(selection_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]),
                         [1, 2, 3, 4, 5, 6, 7, 8, 9])


def main():
    unittest.main()


if __name__ == '__main__':
    main()
