# Run solution on day 12 input code
# Solution code is responsible for printing solution

import day_12

try:
    f = open("day_12/day_12_input.txt", "r")
    contents = f.read()
    print("Solution 1 Result:")
    day_12.solve_problem_1(contents)
    f.close()
except NotImplementedError:
    pass
    
print("\n")

try:
    f = open("day_12/day_12_input.txt", "r")
    contents = f.read()
    print("Solution 2 Result:")
    day_12.solve_problem_2(contents)
    f.close()
except NotImplementedError:
    pass
