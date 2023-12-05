# Run solution on day 14 input code
# Solution code is responsible for printing solution

import day_14

try:
    f = open("day_14/day_14_input.txt", "r")
    contents = f.read()
    print("Solution 1 Result:")
    day_14.solve_problem_1(contents)
    f.close()
except NotImplementedError:
    pass
    
print("\n")

try:
    f = open("day_14/day_14_input.txt", "r")
    contents = f.read()
    print("Solution 2 Result:")
    day_14.solve_problem_2(contents)
    f.close()
except NotImplementedError:
    pass
