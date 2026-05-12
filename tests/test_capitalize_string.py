from pysandbox.capitalize_string import capitalize_string


def test_capitalize_string():
    assert (
        capitalize_string("first, solve the problem.then, write the code.")
        == "First, solve the problem. Then, write the code."
    )

    assert capitalize_string("this is a test... and another test.") == "This is a test... And another test."

    assert capitalize_string("aaaaa  bbbbb,ccccc;  ddddd.eeeee") == "Aaaaa bbbbb, ccccc; ddddd. Eeeee"
