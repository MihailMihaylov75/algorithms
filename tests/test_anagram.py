# tests/test_anagram.py
import pytest

from src.algorithms.strings.anagram import is_anagram, is_anagram2

CANDIDATES = (is_anagram, is_anagram2)


@pytest.mark.unit
@pytest.mark.parametrize("func", CANDIDATES)
@pytest.mark.parametrize(
    ("a", "b"),
    [
        ("listen", "silent"),
        ("rail safety", "fairy tales"),
        ("Dormitory", "Dirty room"),
        ("123", "321"),
        ("ab,", "a,b"),
    ],
)
def test_true_basic_cases(func, a: str, b: str) -> None:
    assert func(a, b)


@pytest.mark.unit
@pytest.mark.parametrize("func", CANDIDATES)
@pytest.mark.parametrize(
    ("a", "b"),
    [
        ("hello", "bello"),
        ("aaab", "aaac "),  # trailing space ignored → same length, BUT different multiset (b vs c)
        ("ab", "a"),        # fast-fail by length
        ("ab", "abc"),      # fast-fail by length
    ],
)
def test_false_basic_cases(func, a: str, b: str) -> None:
    assert not func(a, b)


@pytest.mark.unit
@pytest.mark.parametrize("func", CANDIDATES)
@pytest.mark.parametrize(
    ("a", "b"),
    [
        ("a b", "ab"),      # spaces are ignored
        ("rail  safety", "fairy  tales"),
    ],
)
def test_ignores_spaces(func, a: str, b: str) -> None:
    assert func(a, b)


@pytest.mark.unit
@pytest.mark.parametrize("func", CANDIDATES)
@pytest.mark.parametrize(
    ("a", "b"),
    [
        ("a\tb", "ab"),     # tabs are NOT removed by current spec (only spaces are)
        ("a\nb", "ab"),
    ],
)
def test_does_not_ignore_tabs_or_newlines(func, a: str, b: str) -> None:
    assert not func(a, b)


@pytest.mark.unit
@pytest.mark.parametrize("func", CANDIDATES)
@pytest.mark.parametrize(
    ("a", "b"),
    [
        ("", ""),           # empty vs empty
        (" ", ""),          # space removed → both empty after normalization
    ],
)
def test_empty_and_space_equivalence(func, a: str, b: str) -> None:
    assert func(a, b)


@pytest.mark.unit
@pytest.mark.parametrize("func", CANDIDATES)
@pytest.mark.parametrize(
    ("a", "b"),
    [
        ("binary", "brainy"),
        ("conversation", "voices rant on"),
    ],
)
def test_symmetry(func, a: str, b: str) -> None:
    assert func(a, b) == func(b, a)


@pytest.mark.unit
@pytest.mark.parametrize("func", CANDIDATES)
@pytest.mark.parametrize(
    "s",
    [
        "",
        "   ",
        "Listen",
        "a,b1",
        "rail safety",
    ],
)
def test_reflexive(func, s: str) -> None:
    assert func(s, s)


@pytest.mark.unit
@pytest.mark.parametrize("func", CANDIDATES)
def test_unicode_sharp_s_current_behavior(func) -> None:
    # With simple lowercasing, "straße" != "strasse" (length differs and ß != ss).
    # This documents current behavior; if you switch to casefold() later, update this test.
    assert not func("straße", "strasse")
