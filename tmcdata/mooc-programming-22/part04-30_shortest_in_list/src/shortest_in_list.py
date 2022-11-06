def shortest(list):
  shortest = list[0]
  
  for i in range(len(list) - 1):
    if len(list[i+1]) < len(shortest):
      shortest = list[i+1]
      
  return shortest

if __name__ == "__main__":
  my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

  result = shortest(my_list)
  print(result)