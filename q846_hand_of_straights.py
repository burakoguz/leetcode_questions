class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        result = False

        # Pseudo Code
        # 1. find whether W * W element present in List
        # 2. find min search for consecutive W-1 element
        # 3. Take other elements and do 2. step
        # 4. Check W * W groups

        len_hand = len(hand)
        divided_hand = [[0 for j in range(W)] for i in range(W)]

        if len_hand < W * W:
            result = False
        elif W == 1 and len_hand != 0:
            result = True # 1x1 is always possible
        else:
            sorted_hand = sorted(hand)
            for i in range(W):
                divided_hand[i][0] = min(sorted_hand)
                sorted_hand.remove(divided_hand[i][0])
                print "##################"
                print divided_hand[i][0]
                print sorted_hand
                for j in range(W-1):
                    print divided_hand[i][j] + 1
                    print sorted_hand
                    if not (divided_hand[i][j] + 1) in sorted_hand:
                        result = False
                        break
                    else:
                        divided_hand[i][j+1] = divided_hand[i][j] + 1
                        sorted_hand.remove(divided_hand[i][j] + 1)
                        # print sorted_hand
                        result = True

        return result


# TEST CASES
sol = Solution()

# test1
hand = [1, 2, 3, 4, 5, 6, 7, 8, 9]
W = 3
if sol.isNStraightHand(hand,W):
    print "Test1 passed"
else:
    print "Test1 failed"

# test2
hand = [1, 2, 3, 4, 5, 6, 7, 8, 10]
W = 3
if not sol.isNStraightHand(hand,W):
    print "Test2 passed"
else:
    print "Test2 failed"

# test3
hand = [1, 2, 5, 6]
W = 2
if sol.isNStraightHand(hand,W):
    print "Test3 passed"
else:
    print "Test3 failed"

# test4
hand = [1,2,3,4,5,6]
W = 2
if sol.isNStraightHand(hand,W):
    print "Test4 passed"
else:
    print "Test4 failed"

# test5
hand = [1,2,3]
W = 1
if sol.isNStraightHand(hand,W):
    print "Test5 passed"
else:
    print "Test5 failed"


