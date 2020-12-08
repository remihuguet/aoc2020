import handeld


def test_accumulator_value_before_second_instruction():
    5 == handeld.compute_accumulator_value('8/test_input.txt')


def test_compute_final_value():
    8 == handeld.compute_final_value_debugged_code('8/test_input.txt')
