"""
Problem:
Compress a string by counting consecutive repeated characters (run-length encoding).
For example, "AAABCCDDDD" -> "A3B1C2D4". Empty input -> "".

Examples:
    compress_runs("AAABCCDDDD") -> "A3B1C2D4"
    compress_runs("ABA")        -> "A1B1A1"
    compress_runs("")           -> ""

Notes:
- This is classic run-length encoding (RLE) over consecutive runs.
- Time Complexity: O(n)
- Space Complexity: O(n) for the output string

Also provided (legacy behavior):
- string_compression(text): counts total occurrences per character in order of
  first appearance (NOT run-length). Kept for backward compatibility with the
  original repository version.
"""

from __future__ import annotations

from collections import OrderedDict
from typing import Dict, List


def compress_runs(text: str) -> str:
    """
    Compresses the input string by consecutive runs of the same character.

    :param text: Input string (may be empty).
    :return: Run-length encoded string (e.g., "AAB" -> "A2A1B1"?? no → "A2B1").

    The count is always included (even when it equals 1).
    """
    if not text:
        return ""

    parts: List[str] = []
    current_char = text[0]
    count = 1

    for ch in text[1:]:
        if ch == current_char:
            count += 1
        else:
            parts.append(current_char)
            parts.append(str(count))
            current_char = ch
            count = 1

    # flush last run
    parts.append(current_char)
    parts.append(str(count))
    return "".join(parts)


def string_compression(text: str) -> str:
    """
    Legacy compression: counts TOTAL occurrences per character (order of first appearance).
    This is NOT run-length encoding. For example, "ABA" -> "A2B1".

    :param text: Input string (may be empty).
    :return: Concatenation of each distinct character and its total count.
    """
    if not text:
        return ""

    counts: Dict[str, int] = OrderedDict()  # insertion-ordered
    for ch in text:
        counts[ch] = counts.get(ch, 0) + 1

    out_parts: List[str] = []
    for k, v in counts.items():
        out_parts.append(k)
        out_parts.append(str(v))
    return "".join(out_parts)
