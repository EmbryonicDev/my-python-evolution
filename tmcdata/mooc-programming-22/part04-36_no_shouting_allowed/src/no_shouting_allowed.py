def no_shouting(list):
  new_list = []
  
  for item in list:
    if not item.isupper():
      new_list.append(item)
  
  return new_list
  
  
if __name__ == "__main__":
  my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
  pruned_list = no_shouting(my_list)
  print(pruned_list)
  # Sample output
  # ['def', 'lower', 'another lower', 'Capitalized']