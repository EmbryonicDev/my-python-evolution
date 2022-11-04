def list_of_stars(list):
  for number in list:
    print("*" * number)
  
if __name__ == "__main__":
  list = [3,7,1,1,2]
  list_of_stars(list)