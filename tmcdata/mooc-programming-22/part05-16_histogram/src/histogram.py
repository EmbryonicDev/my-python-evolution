def histogram(string):
  groups = {}

  for letter in string:
    if letter not in groups:
      groups[letter] = []
    groups[letter].append('*')
    
  for key, value in groups.items():
    print(key,end=' ')
    for star in value:
      print(star,end='')
    print()
    
# model solution:
# def histogram(my_str: str):
#     characters = {}
#     for character in my_str:
#         if not character in characters:
#             characters[character] = 0
#         characters[character] += 1
 
#     for character, lkm in characters.items():
#         stars = "*"*lkm
#         print(f"{character} {stars}")

if __name__ == "__main__":
  histogram("abba")
  histogram("statistically")