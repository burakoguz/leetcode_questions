class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        result = False

        len_A = len(A)
        len_B = len(B)

        if len_A != len_B:
            result = False
        else:

            if len_A == 0:
                result = False
            elif len_A == 1:
                result = True
            else:
                for i in range(len_B - 1):
                    C = list(A)
                    C[i+1] = A[i]
                    C[i]   = A[i+1]
                    if ''.join(C) == B:
                        result = True
                        break

        return result


# TEST CASES
sol = Solution()


#test 1
A = "ab"
B = "ba"

if sol.buddyStrings(A,B) == True:
    print "Test1 passed"
else:
    print "Test1 failed"

#test 2
A = "ab"
B = "ab"

if sol.buddyStrings(A,B) == False:
    print "Test2 passed"
else:
    print "Test2 failed"

#test 3
A = ""
B = "ba"

if sol.buddyStrings(A,B) == False:
    print "Test3 passed"
else:
    print "Test3 failed"

#test 4
A = "aaaaaaabc"
B = "aaaaaaacb"

if sol.buddyStrings(A,B) == True:
    print "Test4 passed"
else:
    print "Test4 failed"

# test 5
A = "abab"
B = "abab"

if sol.buddyStrings(A,B) == False:
    print "Test5 passed"
else:
    print "Test5 failed"

