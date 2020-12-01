from typing import List, Tuple, Type


def get_numbers(input_filename: str) -> List[int]:
    with open(input_filename, 'r') as f:
        return [int(i) for i in f.readlines()]


def find_complements_to(n: int, into: List[int]) -> Tuple[int, int]:
    while into:
        f = into.pop()
        try:
            i = into.index(n - f)
            return into[i], f
        except ValueError:
            continue


def solve_two(input_filename: str) -> int:
    inputs = get_numbers(input_filename)
    to_find, c = find_complements_to(2020, inputs)
    return to_find * c


def solve_three(input_filename: str) -> int:
    inputs = get_numbers(input_filename)
    while inputs:
        n = inputs.pop()
        remains = list(filter(lambda i: i < 2020 - n, inputs))
        try:
            to_find, c = find_complements_to(2020 - n, remains)
            return n * to_find * c
        except TypeError:
            continue
