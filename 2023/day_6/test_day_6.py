import pytest
import day_6

@pytest.mark.parametrize(
    "test_input,expected",
    [
        (day_6.PROBLEM_1_EXAMPLE_1_INPUT, day_6.PROBLEM_1_EXAMPLE__1_ANSWER),
        # (day_6.PROBLEM_1_EXAMPLE_1_INPUT, day_6.PROBLEM_1_EXAMPLE__1_ANSWER), # ADD YOUR OWN TEST CASES HERE
    ],
)
def test_solve_problem_1(test_input, expected):
    assert day_6.solve_problem_1(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (day_6.PROBLEM_2_EXAMPLE_1_INPUT, day_6.PROBLEM_2_EXAMPLE__1_ANSWER),
        # (day_6.PROBLEM_1_EXAMPLE_1_INPUT, day_6.PROBLEM_1_EXAMPLE__1_ANSWER), # ADD YOUR OWN TEST CASES HERE
    ],
)
def test_solve_problem_2(test_input, expected):
    assert day_6.solve_problem_2(test_input) == expected

