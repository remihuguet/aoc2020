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

    assert [26, 27, 58, 59] == docking.compute_addresses(mem, mask)
