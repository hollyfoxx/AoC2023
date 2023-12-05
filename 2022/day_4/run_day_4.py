# Run solution on day 4 input code
# Solution code is responsible for printing solution

import day_4

try:
    f = open("day_4/day_4_input.txt", "r")
    contents = f.read()
    print("Solution 1 Result:")
    day_4.solve_problem_1(contents)
    f.close()
except NotImplementedError:
    pass
    
print("\n")

try:
    f = open("day_4/day_4_input.txt", "r")
    contents = f.read()
    print("Solution 2 Result:")
    day_4.solve_problem_2(contents)
    f.close()
except NotImplementedError:
    pass
