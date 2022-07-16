def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if target > arr[mid]:
            low = mid + 1
        elif target < arr[mid]:
            high = mid - 1
        else:
            return arr[mid]

    # target not found, return nearest value
    if low >= len(arr):
        return arr[high]
    return arr[low if arr[low] - target < target - arr[high] else high]


def solve(stores, houses):
    return [binary_search(sorted(stores), house) for house in houses]


def main():
    stores = [1, 5, 20, 11, 16]
    houses = [5, 10, 17]

    # print(solve(stores, houses))
    # print(solve([3,1], [2]))
    print(solve([2], [0]))


if __name__ == "__main__":
    main()
