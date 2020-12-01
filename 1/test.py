import report_repair


input_file = '1/test_input.txt'


def test_repair_report_add_two():
    expected = 514579

    assert expected == report_repair.solve_two(input_file)


def test_repair_report_add_three():
    expected = 241861950

    assert expected == report_repair.solve_three(input_file)
