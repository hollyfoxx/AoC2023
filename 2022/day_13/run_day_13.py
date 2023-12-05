# Run solution on day 13 input code
# Solution code is responsible for printing solution

import day_13

try:
    f = open("day_13/day_13_input.txt", "r")
    contents = f.read()
    print("Solution 1 Result:")
    day_13.solve_problem_1(contents)
    f.close()
except NotImplementedError:
    pass
    
print("\n")

try:
    f = open("day_13/day_13_input.txt", "r")
    contents = f.read()
    print("Solution 2 Result:")
    day_13.solve_problem_2(contents)
    f.close()
except NotImplementedError:
    pass
