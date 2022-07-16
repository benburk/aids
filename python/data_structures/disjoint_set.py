class DisjointSet:
    def __init__(self):
        self.parents = {}

    def get_root(self, w):
        words_traversed = []
        while self.parents[w] != w:
            words_traversed.append(w)
            w = self.parents[w]
        for word in words_traversed:
            self.parents[word] = w
        return w

    def add_synonyms(self, w1, w2):
        if w1 not in self.parents:
            self.parents[w1] = w1
        if w2 not in self.parents:
            self.parents[w2] = w2

        w1_root = self.get_root(w1)
        w2_root = self.get_root(w2)
        if w1_root < w2_root:
            w1_root, w2_root = w2_root, w1_root
        self.parents[w2_root] = w1_root

    def are_synonymous(self, w1, w2):
        return self.get_root(w1) == self.get_root(w2)


def test():
    """run test cases"""
    pass


if __name__ == "__main__":
    test()
