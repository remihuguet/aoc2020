import customs


group = ['abcx', 'abcy', 'abcz']


with open('6/test_input.txt', 'r') as f:
    input = f.read()


def test_count_for_group():
    assert 6 == customs.count_for_group(group)


def test_parse_input():

    assert [
        ['abc'],
        ['a', 'b', 'c'],
        ['ab', 'ac'],
        ['a', 'a', 'a', 'a'],
        ['b']
    ] == customs.parse_input(input)


def test_compute_score_of_groups():
    assert 11 == customs.compute_score(input)


def test_count_for_group_everyone():
    assert 3 == customs.count_everyone(group)


def test_count_score_everyone():
    assert 6 == customs.compute_score_everyone(input)
