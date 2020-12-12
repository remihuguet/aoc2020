from typing import Dict, List
import functools


def compute_interval(adapters: List[int]) -> Dict:
    joltages = sorted([int(i.replace('\n', '')) for i in adapters])
    joltages.append(joltages[-1] + 3)
    result = {1: 0, 2: 0, 3: 0}
    for i, v in enumerate(joltages):
        if i > 0:
            result[v - joltages[i - 1]] += 1
        else:
            result[v] += 1
    print(result)
    return result


def compute_id(adapters: List[int]) -> int:
    inter = compute_interval(adapters)
    return inter[1] * inter[3]


class CountArrangements:
    def __init__(self, adapters: List[int]):
        self._adapters = sorted([int(i.replace('\n', '')) for i in adapters])
        self._combos = {}

    def __call__(self) -> int:
        return self.combo(0)

    def combo(self, jolt: int):
        if jolt in self._combos:
            return self.combos[jolt]
        total = self.combo(jolt + 1) if jolt + 1 in self._adapters else 0
        total += self.combo(jolt + 2) if jolt + 2 in self._adapters else 0
        total += self.combo(jolt + 3) if jolt + 3 in self._adapters else 0
        if total == 0:
            total = 1
        return total


class AltCountArrangements:
    def __init__(self, adapters: List[int]):
        self._adapters = sorted([int(i.replace('\n', '')) for i in adapters])
        self._adapters.append(self._adapters[-1] + 3)
        self._adapters.insert(0, 0)

    def __call__(self) -> int:
        intervals = self.get_intervals()
        return functools.reduce(lambda acc, cur: acc * self.get_combination_number(len(cur)), intervals, 1)

    def get_combination_number(self, n: int):
        f = [0, 1, 1]
        for i in range(3, n + 1):
            f.append(f[i - 1] + f[i - 2] + f[i - 3])
        return f[n]

    def get_intervals(self):
        intervals = []
        tmp = []

        for i, a in enumerate(self._adapters):
            tmp.append(a)

            if i < len(self._adapters) - 1 and self._adapters[i + 1] - a != 1:
                if len(tmp) > 2:
                    intervals.append(tmp)
                tmp = []
        return intervals
