"""Generate all permutations of n objects."""


from typing import Iterable


def permute2(lst: list[int], n: int) -> Iterable[list[int]]:
    """simpler to understand
    fix element at end
    permute the rest
    """

    if n == 1:
        yield lst
        return
    for i in range(n):
        lst[i], lst[n - 1] = lst[n - 1], lst[i]
        yield from permute2(lst, n - 1)
        lst[i], lst[n - 1] = lst[n - 1], lst[i]


def permute(lst: list[int], n: int) -> Iterable[list[int]]:
    """Heap's algorithm
    time: O(n!)
    """
    if n == 1:
        yield lst
        return

    for i in range(n):
        yield from permute(lst, n - 1)
        if n % 2:
            lst[0], lst[n - 1] = lst[n - 1], lst[0]
        else:
            lst[i], lst[n - 1] = lst[n - 1], lst[i]


for p in permute([1, 2, 3, 4], 4):
    print(p)
print("")

for p in permute2([1, 2, 3, 4], 4):
    print(p)


# print(sorted([str(x) for x in permute([1, 2, 3, 4], 4)]))
