import string
from collections import Counter

stopwords = {"the", "a", "is", "it", "and", "to", "i", "this", "was", "of"}


def get_words(text):
    # 1. Lowercase
    text = text.lower()
    # 2. Explicitly remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))
    # 3. Tokenize
    tokens = text.split()
    # 4. Filter stopwords
    return [w for w in tokens if w not in stopwords]


def top_words(comments, top_n=10):
    words = []
    for comment in comments:
        words.extend(get_words(comment))

    return Counter(words).most_common(top_n)


if __name__ == "__main__":
    comments = [
        "This is a great article!",
        "I love this product, it is amazing.",
        "The service was terrible and slow.",
        "What an incredible experience, highly recommend!",
        "It was okay, nothing special though.",
        "I would definitely recommend this product.",
        "Love it!",
    ]
    print(top_words(comments, top_n=10))
