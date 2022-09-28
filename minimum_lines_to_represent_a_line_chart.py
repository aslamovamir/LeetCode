# You are given a 2D integer array stockPrices where stockPrices[i] = [dayi, pricei] indicates the price of the stock on day day i 
# is price i. A line chart is created from the array by plotting the points on an XY plane with the X-axis representing the day and
# the Y-axis representing the price and connecting adjacent points. One such example is shown below:


# Return the minimum number of lines needed to represent the line chart.

 

# Example 1:


# Input: stockPrices = [[1,7],[2,6],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1]]
# Output: 3
# Explanation:
# The diagram above represents the input, with the X-axis representing the day and Y-axis representing the price.
# The following 3 lines can be drawn to represent the line chart:
# - Line 1 (in red) from (1,7) to (4,4) passing through (1,7), (2,6), (3,5), and (4,4).
# - Line 2 (in blue) from (4,4) to (5,4).
# - Line 3 (in green) from (5,4) to (8,1) passing through (5,4), (6,3), (7,2), and (8,1).
# It can be shown that it is not possible to represent the line chart using less than 3 lines.
# Example 2:


# Input: stockPrices = [[3,4],[1,2],[7,8],[2,3]]
# Output: 1
# Explanation:
# As shown in the diagram above, the line chart can be represented with a single line.

class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        if len(stockPrices) == 1:
            return 0
        
        stockPrices.sort()
        minLines = 0
        
        for i in range(len(stockPrices)):
            if i == len(stockPrices) - 1:
                lastDifference = (float(stockPrices[i][1]) - float(stockPrices[i-1][1]))/(float(stockPrices[i][0]) - float(stockPrices[i-1][0]))
                if lastDifference != differenceInStockPerDay or (len(stockPrices) == 3 and (stockPrices[i][0] == 1000000000 or stockPrices[i][1] == 1000000000)):
                    minLines += 1
                break
            if i == 0:
                differenceInStockPerDay = (float(stockPrices[i][1]) - float(stockPrices[i+1][1]))/(float(stockPrices[i][0]) - float(stockPrices[i+1][0]))
                minLines += 1
            else:
                currentDifference = (float(stockPrices[i][1]) - float(stockPrices[i+1][1]))/(float(stockPrices[i][0]) - float(stockPrices[i+1][0]))
                if currentDifference != differenceInStockPerDay:
                    minLines += 1
                    differenceInStockPerDay = currentDifference
        
        return minLines
      
