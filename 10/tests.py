import adapter


def test_return_correct_adapters_suite():
    with open('10/test_input.txt') as f:
        adapters = f.readlines()
        assert {1: 7, 2: 0, 3: 5} == adapter.compute_interval(adapters)
        assert 35 == adapter.compute_id(adapters)

    with open('10/test_input_2.txt') as f:
        adapters = f.readlines()
        assert {1: 22, 2: 0, 3: 10} == adapter.compute_interval(adapters)
        assert 220 == adapter.compute_id(adapters)


def test_count_arrangements():
    with open('10/test_input.txt') as f:
        adapters = f.readlines()
        assert 8 == adapter.CountArrangements(adapters)()


def test_count_arrangements_2():
    with open('10/test_input_2.txt') as f:
        adapters = f.readlines()
        assert 19208 == adapter.CountArrangements(adapters)()


def test_count_arrangements_alternative():
    with open('10/test_input_2.txt') as f:
        adapters = f.readlines()
        assert 19208 == adapter.AltCountArrangements(adapters)()
