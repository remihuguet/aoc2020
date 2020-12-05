from typing import List


def find_column(cols: str) -> int:
    return _find_into(cols, range(8), 'L')


def find_row(rows: str) -> int:
    return _find_into(rows, range(128), 'F')


def _find_into(values: str, interval: range, lower_flag: str) -> int:
    for s in values:
        interval = (
            interval[:int(len(interval) / 2)] if s == lower_flag
            else interval[int(len(interval) / 2):]
        )
    return interval[0]


def compute_boarding_id(boarding: str) -> int:
    return find_column(boarding[7:]) + find_row(boarding[:7]) * 8


def compute_highest(filename: str) -> int:
    return max(compute_ids(filename))


def compute_ids(filename: str) -> int:
    with open(filename, 'r') as f:
        boardings = f.readlines()
        return [compute_boarding_id(b) for b in boardings]


def find_seat_id(ids: List[str]) -> int:
    mi, ma = min(ids), max(ids)
    return (set(range(mi, ma)) - set(ids)).pop()
