def palindromes(word):
  if word == word[::-1]:
    return True
  return False

while True:
  word = input("Please type in a palindrome: ")
  if palindromes(word):
    break
  print("that wasn't a palindrome")
print(word + " is a palindrome!")
  

if __name__ == "__main__":
  palindromes("abcde")