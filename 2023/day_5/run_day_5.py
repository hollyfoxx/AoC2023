# Run solution on day 5 input code
# Solution code is responsible for printing solution

import day_5

try:
    f = open("2023/day_5/day_5_input.txt", "r")
    contents = f.read()
    print("Solution 1 Result:")
    day_5.solve_problem_1(contents)
    f.close()
except NotImplementedError:
    pass
    
print("\n")

try:
    f = open("2023/day_5/day_5_input.txt", "r")
    contents = f.read()
    print("Solution 2 Result:")
    day_5.solve_problem_2(contents)
    f.close()
except NotImplementedError:
    pass
