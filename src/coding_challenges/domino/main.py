import re

from pydantic import BaseModel, Field


class Tile(BaseModel):
    left: int = Field(ge=1, le=6)
    right: int = Field(ge=1, le=6)


class DominoTileChain(BaseModel):
    tiles: list[Tile]


def build_domino_tile_chain_from_string(tile_chain_string: str) -> DominoTileChain:
    if tile_chain_string == "":
        return DominoTileChain(tiles=[])

    if not re.match(r"^[1-6]-[1-6](,[1-6]-[1-6])*$", tile_chain_string):
        raise ValueError("Invalid tile chain string format")

    tiles = [Tile(left=int(tile[0]), right=int(tile[1])) for tile in re.findall(r"([1-6])-([1-6])", tile_chain_string)]
    return DominoTileChain(tiles=tiles)


def domino(S: str):
    chain_tile = build_domino_tile_chain_from_string(S)

    if len(chain_tile.tiles) == 0:
        return 0

    current_match_count = 1
    max_match_count = 1
    for i in range(len(chain_tile.tiles) - 1):
        left_tile = chain_tile.tiles[i]
        right_tile = chain_tile.tiles[i + 1]
        if left_tile.right == right_tile.left:
            current_match_count += 1
        else:
            current_match_count = 1
        max_match_count = max(max_match_count, current_match_count)

    return max_match_count


def test_domino():
    assert domino("") == 0
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
