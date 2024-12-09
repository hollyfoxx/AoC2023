import pytest
import day_8

@pytest.mark.parametrize(
    "test_input,expected",
    [
        (day_8.PROBLEM_1_EXAMPLE_1_INPUT, day_8.PROBLEM_1_EXAMPLE__1_ANSWER),
        # (day_8.PROBLEM_1_EXAMPLE_1_INPUT, day_8.PROBLEM_1_EXAMPLE__1_ANSWER), # ADD YOUR OWN TEST CASES HERE
    ],
)
def test_solve_problem_1(test_input, expected):
    assert day_8.solve_problem_1(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (day_8.PROBLEM_2_EXAMPLE_1_INPUT, day_8.PROBLEM_2_EXAMPLE__1_ANSWER),
        # (day_8.PROBLEM_1_EXAMPLE_1_INPUT, day_8.PROBLEM_1_EXAMPLE__1_ANSWER), # ADD YOUR OWN TEST CASES HERE
    ],
)
def test_solve_problem_2(test_input, expected):
    assert day_8.solve_problem_2(test_input) == expected

