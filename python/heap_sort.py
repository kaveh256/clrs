# Heap Sort
# CLRS Chapter 6 Page ??

from heap import build_max_heap
from heap import max_heapify
from heap import _swap


def heap_sort(items):
    """Sorts a list of items.

    Uses heap sort to sort the list items.
    
    Args:
        items: A list of items.

    Returns:
        The sorted list of items. 
    """

    # Build a max heap of items.
    build_max_heap(items)

    n = len(items)
    result = [0 for x in range(n)]
    for i in reversed(range(n)):
        _swap(items, 0, i)
        result[i] = items.pop()
        max_heapify(items, 0)

    return result
