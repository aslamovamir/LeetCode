# A password is said to be strong if it satisfies all the following criteria:

# It has at least 8 characters.
# It contains at least one lowercase letter.
# It contains at least one uppercase letter.
# It contains at least one digit.
# It contains at least one special character. The special characters are the characters in the following string: "!@#$%^&*()-+".
# It does not contain 2 of the same character in adjacent positions (i.e., "aab" violates this condition, but "aba" does not).
# Given a string password, return true if it is a strong password. Otherwise, return false.

 

# Example 1:

# Input: password = "IloveLe3tcode!"
# Output: true
# Explanation: The password meets all the requirements. Therefore, we return true.
# Example 2:

# Input: password = "Me+You--IsMyDream"
# Output: false
# Explanation: The password does not contain a digit and also contains 2 of the same character in adjacent positions. Therefore, we return false.
# Example 3:

# Input: password = "1aB!"
# Output: false
# Explanation: The password does not meet the length requirement. Therefore, we return false.

class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        # special characters defines
        special_chrs = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '"']
        # some booleans to test validity
        lower_case = False
        upper_case = False
        one_digit = False
        special_chr = False
        
        for i in range(len(password)):
            if i != len(password) - 1:
                if password[i] == password[i+1]:
                    return False
            if password[i].islower():
                lower_case = True
            elif password[i].isupper():
                upper_case = True
            elif password[i].isdigit():
                one_digit = True
            elif password[i] in special_chrs:
                special_chr = True
        
        
        return (lower_case and upper_case and one_digit and special_chr)
      
      
