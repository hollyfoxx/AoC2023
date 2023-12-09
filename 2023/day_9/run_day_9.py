# Run solution on day 9 input code
# Solution code is responsible for printing solution

import day_9

try:
    f = open("2023/day_9/day_9_input.txt", "r")
    contents = f.read()
    print("Solution 1 Result:")
    day_9.solve_problem_1(contents)
    f.close()
except NotImplementedError:
    pass
    
print("\n")

try:
    f = open("2023/day_9/day_9_input.txt", "r")
    contents = f.read()
    print("Solution 2 Result:")
    day_9.solve_problem_2(contents)
    f.close()
except NotImplementedError:
    pass
