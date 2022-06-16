# Each person takes exactly 1 second to buy a ticket. A person can only buy 1 ticket at a time and has to go back to the 
# end of the line (which happens instantaneously) in order to buy more tickets. If a person does not have any tickets left
# to buy, the person will leave the line.

# Return the time taken for the person at position k (0-indexed) to finish buying tickets.

 

# Example 1:

# Input: tickets = [2,3,2], k = 2
# Output: 6
# Explanation: 
# - In the first pass, everyone in the line buys a ticket and the line becomes [1, 2, 1].
# - In the second pass, everyone in the line buys a ticket and the line becomes [0, 1, 0].
# The person at position 2 has successfully bought 2 tickets and it took 3 + 3 = 6 seconds.
# Example 2:

# Input: tickets = [5,1,1,1], k = 0
# Output: 8
# Explanation:
# - In the first pass, everyone in the line buys a ticket and the line becomes [4, 0, 0, 0].
# - In the next 4 passes, only the person in position 0 is buying tickets.
# The person at position 0 has successfully bought 5 tickets and it took 4 + 1 + 1 + 1 + 1 = 8 seconds.

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        counter = 0
        stop = False
        while not stop:
            for i in range(len(tickets)):
                if tickets[k] == 0:
                    stop = True
                    break
                if tickets[i] == 0:
                    continue
                else:
                    tickets[i] = tickets[i] - 1
                    counter += 1
        
        return counter
      
