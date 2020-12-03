from typing import NamedTuple, List, Tuple


Maps = NamedTuple('Maps', (('size', Tuple), ('trees', List)))


def read_map(filename: str) -> Maps:
    with open(filename, 'r') as f:
        raw = f.readlines()
        maps = Maps(
            size=(len(raw), len(raw[0].strip('\n'))),
            trees=[]
        )
        for line in raw:
            count = 0
            for c in line:
                if c == '#':
                    maps.trees.append(
                        (raw.index(line), count)
                    )
                count += 1
        return maps


def count_trees(maps: Maps, slope: Tuple[int, int]) -> int:
    line = 0
    col = 0
    trees = 0
    while line <= maps.size[0]:
        if (line, col % maps.size[1]) in maps.trees:
            trees += 1
        line += slope[0]
        col += slope[1]
    return trees


def count_product_slopes(filename: str, slopes: List[Tuple]) -> int:
    maps = read_map(filename)
    res = 1
    for slope in slopes:
        res *= count_trees(maps=maps, slope=slope)
    return res
