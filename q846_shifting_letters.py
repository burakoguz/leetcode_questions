class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """

        len_shifts = len(shifts)
        new_S = list(S)

        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        # Take shifts numbers
        for i in range(len_shifts-2,-1,-1):
            shifts[i] = (shifts[i] + shifts[i+1]) % 26

        for k in range(len_shifts):
            # Find new shifted characters
            new_S[k] = alphabet[(alphabet.index(new_S[k]) + shifts[k]) % 26]
        return "".join(new_S)



# TEST CASES
sol = Solution()


# test1
S = "abc"
shifts = [3,5,9]
# EO = "rpl"
if sol.shiftingLetters(S,shifts) == "rpl":
    print "Test1 passed"
else:
    print "Test1 failed"
