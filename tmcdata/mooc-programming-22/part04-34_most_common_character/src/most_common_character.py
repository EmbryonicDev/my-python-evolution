def most_common_character(string):
  highest_count = ''
  
  for i in range(len(string)):
    if highest_count == '':
      highest_count = string[i]
    elif string.count(string[i]) > string.count(highest_count):
      highest_count = string[i]
    
  return highest_count
    
  
if __name__ == "__main__":
  first_string = "abcdbde"
  print(most_common_character(first_string))

  second_string = "exemplaryelementary"
  print(most_common_character(second_string))