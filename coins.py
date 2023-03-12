"""
This function tries to recursively solve the coin challenge. It shows all the possible combination of
different changes which could add up to the target value. 
For example:
Followings are all the options to change 4 dollors with 1,and 2 dollor coins:
[[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [1, 3], [2, 1, 1], [2, 2], [3, 1]]
"""

def change_calculator(coins, target, stack, final_solutions, level=0):
 
    # If the remaining is 0 it means we have found a combination
    if target == 0:
        # print("one sulution: ")
        # print(stack)
        # if we don't append a copy of stack to final solutions, popping the stack will also pop the final solutions
        final_solutions.append(stack.copy())
        stack.pop()
        return
 
    # If the remaining is negative, it means we don't have a combination. So, we pop the last number from the 
    # stack and will go to next one
    if target < 0:
        stack.pop()
        return
 
    # do for each coin
    for c in coins:
        # This will help us to have the proper stack for each level of recursive thread.
        stack = stack[:level]
        stack.append(c)
        # Call the funtion recursively with the target - the current coin
        change_calculator(coins, target - c, stack, final_solutions, level + 1)
 
    # return the total number of solutions
    return final_solutions
 
 
coins = [1, 2, 3]
target = 4
stack = []
final_solutions = []
final_solutions = change_calculator(coins, target, stack, final_solutions)
print("="*100)
print("Solutions of changing " + str(target) + " with ")
print(coins)
print(final_solutions)
print("Total solutions:" + str(len(final_solutions)))
print("="*100)