class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        longest_common_pre = ""
        min_len = 2 ** 31
        nr_of_strs = len(strs)

        if (nr_of_strs == 0):
            longest_common_pre
        elif (nr_of_strs == 1):
            longest_common_pre = strs[0]
        else:
            for str in strs:
                len_str = len(str)
                if min_len > len_str:
                    min_len = len_str

            for i in range(min_len):

                char_to_compare = ""

                for j in range(nr_of_strs - 1):
                    # Take char for each of them compare
                    if strs[j][i] == strs[j + 1][i]:
                        char_to_compare = strs[j][i]
                    else:
                        return longest_common_pre

                longest_common_pre += char_to_compare
                # print longest_common_pre

        return longest_common_pre


# TEST CASES
sol = Solution()

# test1
# input = ["abc", "ab", "abcd"] output = "ab"
if (sol.longestCommonPrefix(["abc", "ab", "abcd"]) == "ab"):
    print "Test1 passed"
else:
    print "Test1 failed"

# test2
# input = ["abc", "ef", "abcd"] output = ""
if (sol.longestCommonPrefix(["abc", "ef", "abcd"]) == ""):
    print "Test2 passed"
else:
    print "Test2 failed"

# test3
# input = ["abc", "ab", "abcd"] output = "ab"
if (sol.longestCommonPrefix([""]) == ""):
    print "Test3 passed"
else:
    print "Test3 failed"

