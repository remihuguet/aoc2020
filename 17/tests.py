import conway


def test_parse_input():
    cube = conway.parse_input('17/test_input.txt')

    # assert conway.Grid([
    # [0, 1, 0],
    # [0, 0, 1],
    # [1, 1, 1]]) == cube.z(0)
    assert conway.Grid({
        (0, 0, 0): 0,
        (0, 1, 0): 0,
        (0, 2, 0): 1
    }) == cube.x(0)

    assert conway.Grid({
        (0, 0, 0): 0,
        (1, 0, 0): 1,
        (2, 0, 0): 0
    }) == cube.y(0)

    assert conway.Grid({
        (0, 0, 0): 0,
        (1, 0, 0): 1,
        (2, 0, 0): 0,
        (0, 1, 0): 0,
        (1, 1, 0): 0,
        (2, 1, 0): 1,
        (0, 2, 0): 1,
        (1, 2, 0): 1,
        (2, 2, 0): 1

    }) == cube.z(0)


def test_compute_next_cycle_value_on_one_point():
    assert 1 == conway.next_cycle(conway.parse_input('17/test_input.txt'), coord=(0, 0, 0))


# def test_compute_next_cycle():
#     assert [
#         [
#             [1, 0, 0],
#             [0, 0, 1],
#             [0, 1, 0]
#         ], 
#         [
#             [1, 0, 1],
#             [0, 1, 1],
#             [0, 1, 0]
#         ],
#         [
#             [1, 0, 0],
#             [0, 0, 1],
#             [0, 1, 0]
#         ]
#     ] == conway.compute_next_cycle(conway.parse_input('17/test_input.txt'))