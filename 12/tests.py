import rainrisk


def test_compute_new_direction():
    direction = (1, 0)

    assert (0, -1) == rainrisk.compute_new_direction(direction, 'R90')
    assert (0, 1) == rainrisk.compute_new_direction(direction, 'L90')

    assert (-1, 0) == rainrisk.compute_new_direction(direction, 'R180')
    assert (-1, 0) == rainrisk.compute_new_direction(direction, 'L180')
    assert (0, 1) == rainrisk.compute_new_direction(direction, 'R270')
    assert (0, -1) == rainrisk.compute_new_direction(direction, 'L270')
    assert (1, 0) == rainrisk.compute_new_direction(direction, 'R360')
    assert (1, 0) == rainrisk.compute_new_direction(direction, 'L360')

    direction = (0, 1)

    assert (1, 0) == rainrisk.compute_new_direction(direction, 'R90')
    assert (-1, 0) == rainrisk.compute_new_direction(direction, 'L90')
    assert (0, -1) == rainrisk.compute_new_direction(direction, 'R180')
    assert (0, -1) == rainrisk.compute_new_direction(direction, 'L180')
    assert (-1, 0) == rainrisk.compute_new_direction(direction, 'R270')
    assert (1, 0) == rainrisk.compute_new_direction(direction, 'L270')
    assert (0, 1) == rainrisk.compute_new_direction(direction, 'R360')
    assert (0, 1) == rainrisk.compute_new_direction(direction, 'L360')


def test_compute_final_position():
    with open('12/test_input.txt', 'r') as f:
        mvts = f.readlines()
        assert (17, -8) == rainrisk.compute_final_position(mvts)


def test_compute_manhattan():
    assert 25 == rainrisk.compute_manhattan('12/test_input.txt')


def test_compute_position_waypoint():
    with open('12/test_input.txt', 'r') as f:
        mvts = f.readlines()
        initial = (10, 1)
        assert (214, -72) == rainrisk.compute_position_waypoint(mvts, initial)


def test_compute_final_manhattan():
    assert 286 == rainrisk.compute_final_manhattan('12/test_input.txt')


def test_compute_speed_rotation():
    speed = (10, 1)

    assert (1, -10) == rainrisk.compute_speed_rotation(speed, 'R90')
    assert (-1, 10) == rainrisk.compute_speed_rotation(speed, 'L90')

    assert (-10, -1) == rainrisk.compute_speed_rotation(speed, 'R180')
    assert (-10, -1) == rainrisk.compute_speed_rotation(speed, 'L180')

    assert (-1, 10) == rainrisk.compute_speed_rotation(speed, 'R270')
    assert (1, -10) == rainrisk.compute_speed_rotation(speed, 'L270')
