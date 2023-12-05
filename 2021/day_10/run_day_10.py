# Run solution on day 10 input code
# Solution code is responsible for printing solution

import day_10

try:
    f = open("day_10/day_10_input.txt", "r")
    contents = f.read()
    print("Solution 1 Result:")
    day_10.solve_problem_1(contents)
    f.close()
except NotImplementedError:
    pass
    
print("\n")

try:
    f = open("day_10/day_10_input.txt", "r")
    contents = f.read()
    print("Solution 2 Result:")
    day_10.solve_problem_2(contents)
    f.close()
except NotImplementedError:
    pass
