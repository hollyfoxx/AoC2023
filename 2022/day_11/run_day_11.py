# Run solution on day 11 input code
# Solution code is responsible for printing solution

import day_11

try:
    f = open("day_11/day_11_input.txt", "r")
    contents = f.read()
    print("Solution 1 Result:")
    day_11.solve_problem_1(contents)
    f.close()
except NotImplementedError:
    pass
    
print("\n")

try:
    f = open("day_11/day_11_input.txt", "r")
    contents = f.read()
    print("Solution 2 Result:")
    day_11.solve_problem_2(contents)
    f.close()
except NotImplementedError:
    pass
