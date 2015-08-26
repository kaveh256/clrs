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

    num = len(items)
    for j in range(1, num):
        key = items[j]

        # Insert items[j] into the sorted sequence items[1..j-1]
        i = j - 1
        while i >= 0 and items[i] > key:
            items[i + 1] = items[i]
            i = i - 1
        items[i + 1] = key

    return items
