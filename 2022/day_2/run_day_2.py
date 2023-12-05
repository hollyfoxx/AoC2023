# Run solution on day 2 input code
# Solution code is responsible for printing solution

import day_2

try:
    f = open("day_2/day_2_input.txt", "r")
    contents = f.read()
    print("Solution 1 Result:")
    day_2.solve_problem_1(contents)
    f.close()
except NotImplementedError:
    pass
    
print("\n")

try:
    f = open("day_2/day_2_input.txt", "r")
    contents = f.read()
    print("Solution 2 Result:")
    day_2.solve_problem_2(contents)
    f.close()
except NotImplementedError:
    pass
