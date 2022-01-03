# You are given a phone number as a string number. number consists of digits, spaces ' ', and/or dashes '-'.

# You would like to reformat the phone number in a certain manner. Firstly, remove all spaces and dashes. Then, group the digits from left to 
# right into blocks of length 3 until there are 4 or fewer digits. The final digits are then grouped as follows:

# 2 digits: A single block of length 2.
# 3 digits: A single block of length 3.
# 4 digits: Two blocks of length 2 each.
# The blocks are then joined by dashes. Notice that the reformatting process should never produce any blocks of length 1 and produce at most 
# two blocks of length 2.

# Return the phone number after formatting.
# Example 1:

# Input: number = "1-23-45 6"
# Output: "123-456"
# Explanation: The digits are "123456".
# Step 1: There are more than 4 digits, so group the next 3 digits. The 1st block is "123".
# Step 2: There are 3 digits remaining, so put them in a single block of length 3. The 2nd block is "456".
# Joining the blocks gives "123-456".
# Example 2:

# Input: number = "123 4-567"
# Output: "123-45-67"
# Explanation: The digits are "1234567".
# Step 1: There are more than 4 digits, so group the next 3 digits. The 1st block is "123".
# Step 2: There are 4 digits left, so split them into two blocks of length 2. The blocks are "45" and "67".
# Joining the blocks gives "123-45-67".
# Example 3:

# Input: number = "123 4-5678"
# Output: "123-456-78"
# Explanation: The digits are "12345678".
# Step 1: The 1st block is "123".
# Step 2: The 2nd block is "456".
# Step 3: There are 2 digits left, so put them in a single block of length 2. The 3rd block is "78".
# Joining the blocks gives "123-456-78".

class Solution:
    def reformatNumber(self, number: str) -> str:
        # first let's filter the number from the whitespace and any dashes
        filtered = []
        
        for digit in number:
            if digit != ' ' and digit != '-':
                filtered.append(digit)
        
        answer = ""
        
        # if there are only 2 or 3 digits, we just return a string of those digits
        if len(filtered) == 2 or len(filtered) == 3:
            size = 2 if len(filtered) == 2 else 3
            for i in range(0, size):
                answer += filtered[i]
            return answer
        
        # let's check if the number of digits is eqaul to 4 or not
        if len(filtered) == 4:
            for i in range(0, len(filtered)):
                if i == 2:
                    answer += '-'
                answer += filtered[i]
            return answer
        else:
            # let's determine how many groups of 3 we can make
            groups_3 = len(filtered)//3
            # get the left over
            left = len(filtered)%3
            # we cannot have a left over of 1, so we change the values of the variables above
            if left == 1:
                groups_3 = groups_3-1
                left += 3  
        
            # let's get the groups of 3 first
            # indicator variable will determine when we have to append a dash 
            # when it == 3, we know we need a dash
            indicator = 0
            # we will loop until we get perfect groups of 3
            for i in range(0, groups_3*3):
                if indicator == 2:
                    answer += filtered[i]
                    answer += '-'
                    indicator = 0
                    continue
                answer += filtered[i]
                indicator += 1
            # if we don't have any left over, we just return the answer we got so far
            if left == 0:
                return answer[:len(answer)-1]
            
            # if the left over is 2, we just append a group of two
            if left == 2:
                answer += filtered[len(filtered)-2]
                answer += filtered[len(filtered)-1]
                return answer
            elif left == 4:
                left_over = filtered[len(filtered)-4:]
                for i in range(0, len(left_over)):
                    if i == 2:
                        answer += '-'
                    answer += left_over[i]
                    
                return answer      
              
              
