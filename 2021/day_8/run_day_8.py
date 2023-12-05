# Run solution on day 8 input code
# Solution code is responsible for printing solution

import day_8

try:
    f = open("day_8/day_8_input.txt", "r")
    contents = f.read()
    print("Solution 1 Result:")
    day_8.solve_problem_1(contents)
    f.close()
except NotImplementedError:
    pass
    
print("\n")

try:
    f = open("day_8/day_8_input.txt", "r")
    contents = f.read()
    print("Solution 2 Result:")
    day_8.solve_problem_2(contents)
    f.close()
except NotImplementedError:
    pass
