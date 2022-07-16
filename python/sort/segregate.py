"""
sort array of 0s 1s 2s
"""


def segregate(arr):
    """
    O(n*k)
    """
    j = 0
    for check in (0, 1):
        for i in range(j, len(arr)):
            if arr[i] == check:
                arr[i], arr[j] = arr[j], arr[i]  # swap arr[i], arr[j]
                j += 1
    return arr


def main():
    x = [1, 1, 0, 2, 1, 0, 2, 2, 1, 0]
    segregate(x)


if __name__ == "__main__":
    main()
