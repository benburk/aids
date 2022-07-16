"""
The stable marriage problem (also stable matching problem or SMP) is the
problem of finding a stable matching between two equally sized sets of
elements given an ordering of preferences for each element

References
- https://en.wikipedia.org/wiki/Stable_marriage_problem
- https://tylermoore.utulsa.edu/courses/cse3353/s14/slides/l02-handout.pdf
"""


def gale(guy_pref, girl_pref):
    # preprocessing
    ## build the rank dictionary
    rank = {}
    for woman in girl_pref:
        rank[woman] = {}
        i = 0
        for man in girl_pref[woman]:
            rank[woman][man] = i
            i += 1
    print(rank)
    ## create a ”pointer” to the next woman to propose
    prefptr = {}
    for man in guy_pref:
        prefptr[man] = 0
    freemen = list(guy_pref)
    numpartners = len(freemen)
    pairs = {}  # build dictionary to store engagements

    while freemen:
        man = freemen.pop()
        if prefptr[man] > numpartners:
            continue
        # get the highest ranked woman that has not yet been proposed to
        woman = guy_pref[man][prefptr[man]]
        prefptr[man] += 1
        if woman not in pairs:
            pairs[woman] = man
        else:
            mprime = pairs[woman]
            if rank[woman][man] < rank[woman][mprime]:
                pairs[woman] = man
                freemen.append(mprime)
            else:
                freemen.append(man)
    return pairs


def test2():
    guy_pref = {
        "xavier": ["amy", "bertha", "clare"],
        "yancey": ["bertha", "amy", "clare"],
        "zeus": ["amy", "bertha", "clare"],
    }
    girl_pref = {
        "amy": ["yancey", "xavier", "zeus"],
        "bertha": ["xavier", "yancey", "zeus"],
        "clare": ["xavier", "yancey", "zeus"],
    }

    print(gale(guy_pref, girl_pref))


def gale2(men, women, pref):
    # preprocessing
    ## build the rank dictionary
    rank = {}
    for woman in women:
        rank[woman] = {}
        i = 0
        for man in pref[woman]:
            rank[woman][man] = i
            i += 1
    print(rank)
    ## create a ”pointer” to the next woman to propose
    prefptr = {}
    for man in men:
        prefptr[man] = 0
    freemen = list(men)
    numpartners = len(men)
    pairs = {}  # build dictionary to store engagements

    while freemen:
        man = freemen.pop()
        if prefptr[man] > numpartners:
            continue
        # get the highest ranked woman that has not yet been proposed to
        woman = pref[man][prefptr[man]]
        prefptr[man] += 1
        if woman not in pairs:
            pairs[woman] = man
        else:
            mprime = pairs[woman]
            if rank[woman][man] < rank[woman][mprime]:
                pairs[woman] = man
                freemen.append(mprime)
            else:
                freemen.append(man)
    return pairs


def test():
    men = ["xavier", "yancey", "zeus"]
    women = ["amy", "bertha", "clare"]
    pref = {
        "xavier": ["amy", "bertha", "clare"],
        "yancey": ["bertha", "amy", "clare"],
        "zeus": ["amy", "bertha", "clare"],
        "amy": ["yancey", "xavier", "zeus"],
        "bertha": ["xavier", "yancey", "zeus"],
        "clare": ["xavier", "yancey", "zeus"],
    }

    print(gale2(men, women, pref))


if __name__ == "__main__":
    test2()
