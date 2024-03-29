# You are given a 0-indexed integer array tasks, where tasks[i] represents the difficulty level of a task. In each round, you can 
# complete either 2 or 3 tasks of the same difficulty level.

# Return the minimum rounds required to complete all the tasks, or -1 if it is not possible to complete all the tasks.

 

# Example 1:

# Input: tasks = [2,2,3,3,2,4,4,4,4,4]
# Output: 4
# Explanation: To complete all the tasks, a possible plan is:
# - In the first round, you complete 3 tasks of difficulty level 2. 
# - In the second round, you complete 2 tasks of difficulty level 3. 
# - In the third round, you complete 3 tasks of difficulty level 4. 
# - In the fourth round, you complete 2 tasks of difficulty level 4.  
# It can be shown that all the tasks cannot be completed in fewer than 4 rounds, so the answer is 4.
# Example 2:

# Input: tasks = [2,3,3]
# Output: -1
# Explanation: There is only 1 task of difficulty level 2, but in each round, you can only complete either 2 or 3 tasks of the same 
#   difficulty level. Hence, you cannot complete all the tasks, and the answer is -1.

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        countTasks = {}
        # get the frequency of each task
        for i in range(len(tasks)):
            if tasks[i] not in countTasks:
                countTasks[tasks[i]] = 1
            else:
                countTasks[tasks[i]] += 1
        
        # go by frequency and decide what the min number of rounds required for each task
        # we assume that the min number of tasks will have mist rounds with 3 tasks completed
        countRounds = 0
        for v in countTasks.values():
            if v == 1:
                return -1
            else:
                # get the bare mimumum with 3 tasks completed at a time
                multiple = v // 3 
                # if the frequency is divisible by 3, we can take all rounds with 3 tasks
                if v%3 == 0:
                    countRounds += multiple
                # if the frequency modulo 3 left with 1, we remove one round with 3 tasks, and add 2 rounds with 2 tasks
                elif v%3 == 1:
                    countRounds += ((multiple - 1) + 2)
                # if the modulo 3 is 2, we add the last round as 2 tasks completed
                elif v%3 == 2:
                    countRounds += (multiple + 1)
        
        return countRounds
      
