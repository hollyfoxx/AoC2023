# Run solution on day 15 input code
# Solution code is responsible for printing solution

import day_15

try:
    f = open("day_15/day_15_input.txt", "r")
    contents = f.read()
    print("Solution 1 Result:")
    day_15.solve_problem_1(contents)
    f.close()
except NotImplementedError:
    pass
    
print("\n")

try:
    f = open("day_15/day_15_input.txt", "r")
    contents = f.read()
    print("Solution 2 Result:")
    day_15.solve_problem_2(contents)
    f.close()
except NotImplementedError:
    pass
