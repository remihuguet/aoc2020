import haversacks


def test_parse_rules():
    assert {
        'light red': {
            'bright white': 1,
            'muted yellow': 2
            },
        'dark orange': {
            'bright white': 3,
            'muted yellow': 4
        },
        'bright white': {'shiny gold': 1},
        'muted yellow': {'shiny gold': 2, 'faded blue': 9},
        'shiny gold': {'dark olive': 1, 'vibrant plum': 2},
        'dark olive': {'faded blue': 3, 'dotted black': 4},
        'vibrant plum': {'faded blue': 5, 'dotted black': 6},
        'faded blue': {},
        'dotted black': {}
    } == haversacks.parse_rules('7/test_input.txt')


def test_count_bags():
    rules = haversacks.parse_rules('7/test_input.txt')
    assert 4 == haversacks.count_bags_countain('shiny gold', rules)


def test_count_all_bags():
    rules = haversacks.parse_rules('7/test_input.txt')
    assert 32 == haversacks.count_needed_bags('shiny gold', rules)

    rules = haversacks.parse_rules('7/test_input_2.txt')
    assert 126 == haversacks.count_needed_bags('shiny gold', rules)
