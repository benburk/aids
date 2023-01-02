"""
Quick sort
Links:
    https://en.wikipedia.org/wiki/Quicksort
"""


def quicksort_recursive(arr):
    """Quick sort recursive.
    Given indexable and slicable iterable, return a sorted list
    """
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    below = [i for i in arr[1:] if i < pivot]
    above = [i for i in arr[1:] if i >= pivot]
    return quicksort_recursive(below) + [pivot] + quicksort_recursive(above)


def partition(array: list[int], begin: int, end: int) -> int:
    pivot = array[end]
    wall = begin - 1
    for i in range(begin, end):
        if array[i] <= pivot:
            wall += 1
            array[wall], array[i] = array[i], array[wall]
    array[wall + 1], array[end] = array[end], array[wall + 1]
    return wall + 1


def quicksort(array: list[int], begin: int, end: int):
    """In-place quick sort."""
    if begin < end:
        i = partition(array, begin, end)
        quicksort(array, begin, (i - 1))
        quicksort(array, (i + 1), end)


def main():
    """Main function"""
    array = [9, 5, 4, 8, 2, 0, 7, 6]
    quicksort(array, 0, len(array) - 1)
    print(array)


if __name__ == "__main__":
    main()
