from typing import List, Tuple


def is_valid(suite: List[int], number: int) -> bool:
    suite = list(suite)
    for i, n in enumerate(suite):
        s = suite.copy()
        s.pop(i)
        if number - n in s:
            return True
    return False


def _find_first_non_valid_number(numbers: List[int], preamble: int) -> int:
    for i, n in enumerate(numbers[preamble:]):
        suite = numbers[i: preamble + i]
        if not is_valid(suite, n):
            return n


def find_first_non_valid_in_file(filename: str, preamble: int) -> int:
    with open(filename, 'r') as f:
        numbers = [int(i) for i in f.readlines()]
        return _find_first_non_valid_number(numbers, preamble)


def find_contiguous_numbers_adds_up_to_invalid_number(filename: str, preamble: int) -> Tuple[int, List[int]]:
    with open(filename, 'r') as f:
        numbers = [int(i) for i in f.readlines()]
        n = _find_first_non_valid_number(numbers, preamble)
        s, k = 0, 0
        for i, j in enumerate(numbers):
            s, k = j, 1
            while s < n:
                s += numbers[i + k]
                k += 1
            if s == n:
                break
        return n, numbers[i: i + k], min(numbers[i: i + k]) + max(numbers[i: i + k])
