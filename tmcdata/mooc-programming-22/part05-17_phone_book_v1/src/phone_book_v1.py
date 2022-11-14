def search(persons: dict):
    name = input("name: ")
    if name not in persons:
      print("no number")
    else:
      print(persons[name])
      
def add(persons: dict):
    name = input("name: ")
    number = input("number: ")
    persons[name] = number
    print("ok!")
      
def main():
  persons = {}
  while True:
    command = int(input("command (1 search, 2 add, 3 quit): "))
    if command == 1:
      search(persons)
    if command == 2:
      add(persons)
    if command == 3:
      break
  print("quitting...")
  
main()
    

  
    
    
    
  
  

