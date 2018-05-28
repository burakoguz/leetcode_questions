
# Reverse the digits of an integer
# if it is signed, keep the sign
# if there are zero(s) at the beginning, remove them

class Solution(object):
    def reverseInteger(self,x):

        inverted_x = 0
        y = x
        sign = ""
        rem = 0

        if x < 0:
            sign = "-"
            y = abs(x)
        if x == 0:
            inverted_x = x
        else:
            while y >= 10:
                rem = y % 10
                y = y / 10
                inverted_x = inverted_x * 10 + rem

            inverted_x = inverted_x * 10 + y

        if (inverted_x > 2 ** 31):
            inverted_x = 0
        elif (sign == "-"):
            inverted_x = -inverted_x

        return inverted_x




# TEST CASES
sol = Solution()

# test1
# x = 123 , expected output = 321
if (sol.reverseInteger(123) == 321):
    print "Test1 passed"
else:
    print "Test1 failed"

# test2
# x = -123 , expected output = -321
if (sol.reverseInteger(-123) == -321):
    print "Test2 passed"
else:
    print "Test2 failed"

# test3
# x = 0 , expected output = 0
if (sol.reverseInteger(0) == 0):
    print "Test3 passed"
else:
    print "Test3 failed"

