// Given an integer array nums and an integer k, return true if there are two distinct indices i and j 
// in the array such that nums[i] == nums[j] and abs(i - j) <= k.

// Example 1:

// Input: nums = [1,2,3,1], k = 3
// Output: true
// Example 2:

// Input: nums = [1,0,1,1], k = 1
// Output: true
// Example 3:

// Input: nums = [1,2,3,1,2,3], k = 2
// Output: false


class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        if (k == 0) {
            return false;
        }
        set<int> Set;
        if (k >= nums.size()) {
            for (auto itr: nums) {
                if (Set.find(itr) == Set.end()) {
                    Set.insert(itr);
                } else {
                    return true;
                }
            }
            return false;
        } else {
             for (unsigned int i = 0; i < nums.size(); i++) {
                if (i + k > nums.size()) {
                    //cout<<"CANNOT FURTHER!"<<endl;
                    break;
                }
                for (unsigned int j = i; j <= i + k; j++) {
                    //cout<<"Cycle: "<<nums[j]<<"     ";
                    if (Set.find(nums[j]) != Set.end()) {
                        return true;
                    } else {
                        Set.insert(nums[j]);
                    }
                }
                Set.clear();
                //cout<<"\n";
            }
            return false;   
        }
    }
};
