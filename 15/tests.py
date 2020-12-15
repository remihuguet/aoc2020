import pytest
import memory

inputs = [
    (0, 3, 6, 436),
    (1, 3, 2, 1),
    (2, 1, 3, 10),
    (1, 2, 3, 27),
    (2, 3, 1, 78),
    (3, 2, 1, 438),
    (3, 1, 2, 1836)
]


@pytest.fixture(params=inputs)
def starting(request):
    return list(request.param[:3]), request.param[-1]


def test_apply_rule_for_one_turn():
    starting = list(inputs[0][:3])
    assert 0 == memory.next(starting)
    assert 3 == memory.next(starting + [0])
    assert 3 == memory.next(starting + [0, 3])
    assert 1 == memory.next(starting + [0, 3, 3])
    assert 0 == memory.next(starting + [0, 3, 3, 1])
    assert 4 == memory.next(starting + [0, 3, 3, 1, 0])
    assert 0 == memory.next(starting + [0, 3, 3, 1, 0, 4])


def test_find_2020_number(starting):
    numbers, expec = starting
    assert expec == memory.compute_number_at_turn(turn=2020, starting=numbers)



inputs_high = [
    (0, 3, 6, 175594),
    (1, 3, 2, 2578),
    (2, 1, 3, 3544142),
    (1, 2, 3, 261214),
    (2, 3, 1, 6895259),
    (3, 2, 1, 18),
    (3, 1, 2, 362)
]


@pytest.fixture(params=inputs_high)
def starting_h(request):
    return list(request.param[:3]), request.param[-1]


def test_find_high_number(starting_h):
    numbers, expec = starting_h
    assert expec == memory.compute_number_at_turn(turn=30000000, starting=numbers)
