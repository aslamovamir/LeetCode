# You are playing the Bulls and Cows game with your friend.

# You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

# The number of "bulls", which are digits in the guess that are in the correct position.
# The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits 
# in the guess that could be rearranged such that they become bulls.
# Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

# The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

 

# Example 1:

# Input: secret = "1807", guess = "7810"
# Output: "1A3B"
# Explanation: Bulls are connected with a '|' and cows are underlined:
# "1807"
#   |
# "7810"
# Example 2:

# Input: secret = "1123", guess = "0111"
# Output: "1A1B"
# Explanation: Bulls are connected with a '|' and cows are underlined:
# "1123"        "1123"
#   |      or     |
# "0111"        "0111"
# Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        # helper function to count the number of bulls
        def count_bulls(secret, guess):
            bulls = 0
            zip_object = zip(secret, guess)
            for s, g in zip_object:
                print(s, g)
                if s == g:
                    bulls += 1
            
            return bulls
        
        # helper function to count the number of cows
        def count_cows(secret, guess):
            # let's store the digits of guess in a dictionary
            GueMap = {}
            # we will not consider the digits that are in the correct positions
            # for this will we loop through both of the lists in one run
            zip_object = zip(secret, guess)
            for s, g in zip_object:
                if s != g:
                    if g in GueMap:
                        GueMap[g] += 1
                    else:
                        GueMap[g] = 1
            
            # loop through the secret and see if all the digits, 
            # non-bulls, are in guess
            cows = 0
            zip_object2 = zip(secret, guess)
            for s, g in zip_object2:
                if s != g:
                    if s in GueMap:
                        # if this digit is not left in the map, we omit
                        if GueMap[s] == 0:
                            continue
                        GueMap[s] -= 1
                        cows += 1
            
            return cows
            
        
        return f"{count_bulls(secret, guess)}A{count_cows(secret, guess)}B"
       
       
       
