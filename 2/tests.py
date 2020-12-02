import password


def test_password_is_valid_according_to_occurency_policy():
    input = '1-3 a: abcde'
    policy, pwd = input.split(': ')
    assert password.validate_occurences(policy, pwd)


def test_password_is_invalid_according_to_occurency_policy():
    input = '1-3 b: cdefg'
    policy, pwd = input.split(': ')
    assert not password.validate_occurences(policy, pwd)


def test_count_valid_password_in_file_input():
    assert 2 == password.count_valids_occurences('2/test_input.txt')


def test_password_is_valid__according_to_position_policy():
    input = '1-3 a: abcde'
    policy, pwd = input.split(': ')
    assert password.validate_position(policy, pwd)


def test_count_valid_positions_password_in_file_input():
    assert 1 == password.count_valids_positions('2/test_input.txt')
