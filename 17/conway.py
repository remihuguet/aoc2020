import dataclasses
from typing import Dict, List, Tuple


@dataclasses.dataclass(frozen=True)
class Grid:
    data: Dict[Tuple, int]


class Cube:

    def __init__(self, data: str):
        self._data = {
            (i, j, 0): 1 if v == '#' else 0 for j, line in enumerate(data.split('\n')) if line != '' for i, v in enumerate(line)
        }

    def _coord(self, coord: int, index: int):
        return Grid({
             k: v for k, v in self._data.items() if k[coord] == index
        })

    def x(self, index: int) -> Grid:
        return self._coord(0, index)

    def y(self, index: int) -> Grid:
        return self._coord(1, index)

    def z(self, index: int) -> Grid:
        return self._coord(2, index)


def parse_input(filename: str) -> List[List[List[int]]]:
    with open(filename, 'r') as f:
        return Cube(f.read())


def next_cycle(state: Cube, coord: Tuple[int, int, int]) -> Cube:
    neighbours = 
    