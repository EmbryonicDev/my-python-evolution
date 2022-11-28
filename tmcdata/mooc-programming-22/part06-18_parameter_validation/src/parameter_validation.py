def new_person(name: str, age: int):
    # validate name
    if (len(name) > 40 or len(name) < 1 or
        " " not in name):
        raise ValueError("Invalid argument value for name: " + name)
    
    # validate age
    if age < 0 or age > 150:
        raise ValueError("Invalid argument value for age: " + str(age))
    
    # no error:
    return (name, age)

  
if __name__ == "__main__":
  print(new_person('Andrew', 32))
  