class Solution(object):

    def return_string(self,A):

        len_A = len(A)
        string = ""
        for i in range(len_A):
            if (A[i] != "#"):
                string = string + A[i]
            else:
                string = string[0:-1]

        return string

    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        string_S = self.return_string(S)
        string_T = self.return_string(T)

        if string_S == string_T:
            return True
        else:
            return False



# TEST CASES
sol = Solution()

# test1
# S = "abc" T = "abc" EO = True
S = "abc"
T = "abc"
if (sol.backspaceCompare(S,T) == True):
    print "Test1 passed"
else:
    print "Test1 failed"

# test2
# S = "abc" T = "abd#c" EO = True
S = "abc"
T = "abd#c"
if (sol.backspaceCompare(S,T) == True):
    print "Test2 passed"
else:
    print "Test2 failed"

# test3
# S = "123#456" T = "1#2#3#12456" EO = True
S = "123#456"
T = "1#2#3#12456"
if (sol.backspaceCompare(S,T) == True):
    print "Test3 passed"
else:
    print "Test3 failed"
