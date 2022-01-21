# You are given a string s of lowercase English letters and an integer array shifts of the same length.

# Call the shift() of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').

# For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
# Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x times.

# Return the final string after all such shifts to s are applied.

 

# Example 1:

# Input: s = "abc", shifts = [3,5,9]
# Output: "rpl"
# Explanation: We start with "abc".
# After shifting the first 1 letters of s by 3, we have "dbc".
# After shifting the first 2 letters of s by 5, we have "igc".
# After shifting the first 3 letters of s by 9, we have "rpl", the answer.
# Example 2:

# Input: s = "aaa", shifts = [1,2,3]
# Output: "gfd"

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        
        # let's create a helper function that shifts a single char
        def shifter(char, shift):
            shift_val = (ord(char) + shift%26)%122
            if shift_val == 0:
                return 'z'
            if shift_val >= 97 and shift_val <= 122:
                new_char = chr(shift_val)
            else:
                new_char = chr(shift_val + 96)
                
            return new_char
        
        
        # main
        # idea: we need to determine how many shifts in total each letter is going to have
        # the first letter will have shifts equal to the total sum of shifts, the second
        # total sum minus the sum of previous shifts
        answer = []
        total = sum(shifts)
        run_sum = 0
        for i in range(len(shifts)):
            answer.append(shifter(s[i], total - run_sum))
            run_sum += shifts[i]
        
        return "".join(answer)
      
      
