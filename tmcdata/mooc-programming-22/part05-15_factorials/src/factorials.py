def factorials(n: int):
  result = {}
  result[1] = 1
  
  for i in range(2, n + 1):
    result[i] = result[i-1] * i

  return result
    

if __name__ == "__main__":
  k = factorials(5)
  print(k[1])
  print(k[3])
  print(k[5])