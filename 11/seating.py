import itertools
from typing import List, Tuple


def parse_seats(input: str) -> Tuple[Tuple[str]]:
    return tuple(tuple(c for c in line) for line in input.split('\n'))


def apply_transition(state: Tuple[Tuple[str]]) -> Tuple[Tuple[str]]:
    new_state = list(list(s for s in line) for line in state)
    for i, line in enumerate(state):
        for j, col in enumerate(line):
            line_range = range(max(0, i - 1), min(i + 2, len(state)))
            col_range = range(max(0, j - 1),  min(j + 2, len(line)))
            adjacents = [
                state[k][l]
                for k, l in itertools.product(line_range, col_range)
                if k != i or l != j
            ]
            if col == 'L':
                if '#' not in adjacents:
                    new_state[i][j] = '#'
            elif col == '#':
                if len(list(filter(lambda e: e == '#', adjacents))) >= 4:
                    new_state[i][j] = 'L'

    return tuple(tuple(c for c in line) for line in new_state)


def occupied_seat_in_stable(filename: str) -> int:
    with open(filename, 'r') as f:
        raw = f.read().rstrip('\n')
        previous_grid = parse_seats(raw)
        grid = apply_transition(previous_grid)
        while grid != previous_grid:
            previous_grid = grid
            grid = apply_transition(grid)
        return sum([len(list(filter(lambda e: e == '#', line))) for line in grid])


def compute_adjacents(input: str, coord: Tuple[int, int]) -> List[str]:
    l, c = coord
    raw_adjacents = itertools.product(
        range(max(0, l - 1), min(l + 2, len(input))),
        range(max(0, c - 1),  min(c + 2, len(input[0])))
    )

    adjacents = []

    for p in raw_adjacents:
        if p == coord:
            continue
        i = 1
        val = None
        while val not in ('L', '#'):
            j, k = l + (p[0] - l) * i, c + (p[1] - c) * i
            if j < 0 or k < 0 or j >= len(input) or k >= len(input[0]):
                val = None
                break
            val = input[j][k]
            i += 1
        if val:
            adjacents.append(val)
    return adjacents


def apply_transition_part_2(state: Tuple[Tuple[str]]) -> Tuple[Tuple[str]]:
    new_state = list(list(s for s in line) for line in state)
    for i, line in enumerate(state):
        for j, col in enumerate(line):
            adjacents = compute_adjacents(state, (i, j))
            if col == 'L':
                if '#' not in adjacents:
                    new_state[i][j] = '#'
            elif col == '#':
                if len(list(filter(lambda e: e == '#', adjacents))) >= 5:
                    new_state[i][j] = 'L'
    return tuple(tuple(c for c in line) for line in new_state)


def occupied_seat_in_stable_part_2(filename: str) -> int:
    with open(filename, 'r') as f:
        raw = f.read().rstrip('\n')
        previous_grid = parse_seats(raw)
        grid = apply_transition_part_2(previous_grid)
        while grid != previous_grid:
            previous_grid = grid
            grid = apply_transition_part_2(grid)
        return sum([len(list(filter(lambda e: e == '#', line))) for line in grid])
