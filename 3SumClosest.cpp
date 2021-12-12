// Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

// Return the sum of the three integers.

// You may assume that each input would have exactly one solution.
// Example 1:

// Input: nums = [-1,2,1,-4], target = 1
// Output: 2
// Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
// Example 2:

// Input: nums = [0,0,0], target = 1
// Output: 0
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int run_diff, left, right, run_sum;
        int stop_diff = 999;
        int answer;
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i; j < nums.size(); j++) {
                left = j+1;
                right = nums.size()-1;
                while (left < right) {
                    run_sum = nums[i] + nums[left] + nums[right];
                    run_diff = abs(run_sum - target);
                    if (stop_diff > run_diff) {
                        stop_diff = run_diff;
                        answer = run_sum;
                    }
                    right--;
                }   
            }
        }
        
        return answer;
    }
};
