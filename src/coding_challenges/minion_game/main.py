def do_play_minion_game(s: str, player: str) -> int:
    vowels = set("AEIOU")
    n = len(s)
    score = 0
    for i, ch in enumerate(s):
        if player == "Kevin" and ch in vowels:
            score += n - i
        if player == "Stuart" and ch not in vowels:
            score += n - i
    return score


def play_minion_game(s: str) -> str:
    stuart_score = do_play_minion_game(s, "Stuart")
    kevin_score = do_play_minion_game(s, "Kevin")
    if stuart_score == kevin_score:
        return "Draw"
    elif stuart_score > kevin_score:
        return f"Stuart {stuart_score}"
    else:
        return f"Kevin {kevin_score}"


def minion_game(s: str):
    print(play_minion_game(s))


def test_minion_game():
    assert play_minion_game("BANANA") == "Stuart 12"
    assert play_minion_game("ANANA") == "Kevin 9"

    assert do_play_minion_game("BANANA", "Kevin") == 9
    assert do_play_minion_game("BANANA", "Stuart") == 12


if __name__ == "__main__":
    minion_game("BANANA")
    test_minion_game()
