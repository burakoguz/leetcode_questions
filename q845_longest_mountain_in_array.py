class Solution(object):

    def findFirstMountain(self, B):
        mountain_length = 0
        mountain_last = 0
        increase_detected = False
        decrease_detected = False

        len_B = len(B)

        for i in range(len_B-1):
            mountain_last = i

            # print "B[i] = {} and B[i+1] = {}".format(B[i], B[i+1])

            if increase_detected and decrease_detected:
                # print "##################################################################################"
                # print "mountain_length = {} after increase and decrease detected".format(mountain_length)
                # print "B[i] = {} and B[i+1] = {}".format(B[i], B[i+1])
                if B[i] > B[i+1]:
                    mountain_length += 1
                else:
                    # Mountain found?
                    if mountain_length >= 3:
                        break
                    else:
                        mountain_length = 0
                        increase_detected = False
                        decrease_detected = False

            elif increase_detected:
                if B[i] < B[i+1]:
                    mountain_length += 1
                elif B[i] > B[i+1]:
                    decrease_detected = True
                    mountain_length += 1

            elif B[i] < B[i+1]:
                # possible mountain
                increase_detected = True
                mountain_length = 2

            if B[i] == B[i+1]:
                increase_detected = False
                decrease_detected = False
                if not mountain_length >= 3:
                    mountain_length = 0

            # print "mountain_lenght = {}".format(mountain_length)
            # print "increase_detected = {} and decrease_detected = {}".format(increase_detected, decrease_detected)

        if increase_detected and decrease_detected and mountain_length >=3:
            return [mountain_length, mountain_last]
        else:
            return [0, mountain_last]



    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        longest_mountain_length = 0
        i = 0
        len_A = len(A)

        # find first mountain
        [mountain_length, mountain_last] = self.findFirstMountain(A)
        i = mountain_last

        while i < len_A:
            # print "mountain_length = {} and mountain_last = {}".format(mountain_length, mountain_last)
            # print i

            if mountain_last == 0:
                break

            # check whether it is longest
            if mountain_length > longest_mountain_length:
                longest_mountain_length = mountain_length

            # find another mountain if any
            [mountain_length, mountain_last] = self.findFirstMountain(A[i:])
            i += mountain_last

        return longest_mountain_length


# TEST CASES
sol = Solution()

# test1
# EO = 0
A = [1,2,3,4,5]
if sol.longestMountain(A) == 0:
    print "Test1 passed"
else:
    print "Test1 failed"

# test2
# EO = 3
A = [1,2,1,4,5]
if sol.longestMountain(A) == 3:
    print "Test2 passed"
else:
    print "Test2 failed"

# test3
# EO = 5
A = [1,2,1,4,5,6,5,4]
if sol.longestMountain(A) == 6:
    print "Test3 passed"
else:
    print "Test3 failed"

# test4
# EO = 0
A = []
if sol.longestMountain(A) == 0:
    print "Test4 passed"
else:
    print "Test4 failed"

# test5
A = [875,884,239,731,723,685]
if sol.longestMountain(A) == 4:
    print "Test5 passed"
else:
    print "Test5 failed"

# test6
A = [0,0,1,0,0,1,1,1,1,1]
if sol.longestMountain(A) == 3:
    print "Test6 passed"
else:
    print "Test6 failed"


