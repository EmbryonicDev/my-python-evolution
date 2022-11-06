def no_vowels(string):
  new_string = ''
  vowels = "aeiou"
  
  for letter in string:
    if letter not in vowels:
      new_string += letter
  
  return new_string
  
if __name__ == "__main__":
  my_string = "this is an example"
  print(no_vowels(my_string))
  # Sample output
  # ths s n xmpl