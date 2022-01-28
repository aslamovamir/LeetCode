# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

 

# Example 1:

# Input: n = 2, trust = [[1,2]]
# Output: 2
# Example 2:

# Input: n = 3, trust = [[1,3],[2,3]]
# Output: 3
# Example 3:

# Input: n = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1
 

# Constraints:

# 1 <= n <= 1000
# 0 <= trust.length <= 104
# trust[i].length == 2
# All the pairs of trust are unique.
# ai != bi
# 1 <= ai, bi <= n

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # initial checks
        
        # if n is 1, we know we have only one person, who trusts nobody and except himself,
        # by logical default, everybody trusts that person - that person is a judge
        if n == 1:
            return 1
        # but if the nobody trusts nobody, we know we don't have any judge
        elif len(trust) == 0:
            return -1
        
        # let's store each person as the key and who they trust as a list in a dictionary
        TrustMap = {}
        trusted = []
        
        # collect the trusted people of each person
        for pair in trust:
            if pair[0] not in TrustMap:
                TrustMap[pair[0]] = []
                TrustMap[pair[0]].append(pair[1])
            else:
                TrustMap[pair[0]].append(pair[1])
        
        # identify the person who trusts nobody, by default, leave it at -1
        trust_nobody = -1
        for i in range(1, n+1):
            if i not in TrustMap:
                trust_nobody = i
        # now check if that person, who trusts nobody, is trusted by every other person        
        for person, trusted in TrustMap.items():
            if trust_nobody not in trusted:
                # if any person does not trust that person, the group does not have any judge
                return -1
        
        # return identified judge
        return trust_nobody
      
      
