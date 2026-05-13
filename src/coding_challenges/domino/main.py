# -*- coding: utf-8 -*-


def domino(S):
    max_count = 0
    if S is not None:
        tiles = S.split(",")
        ccount = 0
        for i in range(0, len(tiles)):
            cur_tile = tiles[i].split("-")
            if i < len(tiles) - 1:
                next_tile = tiles[i + 1].split("-")
                if cur_tile[1] == next_tile[0]:
                    ccount += 1
                else:
                    ccount = 0
            if ccount > max_count:
                max_count = ccount
        max_count = max_count + 1
    return max_count


def test_domino():
    assert domino("2-4,4-1") == 2
    assert domino("1-1,3-5,5-2,2-3,2-4") == 3
    assert domino("1-1") == 1
    assert domino("1-2,1-2") == 1
    assert domino("3-2,2-1,1-4,4-4,5-4,4-2,2-1") == 4
    assert domino("5-5,5-5,4-4,5-5,5-5,5-5,5-5,5-5,5-5,5-5") == 7
    assert domino("1-1,3-5,5-5,5-4,4-2,1-3") == 4
    assert domino("1-2,2-2,3-3,3-4,4-5,1-1,1-2") == 3


if __name__ == "__main__":
    test_domino()
    print("All tests passed!")
