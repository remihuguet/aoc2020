from typing import Dict, List


def parse_rules(filename: str) -> Dict:
    with open(filename, 'r') as f:
        lines = f.readlines()
        res = {}
        for r in lines:
            k, vals = r.split('bags contain')
            k = k.rstrip(' ')
            res[k] = {}
            for v in vals.split(','):
                color, number = ' '.join(v.split(' ')[2:4]), v.split(' ')[1]
                if color != 'other bags.\n':
                    res[k][color] = int(number)
        return res


def _count_colors(color: str, rules: Dict) -> int:
    colors = set([])
    bags = [color]
    while True:
        new = set([])
        for c in bags:
            new.update(_find_color_contained(c, rules))
        if len(new) == 0:
            break
        colors.update(new)
        bags = new
    return colors


def _find_color_contained(color: str, rules: Dict) -> List[str]:
    return set([k for k, v in rules.items() if color in v.keys()])


def count_bags_countain(color: str, rules: Dict) -> int:
    return len(_count_colors(color, rules))


def _number_in(color: str, rules: Dict) -> int:
    res = 1
    for c, n in rules[color].items():
        res += int(n) * _number_in(c, rules)
    return res


def count_needed_bags(color: str, rules: Dict) -> int:
    return _number_in(color, rules) - 1
