// Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

// Notice that the solution set must not contain duplicate triplets.
// Example 1:

// Input: nums = [-1,0,1,2,-1,-4]
// Output: [[-1,-1,2],[-1,0,1]]
// Example 2:

// Input: nums = []
// Output: []
// Example 3:

// Input: nums = [0]
// Output: []

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> answer;
        vector<int> runarr;
        int left, right, run;
        sort(nums.begin(), nums.end());
        for (unsigned int i = 0; i < nums.size(); i++) {
            if (i > 0 && nums[i] == nums[i-1]) {
                continue;
            }
            left = i + 1;
            right = nums.size()-1;
            while (left < right) {
                run = nums[i] + nums[left] + nums[right];
                if (run > 0) {
                    right--;
                } else if (run < 0) {
                    left++;
                } else {
                    runarr.push_back(nums[i]);
                    runarr.push_back(nums[left]);
                    runarr.push_back(nums[right]);
                    answer.push_back(runarr);
                    runarr.clear();
                    left++;
                    while (nums[left] == nums[left-1] && left < right) {
                        left++;
                    }
                }
            }
        }
        return answer;
    }
};
