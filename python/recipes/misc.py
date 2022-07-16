def flatten_json(y, prefix=""):
    """flatten json/dict containing inner dicts and lists"""
    out = {}

    def flatten(element, name=""):
        if isinstance(element, dict):
            for a in element:
                flatten(element[a], name + a + "_")
        elif isinstance(element, list):
            for i, a in enumerate(element):
                flatten(a, name + str(i) + "_")
        else:
            out[name[:-1]] = element

    flatten(y, prefix)
    return out


def add_vectors(vec1, vec2, low=0, high=100):
    """saturating vector addition"""
    return [max(min(i + j, high), low) for i, j in zip(vec1, vec2)]


def construct_function(mapping: dict[int, int]) -> str:
    """Construct a mathematical expression for an injective function represented as a
    dictionary.

    Example:
        >>> construct_function({0: 0, 1: 2, -1: 1})
        1/2n(3n+1)

    :param mapping: A dictionary representing an injective function
    :return: An unsimplified polynomial expression
    """
    terms = []
    for i, j in mapping.items():
        coeff = 1
        term = ""
        for k in mapping:
            if i != k:
                coeff *= i - k
                term += f"(n-{k})"
        term += f"({j}/{coeff})"
        terms.append(term)
    return "+".join(terms)


def hanoi(n_discs: int) -> None:
    """Display solution to towers of hanoi puzzle.

    The puzzle has 3 posts indexed as 0,1,2. The discs start on post 0.

    :param n_discs: The number of discs
    """
    for i in range(1, 2 ** n_discs):
        print(f"move a disc from {(i & (i - 1)) % 3} to {((i | i - 1) + 1) % 3}")
