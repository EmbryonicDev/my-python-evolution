def all_the_longest(list):
  new_list = [list[0]]
  
  for i in range(len(list) - 1):
    if len(list[i+1]) > len(new_list[0]):
      new_list = [list[i+1]]
    elif len(list[i+1]) == len(new_list[0]):
      new_list.append(list[i+1])
  
  return new_list

if __name__ == "__main__":
  my_list = ["first", "second", "fourth", "eleventh"]
  result = all_the_longest(my_list)
  print(result) # ['eleventh']
  
  my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
  result = all_the_longest(my_list)
  print(result) # ['dorothy', 'richard']