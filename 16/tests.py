import ticket


def test_parse_authorize_values():
    expected = set(list(range(1, 4)) + list(range(5, 8)) + list(range(6, 12)) + list(range(33, 45)) + list(range(13, 41)) + list(range(45, 51)))
    assert expected == ticket.parse_authorize_values('16/test_input.txt')


def test_compute_error_rate():
    assert 71 == ticket.compute_error_rate('16/test_input.txt')


def test_keep_valid_tickets():

    expected = [
        [3, 9, 18],
        [15, 1, 5],
        [5, 14, 9]
    ]
    assert expected == ticket.keep_valid_tickets('16/test_input_2.txt')


def test_compute_fields_order():
    assert ['row', 'class', 'seat'] == ticket.compute_fields_order('16/test_input_2.txt')


def test_decode_ticket():
    assert {'row': 11, 'class': 12, 'seat': 13} == ticket.decode('16/test_input_2.txt')
