__author__ = 'Mihail Mihaylov'
from src.algorithms.strings.permutations import permutations


def test_permutations_of_three() -> None:
    assert sorted(permutations("abc")) == sorted(["abc","acb","bac","bca","cab","cba"])
