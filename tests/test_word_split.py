__author__ = 'Mihail Mihaylov'
from src.algorithms.strings.word_split import word_split


def test_word_split_basic() -> None:
    assert word_split("helloworld", {"hello", "world"}) == ["hello", "world"]
