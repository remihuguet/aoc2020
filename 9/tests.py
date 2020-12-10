import encoding


def test_is_a_valid_number():
    suite = range(1, 26)
    assert encoding.is_valid(suite, number=26)
    assert not encoding.is_valid(suite, number=50)
    suite = range(2, 27)
    assert encoding.is_valid(suite, number=49)
    suite = list(range(3, 27)) + [49]
    assert not encoding.is_valid(suite, number=100)


def test_find_from_file_non_valid_number():
    assert 127 == encoding.find_first_non_valid_in_file('9/test_input.txt', preamble=5)


def test_find_contiguous_numbers_adds_up_to_invalid_number():
    assert (127, [15, 25, 47, 40], 62) == encoding.find_contiguous_numbers_adds_up_to_invalid_number('9/test_input.txt', preamble=5)
