# Merge Sort
# CLRS Chapter 2 Page 31

import math


def merge(items, l, m, r):
    """Merges two sorted lists.
    Args:
        items: List of items.
        l: index for the first item.
        m: index for the last item in the left side.
        r: index for the last item.

    Returns:
        The sorted list resulting from merging the two sorted sublists.

    Requires:
        l <= m <= r
        items[l],...,items[m] is a sorted list.
        items[m+1],...,items[r] is a sorted list.
    """

    # Copy the left side from l to m to a new list.
    left = [0 for x in range(m - l + 2)]
    for i in range(l, m + 1):
        left[i - l] = items[i]
    left[m + 1 - l] = float('inf')

    # Copy the right side from m+1 to r to a new list.
    right = [0 for x in range(r - m + 1)]
    for j in range(m + 1, r + 1):
        right[j - (m + 1)] = items[j]
    right[r + 1 - (m + 1)] = float('inf')

    i = 0
    j = 0
    for k in range(l, r + 1):
        if left[i] <= right[j]:
            items[k] = left[i]
            i = i + 1
        else:
            items[k] = right[j]
            j = j + 1


def merge_sort_helper(items, l, r):
    if l < r:
        m = (l + r) / 2
        merge_sort_helper(items, l, m)
        merge_sort_helper(items, m + 1, r)
        merge(items, l, m, r)
    return items


def merge_sort(items):
    """Sorts a list of items.

    Uses merge sort to sort the list items.
    
    Args:
        items: A list of items.

    Returns:
        The sorted list of items. 
    """

    return merge_sort_helper(items, 0, len(items) - 1)
