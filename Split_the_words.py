"""
You are given a string and a list of valid words ('the dictionary'). 
The string has had all the spaces and punctuation removed.
Implement the split_the_words function to split the string into words found in
the dictionary. 
There may be multiple possible splits. How might you handle this?

For example:
Given split_words("tablepton")
We might expect the output to look like:
[
    ["tab", "lept", "on"],
    ["tab", "lepton"]
]
"""

def split_the_words(list_of_words, target, stack, final_solutions, level=0):
    # Exit if the original target is ""
    if len(target) == 0 and level == 0:
        print("Target is empty!")
        exit()
    if len(target) == 0:
        # if we don't append a copy of stack to final solutions, popping the stack will also pop the final solutions
        final_solutions.append(stack.copy())
        stack.pop()
        return

    for item in list_of_words:
        # This will help us to have the proper stack for each level of recursive thread.
        stack = stack[:level]
        # If the target starts with item, we add the item to the stack, remove it from the target,
        # and call split_the_word fundction with the new target
        if target.startswith(item):
            stack.append(item)
            split_the_words(list_of_words, target[len(item):], stack, final_solutions, level + 1)

    return final_solutions

dictionary = [
    "a",
    "it",
    "leap",
    "able",
    "air",
    "hair",
    "pre",
    "table",
    "tab",
    "chair",
    "apple",
    "app",
    "cupboard",
    "cup",
    "board",
    "lept",
    "lepton",
    "ton",
    "on",
]

target = "tableptonlepton"
# we don't need to work with all the words in the dictionary. We just need those appearing in the target.
list_of_words = [x for x in dictionary if x in target]
stack = []
final_solutions = []
final_solutions = split_the_words(list_of_words, target, stack, final_solutions)
print("="*100)
print(str(len(final_solutions)) + " solution(s) ware found for \"" + target + "\"")
print(final_solutions)
print("="*100)