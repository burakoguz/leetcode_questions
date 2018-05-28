

# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

class Solution(object):
    def isPalindrome(self,x):
        # input is integer, output is boolean

        result = False

        if x < 0:
            result = False
        elif x == 0:
            result = True
        else:
            for i in range(11):
                if (x >= 10 ** i) and (x < 10 ** (i+1)):
                    digits_in_integer = i + 1

            for j in range((digits_in_integer+1)/2):
                digitn_divider = 10 ** (digits_in_integer - 1 - (j * 2))
                digitn = x / digitn_divider
                digit1 = x % 10
                x = (x - (digitn * digitn_divider) - digit1) / 10
                if digit1 == digitn:
                    result = True
                else:
                    result = False
                    break


        return result



# TEST CASES
sol = Solution()

# test1
# input = 0, expected output = True
if sol.isPalindrome(0):
    print "Test1 passed"
else:
    print "Test1 failed"

# test2
# input = 121, expected output = True
if sol.isPalindrome(121):
    print "Test2 passed"
else:
    print "Test2 failed"

# test3
# input = -121. expected output = False
if not sol.isPalindrome(-121):
    print "Test3 passed"
else:
    print "Test3 failed"

# test4
# input = 234565432, expected output = True
if sol.isPalindrome(234565432):
    print "Test4 passed"
else:
    print "Test4 failed"
