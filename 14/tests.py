import docking


def test_compute_simple_masking_from_int():
    mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'
    val = 11

    assert 73 == docking.apply_mask(val, mask)

    val = 101
    assert 101 == docking.apply_mask(val, mask)

    val = 0
    assert 64 == docking.apply_mask(val, mask)


def test_compute_init_program():
    assert 165 == docking.compute_init('14/test_input.txt')


def test_compute_memory_addresses():
    mask = '000000000000000000000000000000X1001X'
    mem = 42

    assert set([26, 27, 58, 59]) == set(docking.compute_addresses(mem, mask))


def test_compute_init_part2():
    mask = '000000000000000000000000000000X1001X'
    mem = 42

    assert set([26, 27, 58, 59]) == set(docking.compute_addresses(mem, mask))


def test_compute_init_program_2():
    assert 208 == docking.compute_init_2('14/test_input_2.txt')

