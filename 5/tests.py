import boarding


text_expected = [
    (44, 5, 357),
    (70, 7, 567),
    (14, 7, 119),
    (102, 4, 820)
]


def test_find_column():
    cols = 'RLR'
    assert 5 == boarding.find_column(cols)

    cols = 'RRR'
    assert 7 == boarding.find_column(cols)

    cols = 'RLL'
    assert 4 == boarding.find_column(cols)


def test_find_row():
    rows = 'FBFBBFF'
    assert 44 == boarding.find_row(rows)

    rows = 'BFFFBBF'
    assert 70 == boarding.find_row(rows)

    rows = 'FFFBBBF'
    assert 14 == boarding.find_row(rows)

    rows = 'BBFFBBF'
    assert 102 == boarding.find_row(rows)


def test_compute_boarding_id():
    assert 357 == boarding.compute_boarding_id('FBFBBFFRLR')
    assert 567 == boarding.compute_boarding_id('BFFFBBFRRR')
    assert 119 == boarding.compute_boarding_id('FFFBBBFRRR')
    assert 820 == boarding.compute_boarding_id('BBFFBBFRLL')


def test_highest_id():
    assert 820 == boarding.compute_highest('5/test_input.txt')


def test_find_seat_id():
    ids = [5, 3, 2, 8, 9, 6, 1, 4, 10]
    assert 7 == boarding.find_seat_id(ids)
