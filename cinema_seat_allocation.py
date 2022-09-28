# A cinema has n rows of seats, numbered from 1 to n and there are ten seats in each row, labelled from 1 to 10 as shown in the figure above.

# Given the array reservedSeats containing the numbers of seats already reserved, for example, reservedSeats[i] = [3,8] means the seat located 
# in row 3 and labelled with 8 is already reserved.

# Return the maximum number of four-person groups you can assign on the cinema seats. A four-person group occupies four adjacent seats in one 
# single row. Seats across an aisle (such as [3,3] and [3,4]) are not considered to be adjacent, but there is an exceptional case on which an
# aisle split a four-person group, in that case, the aisle split a four-person group in the middle, which means to have two people on each side.

 

# Example 1:



# Input: n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
# Output: 4
# Explanation: The figure above shows the optimal allocation for four groups, where seats mark with blue are already reserved and contiguous seats 
#   mark with orange are for one group.
# Example 2:

# Input: n = 2, reservedSeats = [[2,1],[1,8],[2,6]]
# Output: 2
# Example 3:

# Input: n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
# Output: 4

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        
        reservedSeats.sort()
        maxGroupSeats = 0
        rowCount = 1
        
        # 1st case = the seats between 2 - 5 and 6 - 9 is max
        # 2nd case = the seats between 4 - 7 is max or between 2 - 5 or between 6 - 9

        # seats between 2 - 5
        firstGroupDisrupted = False
        # seats between 6 - 9
        secondGroupDisrupted = False
        # seats between 4 - 7
        thirdGroupDisrupted = False
        
        if len(reservedSeats) != 0:
            if rowCount != reservedSeats[0][0]:
                maxGroupSeats += ((reservedSeats[0][0] - rowCount) * 2)
                rowCount = reservedSeats[0][0]
            
        
        for i in range(len(reservedSeats)):
            row = reservedSeats[i][0]
            seat = reservedSeats[i][1]

            if seat >= 2 and seat <= 5:
                firstGroupDisrupted = True
            if seat >= 6 and seat <= 9:
                secondGroupDisrupted = True
            if seat >= 4 and seat <= 7:
                thirdGroupDisrupted = True

            # check if the next reserved row is not the row we are currently analyzing
            if i == len(reservedSeats) - 1 or (i != len(reservedSeats) - 1 and reservedSeats[i+1][0] != row):
                # print("NEXT RESERVED ROW: ", reservedSeats[i+1][0])
                if not firstGroupDisrupted and not secondGroupDisrupted and not thirdGroupDisrupted:
                    maxGroupSeats += 2
                elif not firstGroupDisrupted:
                    maxGroupSeats += 1
                elif not secondGroupDisrupted:
                    maxGroupSeats += 1
                elif not thirdGroupDisrupted:
                    maxGroupSeats += 1

                # reset the identifiers
                firstGroupDisrupted = False
                secondGroupDisrupted = False
                thirdGroupDisrupted = False

                if i != len(reservedSeats) - 1:
                    # bring the row count to the next reserved row, adding 2 max for each qualified row
                    rowCount += 1
                    while rowCount != reservedSeats[i+1][0]:
                        maxGroupSeats += 2
                        rowCount += 1
                            
        
        if rowCount != n:
            maxGroupSeats += ((n - rowCount) * 2)           
                        
                        
        return maxGroupSeats
                    
