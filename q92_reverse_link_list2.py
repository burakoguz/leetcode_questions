# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        cur = head
        first = None
        second = None

        print head
        print head.next
        print head.next.next
        print head.next.next.next
        print head.next.next.next.next

        if m == n:                      # No swap
            return head
        elif head.next == None:         # Empty linked list
            return head
        elif head.next.next == None:    # One member linked list
            return head
        else:
            count = 1
            # while cur.next != None:
            while (first is None) or (second is None):

                if count + 1 == m:
                    first = cur

                if count + 1 == n:
                    second = cur

                # print "Count = {} and first = {} and second = {}".format(count,first,second)

                count += 1

                cur = cur.next

                if cur == None:
                    break

            print "first = {}".format(first)
            print "second = {}".format(second)

            tmp1 = first
            tmp1_n = first.next

            tmp2 = second
            tmp2_n = second.next.next

            print "tmp1 = {}".format(tmp1)
            print "tmp2 = {}".format(tmp2)
            print "tmp1_n = {}".format(tmp1_n)
            print "tmp2_n = {}".format(tmp2_n)

            # first.next = None
            first.next = tmp2
            first.next.next = tmp1_n

            # second.next = None
            second.next = tmp1
            second.next.next = tmp2_n

        print head
        print head.next
        print head.next.next
        print head.next.next.next
        print head.next.next.next.next
        return head


# TEST CASES
sol = Solution()

#test1
# m = 1
# n = 2
# head = ListNode(3)
# head.next = ListNode(5)
# head.next.next = ListNode(None)
#
# new_head = sol.reverseBetween(head,m,n)
# print new_head.val
# print new_head.next.val
#
# if new_head.val == 5 and new_head.next.val == 3 and new_head.next.next == None:
#     print "Test1 passed"
# else:
#     print "Test1 failed"


#test2
m = 2
n = 4
head = ListNode(3)
head.next = ListNode(5)
head.next.next = ListNode(7)
head.next.next.next = ListNode(9)
head.next.next.next.next = ListNode(11)
head.next.next.next.next.next = ListNode(None)

new_head = sol.reverseBetween(head, m, n)
print new_head.val
print new_head.next.val
print new_head.next.next.val
print new_head.next.next.next.val

if new_head.val == 3 and new_head.next.val == 9 and new_head.next.next.val == 7 and \
   new_head.next.next.val == 5 and new_head.next.next.next.val == 11 and new_head.next.next.next.next == None:
    print "Test2 passed"
else:
    print "Test2 failed"

