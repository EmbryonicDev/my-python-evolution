def most_common_character(string):
  highest_count = 'string[0]'
  
  for letter in string:
    if string.count(letter) > string.count(highest_count):
      highest_count = letter
    
  return highest_count
    
  
if __name__ == "__main__":
  first_string = "abcdbde"
  print(most_common_character(first_string))

  second_string = "exemplaryelementary"
  print(most_common_character(second_string))