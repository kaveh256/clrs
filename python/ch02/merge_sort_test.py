from merge_sort import merge_sort

import unittest


class MergeSortTests(unittest.TestCase):
    def test_reverse_order(self):
        items = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        sorted_items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(sorted_items, merge_sort(items))


def main():
    unittest.main()


if __name__ == '__main__':
    main()
