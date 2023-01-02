"""find all the connected components in a directed graph."""
from typing import Iterator, TypeVar

T = TypeVar("T")


def connected(graph: dict[T, list[T]]) -> Iterator[list[T]]:
    """Returns an iterator over lists of connected components."""
    seen = set()

    def dfs(node):
        path = []
        stack = [node]
        while stack:
            current = stack.pop()
            if current not in seen:
                seen.add(current)
                path.append(current)
                stack.extend(graph[current])
        return path

    for node in graph:
        if node not in seen:
            yield dfs(node)


def test():
    """run test cases"""
    graph = {
        "a": ["c"],
        "b": ["c", "e"],
        "c": ["a", "b", "d", "e"],
        "d": ["c"],
        "e": ["c", "b"],
        "f": [],
    }
    graph = {"a": ["b"], "b": [], "c": ["d", "e"], "d": [], "e": []}

    print(list(connected(graph)))
    for component in connected(graph):
        print(component)


if __name__ == "__main__":
    test()
