// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

// You may assume that each input would have exactly one solution, and you may not use the same element twice.

// You can return the answer in any order.

 

// Example 1:

// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]
// Output: Because nums[0] + nums[1] == 9, we return [0, 1].
// Example 2:

// Input: nums = [3,2,4], target = 6
// Output: [1,2]
// Example 3:

// Input: nums = [3,3], target = 6
// Output: [0,1]

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> solution;
        map <int, int> diffs;
        map <int, int> hash;
        int difference;
        if (target == 0) {
            for (int i = 0; i < nums.size(); i++) {
                if (nums[i] == 0) {
                   solution.push_back(i);
                   if (solution.size() == 2) {
                       return solution;
                   }
                } 
            }
        }
        for (int i = 0; i < nums.size(); i++) {
            hash[nums[i]] = i;
            difference = target - nums[i];
            diffs[nums[i]] = difference;
        }

        for (int i = 0; i < nums.size(); i++) {
            if (diffs[nums[i]] != 0) {
                if (hash[diffs[nums[i]]] != 0) {
                    if (i == hash[diffs[nums[i]]]) {
                        continue;
                    }
                    solution.push_back(i);
                    solution.push_back(hash[diffs[nums[i]]]);
                    break;
                }
            }   
        }
        
        return solution;
    }
};
