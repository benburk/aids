from collections import defaultdict


def remove_islands(matrix: list[list[int]]):
    n_rows, n_cols = len(matrix), len(matrix[0])

    def find_component(i, j):
        """do a depth first search in grid at (i,j)"""
        stack = [(i, j)]
        component = set()
        connected_to_border = False

        while stack:
            node = stack.pop()
            if node not in component:
                component.add(node)
                i, j = node

                for row, col in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                    if (
                        row in range(n_rows)
                        and col in range(n_cols)
                        and matrix[row][col] == 1
                    ):
                        stack.append((row, col))
                        if row in (0, n_rows - 1) or col in (0, n_cols - 1):
                            connected_to_border = True
        return component, connected_to_border

    seen = set()
    remove_us = []
    for i in range(1, n_rows - 1):
        for j in range(1, n_cols - 1):
            if (i, j) not in seen and matrix[i][j] == 1:
                component, edged = find_component(i, j)
                if not edged:
                    seen.update(component)
                    remove_us.extend(component)

    print(remove_us)


def main():
    board = "100000\n" "010111\n" "001010\n" "110010\n" "101100\n" "100001"

    board = [[int(c) for c in row] for row in board.split("\n")]
    from pprint import pprint

    pprint(board)
    remove_islands(board)


if __name__ == "__main__":
    main()
