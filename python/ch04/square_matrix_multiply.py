# Square Matrix Multiply
# CLRS Chapter 4 Page 75


def square_matrix_multiply(a, b):
    """Multiplies two square matrices.

    Args:
        a: A square matrix.
        b: A square matrix.

    Returns:
        The matrix resulting from multiplying a to b. 
    """

    n = len(a)
    c = [[0 for x in range(n)] for x in range(n)]
    for i in range(n):
        for j in range(n):
            c[i][j] = 0
            for k in range(n):
                c[i][j] = c[i][j] + a[i][k] * b[k][j]

    return c
