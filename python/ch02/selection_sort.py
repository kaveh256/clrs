# Selection Sort
# CLRS Chapter 2 Page 29
# Ex. 2.2-2


def selection_sort(items):
    """Sorts a list of items.

    Uses selection sort to sort the list items.
    
    Args:
        items: A list of items.

    Returns:
        The sorted list of items. 
    """

    n = len(items)
    for j in range(n):
        # Find the index of the smallest item in the range(j,n)
        i_min = j
        for i in range(j + 1, n):
            if (items[i] < items[i_min]):
                i_min = i

        # Swap the items at j and i_min if needed.
        if i_min != j:
            temp = items[j]
            items[j] = items[i_min]
            items[i_min] = temp

    return items
