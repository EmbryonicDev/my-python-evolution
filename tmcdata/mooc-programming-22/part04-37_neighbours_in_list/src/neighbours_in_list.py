def longest_series_of_neighbours(list):
  neighbor_count = 1
  neighbor_list = []
  
  for i in range(len(list) - 1):
    if list[i+1] == list[i] - 1 or list[i+1] == list[i] + 1:
      neighbor_count += 1
    else:
      neighbor_count = 1
    neighbor_list.append(neighbor_count)
  
  return max(neighbor_list)
    
  
if __name__ == "__main__":
  # my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
  print(longest_series_of_neighbours(my_list))
  # Sample output
  # 4