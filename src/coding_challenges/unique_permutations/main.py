import itertools


def unique_permutations(input: int) -> int:
    s = str(input)
    ps = set(itertools.permutations(s, len(s)))
    ps = list(itertools.filterfalse(lambda x: len(x) > 1 and x[0] == "0", ps))
    return len(ps)


def test_unique_permutations():
    assert unique_permutations(0) == 1
    assert unique_permutations(1213) == 12
    assert unique_permutations(123) == 6
    assert unique_permutations(100) == 1
    assert unique_permutations(11) == 1


if __name__ == "__main__":
    test_unique_permutations()
    print("All tests passed!")
