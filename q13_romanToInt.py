
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_numbers = {"M": 1000, "D" : 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        converted_int = 0

        reverse_case_detected = False


        s_len = len(s)

        for i in range(s_len):
            if reverse_case_detected:
                reverse_case_detected = False
            else:

                # Find small big sequences
                first = s[i]
                first_num = roman_numbers[first]
                second_num = 0

                if s_len - i > 1:
                    second = s[i+1]
                    second_num = roman_numbers[second]

                # print "first_num = {}, second_num = {}".format(first_num, second_num)

                if (first_num != 0 and second_num != 0) and (first_num < second_num):
                    # Reverse case detected
                    converted_int += second_num - first_num
                    reverse_case_detected = True
                elif first_num != 0 and second_num != 0:
                    # Accumulate normal numbers
                    converted_int += first_num
                elif first_num != 0:
                    converted_int += first_num


        return converted_int


# TEST CASES
sol = Solution()

# test1
# input = "III" output = 3
if sol.romanToInt("III") == 3:
    print "Test1 passed"
else:
    print "Test1 failed"

# test2
# input = "IV" output = 4
if sol.romanToInt("IV") == 4:
    print "Test2 passed"
else:
    print "Test2 failed"

# test3
# input = "MCMLXXVII" output = 1977
if sol.romanToInt("MCMLXXVII") == 1977:
    print "Test3 passed"
else:
    print "Test3 failed"

# test4
# input = "" output = 0
if sol.romanToInt("") == 0:
    print "Test4 passed"
else:
    print "Test4 failed"

