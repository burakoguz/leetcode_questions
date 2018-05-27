

def search_arr_return_index(nums, target):
  index = -1

  if (nums == []):
    # Do nothing
    index = -1
  else:
    nums_len = len(nums)
    for i in range(nums_len / 2 + 1):
      a = nums[i]
      b = nums[nums_len - i - 1]
      if (a == target or b == target):
        if (a == target):
          index = i
          break
        if (b == target):
          index = nums_len - i - 1
          break
      elif (a > target):
        if (b < target):
          # Not found
          break
        else:
          # Do nothing
          next
      elif (a < target):
        # Do nothing
        next

  return index

###################################################################################################
# Test input & outputs

# test1
# nums = [3,4,5,0,1,2], target=1 => out= 4
if (search_arr_return_index([3,4,5,0,1,2], 1) == 4):
  print "Test1 passed"
else:
  print "Test1 failed"

# test2
# nums = [3,4,5,0,1,2], target=6 => out= -1
if (search_arr_return_index([3,4,5,0,1,2], 6) == -1):
  print "Test2 passed"
else:
  print "Test2 failed"

# test3
# nums = [], target=6 => out= -1
if (search_arr_return_index([], 6) == -1):
  print "Test3 passed"
else:
  print "Test3 failed"

# test4
# nums = [5,7,9,1,3], target=7 => out= 1
if (search_arr_return_index([5,7,9,1,3], 7) == 1):
  print "Test4 passed"
else:
  print "Test4 failed"
