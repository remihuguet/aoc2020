from typing import List


class Next:

    def __init__(self, numbers: List[int]):
        self._map = {n: i + 1 for i, n in enumerate(numbers)}

    def __call__(self, numbers: List[int]) -> int:
        last, pos = numbers[-1], len(numbers)
        prev = self._map[last] if last in self._map else pos
        self._map[last] = pos
        return pos - prev


def next(numbers: List[int]) -> int:
    last = numbers[-1]
    previous = list(filter(lambda n: n[1] == last, [(i, n) for i, n in enumerate(numbers[:-1])]))
    return len(numbers) - previous[-1][0] - 1 if previous else 0


def compute_number_at_turn(turn: int, starting: List[int]) -> int:
    t0 = len(starting) + 1
    nex = Next(starting)
    while t0 <= turn:
        starting.append(nex(starting))
        t0 += 1
    return starting[-1]
