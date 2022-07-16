"""
Synonymous queries
https://medium.com/@alexgolec/google-interview-problems-synonymous-queries-36425145387c

"""
from collections import defaultdict


def solve(synonym_words, queries):
    """
    linear time
    """
    synonyms = defaultdict(set)
    for word1, word2 in synonym_words:
        synonyms[word1].add(word2)

    result = []

    for query1, query2 in queries:
        query1, query2 = query1.split(), query2.split()
        if len(query1) != len(query2):
            result.append(False)
            continue

        result.append(
            all(
                w1 == w2
                or (
                    (w1 in synonyms and w2 in synonyms[w1])
                    or (w2 in synonyms and w1 in synonyms[w2])
                )
                for w1, w2 in zip(query1, query2)
            )
        )
    return result


def test():
    """run test cases"""
    synonyms = [("rate", "ratings"), ("approval", "popularity")]

    queries = [
        ("obama approval rate", "obama popularity ratings"),
        ("obama approval rates", "obama popularity ratings"),
        ("obama approval rate", "popularity ratings obama"),
    ]
    print(solve(synonyms, queries))


if __name__ == "__main__":
    test()
