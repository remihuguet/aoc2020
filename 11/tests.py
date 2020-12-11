import seating


first_round = '''#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##'''
second_round = '''#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##'''


input = '''L.LL
LLLL
L.L.
LLLL'''


def test_parse_input():
    assert (
        ('L', '.', 'L', 'L'),
        ('L', 'L', 'L', 'L'),
        ('L', '.', 'L', '.'),
        ('L', 'L', 'L', 'L'),
    ) == seating.parse_seats(input)


def test_apply_rules_to_one_seat():
    assert '#' == seating.apply_transition(state=seating.parse_seats(input))[1][1]

    input_2 = '''#.#L
#LLL
#.L.
LLLL'''

    assert 'L' == seating.apply_transition(state=seating.parse_seats(input_2))[1][1]

    input_3 = '''#.#L
#..L
#.L.
LLLL'''
    assert '.' == seating.apply_transition(state=seating.parse_seats(input_3))[1][1]


def test_apply_rules_to_grid():
    assert (
        ('#', '.', '#', '#'),
        ('#', '#', '#', '#'),
        ('#', '.', '#', '.'),
        ('#', '#', '#', '#'),
    ) == seating.apply_transition(state=seating.parse_seats(input))

    assert (
        ('#', '.', 'L', '#'),
        ('#', 'L', 'L', 'L'),
        ('L', '.', 'L', '.'),
        ('#', 'L', '#', '#'),
    ) == seating.apply_transition(
        state=seating.apply_transition(
            seating.parse_seats(input)
        )
    )

    f = open('11/test_input.txt', 'r')
    grid = f.read().rstrip('\n')
    assert seating.parse_seats(first_round) == seating.apply_transition(
        seating.parse_seats(grid)
    )

    assert seating.parse_seats(second_round) == seating.apply_transition(
        seating.apply_transition(
            seating.parse_seats(grid)
        )
    )


def test_find_number_of_occupied_seat_in_stable_state():
    assert 37 == seating.occupied_seat_in_stable('11/test_input.txt')


def test_compute_adjacents_seats_for_part_2():
    input = '''.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#.....'''
    input = seating.parse_seats(input)
    assert ['#', '#', '#', '#', '#', '#', '#', '#'] == seating.compute_adjacents(input=input, coord=(4, 3))

    input = '''.............
.L.L.#.#.#.#.
.............'''
    input = seating.parse_seats(input)
    assert ['L'] == seating.compute_adjacents(input=input, coord=(1, 1))

    input = '''.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##.'''
    input = seating.parse_seats(input)
    assert [] == seating.compute_adjacents(input=input, coord=(3, 3))


def test_apply_rules_to_grid_part_2():
    first_round = '''#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##'''
    second_round = '''#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#'''

    f = open('11/test_input.txt', 'r')
    grid = f.read().rstrip('\n')
    assert seating.parse_seats(first_round) == seating.apply_transition_part_2(
        seating.parse_seats(grid)
    )

    assert seating.parse_seats(
        second_round
    ) == seating.apply_transition_part_2(
        seating.apply_transition(
            seating.parse_seats(grid)
        )
    )


def test_find_number_of_occupied_seat_in_stable_state_part_2():
    assert 26 == seating.occupied_seat_in_stable_part_2('11/test_input.txt')
