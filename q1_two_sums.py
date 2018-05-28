

# Return the indices of two integers that sums up target value
# input1 array of integers
# input2 sum target value
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_len = len(nums)

        ret_val = []

        if not nums_len == 0:
            ### # For-else first time seen from one user from stackoverflow
            ### # if for not break, continue
            ### for i in range(nums_len):
            ###     for j in range(i+1,nums_len):
            ###         # print "nums[i] = {} + nums[j] = {} =? target = {}".format(nums[i],nums[j],target)
            ###         if nums[i] + nums[j] == target:
            ###             ret_val = [i,j]
            ###             break
            ###     else:
            ###         continue
            ###
            ###     break

            for i in range(nums_len):
                search_item = target - nums[i]
                # print "nums[i] = {} and search_item = {}".format(nums[i], search_item)
                if (search_item in nums) and (nums.index(target-nums[i]) != i):
                    ret_val = [i,nums.index(search_item)]
                    break

        return ret_val


# Test Cases
sol = Solution()

# Test1
# input1 = [1,2,3,4,5,6] input2 = 11 expected_output = [4,5]
if sol.twoSum([1,2,3,4,5,6],11) == [4,5]:
    print "Test1 passed"
else:
    print "Test1 failed"

# Test2
# input1 = [1,2,4,9,8,3] input2 = 7 expected_output = [2,5]
if sol.twoSum([1,2,4,9,8,3],7) == [2,5]:
    print "Test2 passed"
else:
    print "Test2 failed"

# Test3
# input1 = [] input2 = 3 expected_output = []
if sol.twoSum([],3) == []:
    print "Test3 passed"
else:
    print "Test3 failed"

