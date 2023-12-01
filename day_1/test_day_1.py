import pytest
import day_1


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (day_1.PROBLEM_1_EXAMPLE_1_INPUT, day_1.PROBLEM_1_EXAMPLE__1_ANSWER),
    ],
)
def test_solve_problem_1(test_input, expected):
    assert day_1.solve_problem_1(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (day_1.PROBLEM_2_EXAMPLE_1_INPUT, day_1.PROBLEM_2_EXAMPLE__1_ANSWER),
        (day_1.PROBLEM_2_EXAMPLE_2_INPUT, day_1.PROBLEM_2_EXAMPLE__2_ANSWER),
    ],
)
def test_solve_problem_2(test_input, expected):
    assert day_1.solve_problem_2(test_input) == expected

