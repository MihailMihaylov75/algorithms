# Algorithms in Python

Clean, portfolio-ready implementations of classic algorithms and data structures with type hints, docstrings, and focused tests (1 behavior = 1 assert). The project follows a modern `src/` layout and includes linting, typing, and coverage.

## Features
- Clear module headers (`Problem / Examples / Notes`)
- PEP 8 + type hints throughout
- Pytest tests with minimal assertions and fixtures
- Linting (ruff), static typing (mypy), coverage (coverage.py)
- CI-ready (GitHub Actions example provided)

## Requirements
- Python 3.11+
- See `requirements.txt` for tooling (pytest, coverage, ruff, mypy, pylint)


## Project Structure

Below is the high-level layout (key files only). Ellipses mean additional files may exist.

```text
.
├─ README.md
├─ requirements.txt
├─ pytest.ini
├─ mypy.ini
├─ ruff.toml
├─ .coveragerc
├─ .gitignore
├─ .github/
│  └─ workflows/
│     └─ ci.yml
├─ src/
│  └─ algorithms/
│     ├─ arrays/
│     │  ├─ array_pair_sum.py
│     │  ├─ largest_contiguous_sum.py
│     │  └─ missing_element.py
│     ├─ numbers/
│     │  ├─ factorial.py
│     │  ├─ fibonacci.py
│     │  ├─ recursive_sum.py
│     │  ├─ sum_of_digits.py
│     │  └─ coin_change_min.py
│     ├─ strings/
│     │  ├─ balance_parentheses.py
│     │  ├─ sentence_reversal.py
│     │  ├─ string_compression.py
│     │  ├─ unique_characters.py
│     │  ├─ word_split.py
│     │  └─ reverse_string_recursive.py
│     ├─ structures/
│     │  ├─ stack.py
│     │  ├─ queue.py
│     │  ├─ deque.py
│     │  ├─ queue2stack.py
│     │  ├─ linked_list.py
│     │  └─ binary_tree.py
│     └─ patterns/
│        └─ access_control.py
└─ tests/
   ├─ test_array_pair_sum.py
   ├─ test_largest_contiguous_sum.py
   ├─ test_missing_element.py
   ├─ test_factorial.py
   ├─ test_fibonacci.py
   ├─ test_recursive_sum.py
   ├─ test_sum_of_digits.py
   ├─ test_balance_parentheses.py
   ├─ test_sentence_reversal.py
   ├─ test_string_compression.py
   ├─ test_unique_characters.py
   ├─ test_word_split.py
   ├─ test_stack.py
   ├─ test_queue.py
   ├─ test_deque.py
   ├─ test_queue2stack.py
   ├─ test_linked_list.py
   └─ test_binary_tree.py
```




## Quickstart

### Setup (Windows)
```bash
python -m venv .venv && .\.venv\Scripts\activate
pip install -r requirements.txt
```
### Setup (Linux/macOS)
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

### Quality & Tests
- ruff format .
- ruff check .
- mypy src
- pytest -q
- coverage run -m pytest && coverage report -m


## Algorithms Index

| Category   | Problem                         | File                                              | Time                 | Space  |
|------------|----------------------------------|---------------------------------------------------|----------------------|--------|
| Arrays     | Pair Sum (unique pairs)          | `arrays/array_pair_sum.py`                        | O(n)                 | O(n)   |
| Arrays     | Missing Element (2 ways)         | `arrays/missing_element.py`                       | O(n log n) / O(n)    | O(n)   |
| Arrays     | Max Contiguous Sum (Kadane)      | `arrays/largest_contiguous_sum.py`                | O(n)                 | O(1)   |
| Numbers    | Factorial (iter/rec)             | `numbers/factorial.py`                            | O(n)                 | O(1)/O(n) |
| Numbers    | Fibonacci (iter/rec/gen/seq)     | `numbers/fibonacci.py`                            | O(n) / exponential   | O(1)/O(n) |
| Numbers    | Recursive Sum 1..n               | `numbers/recursive_sum.py`                        | O(n)                 | O(n)   |
| Numbers    | Sum of Digits                    | `numbers/sum_of_digits.py`                        | O(d)                 | O(1)   |
| Numbers    | Coin Change (min, memo)          | `numbers/coin_change_min.py`                      | ~O(T·k) (memo)       | O(T)   |
| Strings    | Balanced Parentheses             | `strings/balance_parentheses.py`                  | O(n)                 | O(n)   |
| Strings    | Sentence Reversal                | `strings/sentence_reversal.py`                    | O(n)                 | O(n)   |
| Strings    | String Compression (RLE)         | `strings/string_compression.py`                   | O(n)                 | O(n)   |
| Strings    | Unique Characters                | `strings/unique_characters.py`                    | O(n)                 | O(n)   |
| Strings    | Word Split (DP)                  | `strings/word_split.py`                           | O(n²)                | O(n)   |
| Strings    | Reverse String (recursive)       | `strings/reverse_string_recursive.py`             | O(n)                 | O(n)   |
| Structures | Stack                            | `structures/stack.py`                             | O(1) ops             | O(n)   |
| Structures | Queue (list-based)               | `structures/queue.py`                             | enqueue O(n), dequeue O(1) | O(n) |
| Structures | Deque (list-based)               | `structures/deque.py`                             | add rear O(1), add front O(n) | O(n) |
| Structures | Queue via Two Stacks             | `structures/queue2stack.py`                       | amortized O(1)       | O(n)   |
| Structures | Linked List + ops                | `structures/linked_list.py`                       | O(n)                 | O(1)   |
| Structures | Binary Tree + inorder            | `structures/binary_tree.py`                       | O(n)                 | O(h)   |
| Patterns   | Access Control Decorator         | `patterns/access_control.py`                      | O(1)                 | O(1)   |

> Note: `strings/string_compression.py` also includes `string_compression()` with legacy *total-counts-per-char* behavior.


## Contributing (Definition of Done)
- Module header has **Problem / Examples / Notes**
- Single responsibility; clear naming
- Type hints + docstrings
- Tests: **1 behavior = 1 assert**; use `pytest.raises` for exceptions
- Lint/typing/tests pass (`ruff`, `mypy`, `pytest`)
- Coverage ≥ 90% and entry added to **Algorithms Index**

