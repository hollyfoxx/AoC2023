# Run solution on day 3 input code
# Solution code is responsible for printing solution

import day_3

try:
    f = open("2024/day_3/day_3_input.txt", "r")
    contents = f.read()
    print("Solution 1 Result:")
    day_3.solve_problem_1(contents)
    f.close()
except NotImplementedError:
    pass
    
print("\n")

try:
    f = open("2024/day_3/day_3_input.txt", "r")
    contents = f.read()
    print("Solution 2 Result:")
    day_3.solve_problem_2(contents)
    f.close()
except NotImplementedError:
    pass
