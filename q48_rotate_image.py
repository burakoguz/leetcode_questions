######################################
# NxN matrix image
# turn clockwise 90 degree
# do not allocate another NxN matrix (in-pace change)

def rotate_90_degrees_clockwise(matrix):
    # find center for N (center is matrix[center,center])
    N = len(matrix)
    if N % 2 == 1:
        center = (N + 1) / 2.0
    else:
        center = (N + 2) / 2.0

    i = 0
    j = 0

    # rotate one by one each cell
    for loop_var1 in range(int(center-1)):
        for loop_var2 in range(N - 1 - 2 * loop_var1):
            i = loop_var1
            j = loop_var1+loop_var2
            temp = ""
            temp2 = ""
            for loop_var3 in range(4):
                # do rotation by assigning each cell value to temp value
                # matrix[i,j] will be matrix[new_loc_x,new_loc_y]
                # each loop 4 times because matrix has 4 edges
                new_loc_y = N - i - 1
                new_loc_x = j
                if temp == "":
                    temp = matrix[new_loc_x][new_loc_y]
                    matrix[new_loc_x][new_loc_y] = matrix[i][j]
                else:
                    temp2 = matrix[new_loc_x][new_loc_y]
                    matrix[new_loc_x][new_loc_y] = temp
                    temp = temp2


                i = new_loc_x
                j = new_loc_y


    return matrix # for leetcode, remove this return


"""
 1  2  3  4  5      21 16 11  6  1
 6  7  8  9 10      22 17 12  7  2
11 12 13 14 15  =>  23 18 13  8  3
16 17 18 19 20      24 19 14  9  4
21 22 23 24 25      25 20 15 10  5

[0][0] -> [0][4]
[0][4] -> [4][4]
[4][4] -> [4][0]
[4][0] -> [0][0]

[0][1] -> [1][4]
[1][4] -> [3][4]
[3][4] -> [3][0]
[3][0] -> [0][1]

"""
###################
# Test cases

# test1
# inp = [ [1,2,3],[4,5,6],[7,8,9]]
# out = [ [7,4,1],[8,5,2],[9,6,3]]
if (rotate_90_degrees_clockwise([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]):
    print "Test1 passed"
else:
    print "Test1 failed"

# test2
# inp = [ [1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# out = [ [13,9,5,1],[14,10,6,2],[15,11,7,3],[16,12,8,4]]
if (rotate_90_degrees_clockwise([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]) == [[13, 9, 5, 1],
                                                                                                     [14, 10, 6, 2],
                                                                                                     [15, 11, 7, 3],
                                                                                                     [16, 12, 8, 4]]):
    print "Test2 passed"
else:
    print "Test2 failed"

# test3
# inp = [ [1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25] ]
# out = [[21,16,11, 6, 1], [22,17,12, 7, 2], [23,18,13, 8, 3], [24,19,14, 9, 4], [25,20,15,10, 5]]
if (rotate_90_degrees_clockwise(
        [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]) == [
    [21, 16, 11, 6, 1], [22, 17, 12, 7, 2], [23, 18, 13, 8, 3], [24, 19, 14, 9, 4], [25, 20, 15, 10, 5]]):
    print "Test3 passed"
else:
    print "Test3 failed"

# test4
# inp = [ ]
# out = [ ]
if (rotate_90_degrees_clockwise([]) == []):
    print "Test4 passed"
else:
    print "Test4 failed"
