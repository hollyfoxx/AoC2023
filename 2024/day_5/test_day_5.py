import pytest
import day_5

@pytest.mark.parametrize(
    "test_input,expected",
    [
        (day_5.PROBLEM_1_EXAMPLE_1_INPUT, day_5.PROBLEM_1_EXAMPLE__1_ANSWER),
        # (day_5.PROBLEM_1_EXAMPLE_1_INPUT, day_5.PROBLEM_1_EXAMPLE__1_ANSWER), # ADD YOUR OWN TEST CASES HERE
    ],
)
def test_solve_problem_1(test_input, expected):
    assert day_5.solve_problem_1(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (day_5.PROBLEM_1_EXAMPLE_1_INPUT, day_5.PROBLEM_2_EXAMPLE__1_ANSWER),
        # (day_5.PROBLEM_1_EXAMPLE_1_INPUT, day_5.PROBLEM_1_EXAMPLE__1_ANSWER), # ADD YOUR OWN TEST CASES HERE
    ],
)
def test_solve_problem_2(test_input, expected):
    assert day_5.solve_problem_2(test_input) == expected

