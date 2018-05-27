

# Remove duplicates from given sorted array nums and return the result array lenght

def remove_duplicates_from_sorted_array(sorted_input_arr):
  # Take sorted input array
  i_prev = ""
  count  = 0

  for i in sorted_input_arr:

    # find uniq elements
    if not (i == i_prev):
        # Count the uniq elements
        sorted_input_arr[count] = i
        count += 1


    i_prev = i

  # Return count of uniq elements
  return count



# test behaviour
# test1 : no duplicates
sorted_array = [0,1,2,3]
print remove_duplicates_from_sorted_array(sorted_array)

# test2 : duplicates
sorted_array = [0,0,1,1,2,2,3,3,4,4]
print remove_duplicates_from_sorted_array(sorted_array)

# test3: empty
sorted_array = []
print remove_duplicates_from_sorted_array(sorted_array)

# test4: not sequential
sorted_array = [0,0,3,3,3,5,5,7,8,8,10,10,10,10]
print remove_duplicates_from_sorted_array(sorted_array)

