from typing import Dict, List


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
