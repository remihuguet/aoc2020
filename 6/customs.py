from typing import List


def count_for_group(answers: List[str]) -> int:
    return len(set('').union(*[set(s) for s in answers]))


def count_everyone(answers: List[str]) -> int:
    first = set(answers[0])
    return len(first.intersection(*[set(s) for s in answers[1:]]))


def parse_input(input: str) -> List[List[str]]:
    return [i.split('\n') for i in input.rstrip('\n').split('\n\n')]


def compute_score(input: str) -> int:
    groups = parse_input(input)
    return sum([count_for_group(g) for g in groups])


def compute_score_everyone(input: str) -> int:
    groups = parse_input(input)
    return sum([count_everyone(g) for g in groups])


def result(filename: str) -> int:
    with open(filename, 'r') as f:
        input = f.read()
        return compute_score(input)


def result_everyone(filename: str) -> int:
    with open(filename, 'r') as f:
        input = f.read()
        return compute_score_everyone(input)
