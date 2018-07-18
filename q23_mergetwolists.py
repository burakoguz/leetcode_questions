# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        mergedList = ListNode()

        next = l1.next

        while next is not None:
            if (l1.val < l2.val):
                mergedList = l1
                next = l1.next
                if l1.next is None:
                    next = l2.next
            else:
                mergedList = l2
                next = l2.next



        return mergedList


# Test Cases
sol = Solution()

l1[0] = ListNode(1)
l1[1] = ListNode(2)
l1[2] = ListNode(4)
l1[0].next = l1[1]
l1[1].next = l1[2]

l2[0] = ListNode(1)
l2[1] = ListNode(2)
l2[2] = ListNode(3)
l2[0].next = l2[1]
l2[1].next = l2[2]

exp_out[0] = ListNode(1)
exp_out[1] = ListNode(1)
exp_out[2] = ListNode(2)
exp_out[0] = ListNode(2)
exp_out[1] = ListNode(3)
exp_out[2] = ListNode(4)

exp_out[0].next = exp_out[1]
exp_out[1].next = exp_out[2]
exp_out[2].next = exp_out[3]
exp_out[3].next = exp_out[4]
exp_out[4].next = exp_out[5]

if sol.mergeTwoLists(l1[0],l2[0]) == exp_out[0]:
    print "Test1 passed"
else:
    print "Test1 failed"

