# Linear Search
# CLRS Chapter 2 Page 22


def linear_search(x, items):
    """Searches for an item in a list of items.

    Uses linear search to find the index of x in the list items.
    
    Args:
        x: An item.
        items: A list of items.

    Returns:
        The index of x if it is in the list items,
        otherwise None.
    """

    for i in range(1, len(items)):
        if x == items[i]:
            return i
    return None
