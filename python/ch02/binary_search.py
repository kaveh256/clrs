# Binary Search
# CLRS Chapter 2 Page 39
# Ex. 2.3-5


def binary_search_helper(items, l, r, x):
    while l <= r:
        m = (l + r) / 2
        if items[m] == x:
            return m
        elif items[m] < x:
            l = m + 1
        else:
            r = m - 1

    return None


def binary_search(x, items):
    """Searches for an item in a sorted list of items.

    Uses binary search to find the index of x in the list items.
    
    Args:
        x: An item.
        items: A sorted list of items.

    Returns:
        The index of x if it is in the list items,
        otherwise None.
    """
    return binary_search_helper(items, 0, len(items) - 1, x)
