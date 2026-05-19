from pysandbox.simple_tokenizer import top_words


def test_top_words_empty_comments():
    assert top_words([]) == []


def test_top_words_single_comment():
    comments = ["This is a great article!"]
    assert top_words(comments) == [("great", 1), ("article", 1)]


def test_top_words_multiple_comments():
    comments = [
        "I love this product, it is amazing.",
        "The service was terrible and slow.",
        "What an incredible experience, highly recommend!",
    ]
    assert top_words(comments, top_n=3) == [("love", 1), ("product", 1), ("amazing", 1)]


def test_top_words_top_n_limit():
    comments = [
        "apple apple apple",
        "banana banana",
        "cherry",
    ]
    assert top_words(comments, top_n=2) == [("apple", 3), ("banana", 2)]


def test_top_words_case_insensitive_and_punctuation():
    comments = [
        "Hello, World!",
        "hello world",
    ]
    assert top_words(comments) == [("hello", 2), ("world", 2)]
