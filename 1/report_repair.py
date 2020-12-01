from typing import List, Tuple


def get_numbers(input_filename: str) -> List[int]:
    return [int(i) for i in open(input_filename, 'r').readlines()]


def find_complement(n: int, remains: List[int]) -> Tuple[int, int, bool]:
    to_find, c = 0, 0
    for c in remains:
        try:
            to_find = remains[remains.index(n - c)]
            break
        except ValueError:
            continue
    return to_find, c, to_find + c == n


def solve_two(input_filename: str) -> int:
    report = get_numbers(input_filename)
    to_find, c, _ = find_complement(2020, report)
    return to_find * c


def solve_three(input_filename: str) -> int:
    numbers = get_numbers(input_filename)
    numbers.sort()

    while numbers:
        n = numbers.pop()
        remains = list(filter(lambda i: i < 2020 - n, numbers))
        to_find, c, ok = find_complement(2020 - n, remains)
        if ok:
            return n * to_find * c
