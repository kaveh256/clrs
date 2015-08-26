# Heap
# CLRS Chapter 6 Page 152, 154, 157, 163, 164
# For CPython's implementation see:
#   https://hg.python.org/cpython/file/2.7/Lib/heapq.py


def max_heapify(heap, node):
    left = _left(node)
    right = _right(node)
    largest = node
    if left < size(heap) and heap[largest] < heap[left]:
        largest = left
    if right < size(heap) and heap[largest] < heap[right]:
        largest = right
    if largest != node:
        _swap(heap, node, largest)
        max_heapify(heap, largest)


def build_max_heap(heap):
    # Run max_heapify buttom-up.
    for node in reversed(range((len(heap) - 1) // 2 + 1)):
        max_heapify(heap, node)
    return heap


def remove_last(heap):
    return heap.pop()


def remove(heap, node):
    if node >= size(heap):
        raise Exception("Node does not exist in the heap.")
    # Swap the item with the last item if needed.
    last = size(heap) - 1
    if node != last:
        _swap(heap, node, last)

    # Remove the last item.
    item = remove_last(heap)

    # Fix the heap property.
    max_heapify(heap, node)

    return item


def remove_top(heap):
    return remove(heap, _root())


def decrease_key(heap, node, item):
    if heap[node] < item:
        raise Exception("The new key is lsrger than the current key.")

    heap[node] = item

    _move_down(heap, node)


def increase_key(heap, node, item):
    if item < heap[node]:
        raise Exception("The new key is smaller than the current key.")

    heap[node] = item

    _move_up(heap, node)


def insert(heap, item):
    # Put the item at the end.
    node = size(heap)
    heap.append(item)

    _move_up(heap, node)


def top(heap):
    """Returns the top item in the heap."""
    return heap[_root()]


def size(heap):
    """The number of items in the heap."""
    return len(heap)


def empty(heap):
    """Check if the heap is empty."""
    return size(heap) == 0


def _swap(heap, i, j):
    """Swaps nodes i and j in heap."""
    heap[i], heap[j] = heap[j], heap[i]


def _parent(node):
    """Parent of a node. The root points to itself."""
    if node == _root():
        return _root()
    return (node + 1) // 2 - 1


def _left(node):
    """The _left child of a node."""
    return 2 * node + 1


def _right(node):
    """The right child of a node."""
    return 2 * node + 2


def _root():
    """Returns the root node."""
    return 0


def _move_down(heap, node):
    # Move down the item as long as needed.
    # This is an iterative version of max_heapify.
    while node < size(heap):
        left = _left(node)
        right = _right(node)
        largest = node
        if left < size(heap) and heap[largest] < heap[left]:
            largest = left
        if right < size(heap) and heap[largest] < heap[right]:
            largest = right
        if largest == node:
            break
        _swap(heap, node, largest)
        node = largest


def _move_up(heap, node):
    # Move up the item as long as needed.
    while node != _root() and heap[_parent(node)] < item:
        _swap(heap, node, _parent(node))
        node = _parent(node)
