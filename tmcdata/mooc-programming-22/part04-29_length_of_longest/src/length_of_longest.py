def length_of_longest(list):
  longest = len(list[0])
  
  for i in range(len(list) - 1):
    if len(list[i+1]) > longest:
      longest = len(list[i+1])
      
  return longest
  

if __name__ == "__main__":
  my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
  result = length_of_longest(my_list)
  print(result)