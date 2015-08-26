import heap

import unittest


class HeapTests(unittest.TestCase):
    def test_simple(self):
        h = []
        self.assertEqual(0, heap.size(h))

        heap.insert(h, 100)
        self.assertEqual(1, heap.size(h))
        self.assertEqual(100, heap.top(h))

        heap.insert(h, 10)
        self.assertEqual(2, heap.size(h))
        self.assertEqual(100, heap.top(h))

        heap.insert(h, 200)
        self.assertEqual(3, heap.size(h))
        self.assertEqual(200, heap.top(h))

        self.assertEqual(200, heap.remove_top(h))
        self.assertEqual(2, heap.size(h))

        self.assertEqual(100, heap.remove_top(h))
        self.assertEqual(1, heap.size(h))

        self.assertEqual(10, heap.remove_top(h))
        self.assertEqual(0, heap.size(h))


def main():
    unittest.main()


if __name__ == '__main__':
    main()
