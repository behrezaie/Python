def find_longest_common_prefix(list_of_words, prefix=True):
  """
  This function finds and returns the longest common prefix among all given strings.
  input:
    list_of_words (list of strings)
    prefix (boolean): default True. Set to False for longest common postfix
  output:
    common_prefix (string)
  """
  if not prefix:
    list_of_words = [x[::-1] for x in list_of_words]

  if not list_of_words:
    print("The list is empty!")
    exit()
  else:
    shortest_lenght = min(list_of_words, key=len)

  common_prefix = ""
  for i in range(len(shortest_lenght)):
    if all(word[i] == shortest_lenght[i] for word in list_of_words):
      common_prefix += shortest_lenght[i]
    else:
      break

  if not prefix:
    common_prefix = common_prefix[::-1]
  return common_prefix


list_of_words = ["wonder", "wonderful", "wonderland"]
print(list_of_words)
print("Longest common prefix is: " + find_longest_common_prefix(list_of_words))