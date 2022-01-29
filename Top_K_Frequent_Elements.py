# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # let's first collect the frequencies of each number in a map
        NumFreq = {}
        for num in nums:
            if num not in NumFreq:
                NumFreq[num] = 1
            else:
                NumFreq[num] += 1
        
        # now, we will frequencies to the numbers: for each frequency, we will have a list
        # of numbers that have this frequency in nums
        FreqNum = {}
        # we will create a helper list to collect unique frequency values in a seperate list
        # when we sort this list, we know which numbers have most frequencies
        frequencies = []
        for key, value in NumFreq.items():
            if value not in FreqNum:
                FreqNum[value] = []
                FreqNum[value].append(key)
            else:
                FreqNum[value].append(key)
            # get only unique frequencies
            if value not in frequencies:
                frequencies.append(value)
        
        # sort the frequencies list in reverse, so greatest frequencies are at the front
        frequencies.sort(reverse = True)
        
        answer = []
        # this boolean will help in filling the answer with k most frequent numbers
        got_k_most = False
        for j in range(len(frequencies)):
            for i in range(len(FreqNum[frequencies[j]])):
                print(FreqNum[frequencies[j]])
                if len(answer) == k:
                    # we know we got k numbers
                    got_k_most = True
                    break
                answer.append(FreqNum[frequencies[j]][i])
            if got_k_most:
                break
    
        return answer
    
    
