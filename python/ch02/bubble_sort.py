# Bubble Sort
# CLRS Chapter 2 Page 40
# Ex. 2-2


def bubble_sort(items):
    """Sorts a list of items.

    Uses inserstion sort to sort the list items.
    
    Args:
        items: A list of items.

    Returns:
        The sorted list of items. 
    """

    for i in range(1, len(items)):
        for j in range(1, len(items)):
            if items[j] < items[j - 1]:
                temp = items[j]
                items[j] = items[j - 1]
                items[j - 1] = temp

    return items
