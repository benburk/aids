"""
find all the connected components in a directed graph
"""


def connected(graph):
    """return a list of lists of all connected components"""
    seen = set()

    def bfs(node):
        path = []
        stack = [node]
        while stack:
            current = stack.pop(0)
            if current not in seen:
                seen.add(current)
                path.append(current)
                stack.extend(graph[current])
        return path

    for node in graph:
        if node not in seen:
            yield bfs(node)


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
