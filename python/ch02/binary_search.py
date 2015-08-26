# Binary Search
# CLRS Chapter 2 Page 39
# Ex. 2.3-5


def binary_search(items, x):
    """Searches for an item in a sorted list of items.

    Uses binary search to find the index of x in the list items.
    
    Args:
        items: A sorted list of items.
        x: The item to be searched.


    Returns:
        The index of x if it is in the list items,
        otherwise None.
    """

    l = 0
    r = len(items) - 1
    while l <= r:
        m = (l + r) // 2
        if items[m] == x:
            return m
        elif items[m] < x:
            l = m + 1
        else:
            r = m - 1

    return None
