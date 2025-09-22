__author__ = 'Mihail Mihaylov'
from src.algorithms.strings.string_compression import compress_runs


def test_runs_basic_mixed() -> None:
    assert compress_runs("AAABCCDDDD") == "A3B1C2D4"


def test_runs_preserves_nonadjacent_order() -> None:
    assert compress_runs("ABA") == "A1B1A1"


def test_runs_handles_singletons() -> None:
    assert compress_runs("abcd") == "a1b1c1d1"


def test_runs_empty_returns_empty() -> None:
    assert compress_runs("") == ""
