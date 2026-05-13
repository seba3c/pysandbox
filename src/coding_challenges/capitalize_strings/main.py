import re


def capitalize_string(S):
    def upper_after_dot(m):
        return m[1] + " " + m[2].strip().capitalize()

    if S is not None:
        # remove leading and trailing spaces
        ss = S.strip()
        # capitalize first letter
        ss = ss.capitalize()
        # replace more than one space by one space
        ss = re.sub(r"\s+", " ", ss)
        # fix . spacing
        ss = re.sub(r"([.])(\s{2,*})", r". \2", ss)
        ss = re.sub(r"([.])(\w+)", r". \2", ss)
        # fix , spacing
        ss = re.sub(r"(,)(\s{2,*})", r", \2", ss)
        ss = re.sub(r"(,)(\w+)", r", \2", ss)
        # fix ; spacing
        ss = re.sub(r"(;)(\s{2,*})", r"; \2", ss)
        ss = re.sub(r"(;)(\w+)", r"; \2", ss)
        # fix : spacing
        ss = re.sub(r"(:)(\s{2,*})", r": \2", ss)
        ss = re.sub(r"(:)(\w+)", r": \2", ss)
        # fix ? spacing
        ss = re.sub(r"(\?)(\s{2,*})", r"? \2", ss)
        ss = re.sub(r"(\?)(\w+)", r"? \2", ss)
        # fix ! spacing
        ss = re.sub(r"(!)(\s{2,*})", r"! \2", ss)
        ss = re.sub(r"(!)(\w+)", r"! \2", ss)
        # upper case after .
        ss = re.sub(r"([.])(\s[a-z]*)", upper_after_dot, ss)

        return ss
    return None


def test_capitalize_string():
    assert (
        capitalize_string("first, solve the problem.then, write the code.")
        == "First, solve the problem. Then, write the code."
    )
    assert capitalize_string("this is a test... and another test.") == "This is a test... And another test."
    assert capitalize_string("aaaaa  bbbbb,ccccc;  ddddd.eeeee") == "Aaaaa bbbbb, ccccc; ddddd. Eeeee"


if __name__ == "__main__":
    test_capitalize_string()
    print("All tests passed!")
