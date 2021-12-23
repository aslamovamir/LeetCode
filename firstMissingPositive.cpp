// Given an unsorted integer array nums, return the smallest missing positive integer.

// You must implement an algorithm that runs in O(n) time and uses constant extra space.
  
// Example 1:

// Input: nums = [1,2,0]
// Output: 3
// Example 2:

// Input: nums = [3,4,-1,1]
// Output: 2
// Example 3:

// Input: nums = [7,8,9,11,12]
// Output: 1

class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        //a set to keep unique positive numbers
        set<int> Set;
        for (auto i: nums) {
            if (i > 0) {
                Set.insert(i);
            }
        }
        //a variable to indicate the numbers to follow in ascending order
        int indexing = 1;
        while(true) {
            //if the naturally following number is not in the set, return it
            if (Set.find(indexing) == Set.end()) {
                return indexing;
            }
            Set.erase(indexing);
            indexing++;
            //if the Set is empty,return the number greater than the max number in the set by one
            if (Set.size() == 0) {
                return indexing;
            }
        }
    }
};
