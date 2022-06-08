# You have a chat log of n messages. You are given two string arrays messages and senders where messages[i] is a message sent by senders[i].

# A message is list of words that are separated by a single space with no leading or trailing spaces. The word count of a sender is 
# the total number of words sent by the sender. Note that a sender may send more than one message.

# Return the sender with the largest word count. If there is more than one sender with the largest word count, return the one with 
# the lexicographically largest name.

# Note:

# Uppercase letters come before lowercase letters in lexicographical order.
# "Alice" and "alice" are distinct.
 

# Example 1:

# Input: messages = ["Hello userTwooo","Hi userThree","Wonderful day Alice","Nice day userThree"], senders = ["Alice","userTwo","userThree","Alice"]
# Output: "Alice"
# Explanation: Alice sends a total of 2 + 3 = 5 words.
# userTwo sends a total of 2 words.
# userThree sends a total of 3 words.
# Since Alice has the largest word count, we return "Alice".
# Example 2:

# Input: messages = ["How is leetcode for everyone","Leetcode is useful for practice"], senders = ["Bob","Charlie"]
# Output: "Charlie"
# Explanation: Bob sends a total of 5 words.
# Charlie sends a total of 5 words.
# Since there is a tie for the largest word count, we return the sender with the lexicographically larger name, Charlie.

class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        # let's keep a list of all senders with largest number of message words
        senders_largest = []
        # let's map the senders to the number of words in their messages in a dictionary
        map_senders = {}
        # this wil track the largest number of words
        largest = 0
        for i in range(len(senders)):
            if senders[i] not in map_senders:
                map_senders[senders[i]] = len(messages[i].split(" "))
                if map_senders[senders[i]] > largest:
                    largest = map_senders[senders[i]]
            else:
                map_senders[senders[i]] += len(messages[i].split(" "))
                if map_senders[senders[i]] > largest:
                    largest = map_senders[senders[i]]
        
        for key, value in map_senders.items():
            if value == largest:
                senders_largest.append(key)
        
        senders_largest.sort()
        
        return senders_largest[len(senders_largest)-1]
      
