import functools
import operator
from typing import NamedTuple, List, Tuple


Maps = NamedTuple('Maps', (('size', Tuple), ('trees', List)))


def read_map(filename: str) -> Maps:
    with open(filename, 'r') as f:
        raw = f.readlines()
        trees = []
        for line in raw:
            col = 0
            for c in line:
                if c == '#':
                    trees.append(
                        (raw.index(line), col)
                    )
                col += 1
        maps = Maps(
            size=(len(raw), len(raw[0].strip('\n'))),
            trees=trees
        )
        return maps


def count_trees(maps: Maps, slope: Tuple[int, int]) -> int:
    line, col, trees = 0, 0, 0
    height, width = maps.size
    while line <= height:
        trees += 1 if (line, col % width) in maps.trees else 0
        line += slope[0]
        col += slope[1]
    return trees


def count_product_slopes(filename: str, slopes: List[Tuple]) -> int:
    maps = read_map(filename)

    def _(slope):
        return count_trees(maps=maps, slope=slope)

    return functools.reduce(
        operator.mul,
        map(_, slopes),
        1
    )
