from square_matrix_multiply import square_matrix_multiply

import unittest


class SquareMatrixMultiplyTests(unittest.TestCase):
    def test_2by2(self):
        a = [[2, 1], [1, 2]]
        b = [[1, 2], [2, 1]]
        c = [[4, 5], [5, 4]]
        self.assertEqual(square_matrix_multiply(a, b), c)

    def test_3by3(self):
        a = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
        b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        c = [[90, 114, 138], [54, 69, 84], [18, 24, 30]]
        self.assertEqual(square_matrix_multiply(a, b), c)

    def test_noncommunicative(self):
        a = [[1, 1], [0, 1]]
        b = [[0, 1], [0, 1]]
        c = [[0, 2], [0, 1]]
        self.assertEqual(square_matrix_multiply(a, b), c)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
