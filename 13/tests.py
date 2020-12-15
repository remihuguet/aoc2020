import shuttle


def test_compute_earliest_bus():
    with open('13/test_input.txt') as f:
        d = f.readlines()
        time = int(d[0].rstrip('\n'))
        buses = [int(i) for i in d[1].rstrip('\n').split(',') if i != 'x']
        assert 59, 5 == shuttle.compute_earliest_bus(time, buses)


def test_compute_result_part_1():
    assert 295 == shuttle.compute_result_part_1('13/test_input.txt')