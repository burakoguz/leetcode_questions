class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """

        result = 0
        total = 0
        length = 0
        seat_prev = -1

        # find 0, if no 0 then all seats are taken return 0
        if not 0 in seats:
            result = 0
        else:
            len_seats = len(seats)
            for i in range(len_seats):

                seat = seats[i]

                # find distance for all 0s (forward and backward)
                if i == 0:
                    length = 0
                elif (seat == 0) or (seat == 1 and seat_prev == 0):
                    length += 1
                else:
                    length = 0

                total += seat
                print "length = {}, total = {}, result = {}".format(length, total, result)

                if total == 2:
                    temp_result = length / 2
                    if temp_result > result:
                        result = temp_result

                    total = 1
                    length = 0

                # End with zero
                elif total == 1 and seat == 0 and i == len_seats - 1:
                    temp_result = length

                    if temp_result > result:
                        result = temp_result

                # Start with zero
                elif total == 1 and seats[0] == 0 and seat == 1:
                    temp_result = length

                    if temp_result > result:
                        result = temp_result

                seat_prev = seat

                if seat == 1 and i != len_seats - 1:
                    length = 0

        print "result = {}".format(result)
        return result

# TEST CASES
sol = Solution()

# test1
seats = [1, 0, 0, 0] # EO = 3
if sol.maxDistToClosest(seats) == 3:
    print "Test1 passed"
else:
    print "Test1 failed"

# test2
seats = [1, 0, 0, 0, 1, 0, 1] # EO = 2
if sol.maxDistToClosest(seats) == 2:
    print "Test2 passed"
else:
    print "Test2 failed"

# test3
seats = [] # EO = 0
if sol.maxDistToClosest(seats) == 0:
    print "Test3 passed"
else:
    print "Test3 failed"

# test4
seats = [0, 1] # EO = 0
if sol.maxDistToClosest(seats) == 1:
    print "Test4 passed"
else:
    print "Test4 failed"

# test5
seats = [0,1,0,0,0,0] # EO = 4
if sol.maxDistToClosest(seats) == 4:
    print "Test5 passed"
else:
    print "Test5 failed"

# test6
seats = [0,0,1,0,1,1] # EO = 2
# seats = [0,0,1] # EO = 2
if sol.maxDistToClosest(seats) == 2:
    print "Test6 passed"
else:
    print "Test6 failed"

