import toboggan


filename = '3/test_input.txt'


def test_read_map():
    maps = toboggan.read_map(filename)
    assert maps.size == (11, 11)
    print(maps.trees)
    assert maps.trees == [
        (0, 2), (0, 3),
        (1, 0), (1, 4), (1, 8),
        (2, 1), (2, 6), (2, 9),
        (3, 2), (3, 4), (3, 8), (3, 10),
        (4, 1), (4, 5), (4, 6), (4, 9),
        (5, 2), (5, 4), (5, 5),
        (6, 1), (6, 3), (6, 5), (6, 10),
        (7, 1), (7, 10),
        (8, 0), (8, 2), (8, 3), (8, 7),
        (9, 0), (9, 4), (9, 5), (9, 10),
        (10, 1), (10, 4), (10, 8), (10, 10)
    ]


def test_count_trees_with_slope():
    maps = toboggan.read_map(filename)

    assert 7 == toboggan.count_trees(maps=maps, slope=(1, 3))


def test_compute_slopes_product():
    slopes = [
        (1, 1),
        (1, 3),
        (1, 5),
        (1, 7),
        (2, 1)
    ]
    assert 336 == toboggan.count_product_slopes(
        filename=filename, slopes=slopes
    )
