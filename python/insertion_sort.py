# Insertion Sort
# CLRS Chapter 2 Page 18


def insertion_sort(items):
    """Sorts a list of items.

    Uses inserstion sort to sort the list items.
    
    Args:
        items: A list of items.

    Returns:
        The sorted list of items. 
    """

    for j in range(1, len(items)):
        key = items[j]

        # Insert items[j] into the sorted sequence items[0..j-1]
        i = j - 1
        while 0 <= i and key < items[i]:
            items[i + 1] = items[i]
            i = i - 1
        items[i + 1] = key

    return items
