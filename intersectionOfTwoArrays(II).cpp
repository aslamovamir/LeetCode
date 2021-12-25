// Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear 
// as many times as it shows in both arrays and you may return the result in any order.

// Example 1:
// Input: nums1 = [1,2,2,1], nums2 = [2,2]
// Output: [2,2]

// Example 2:
// Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
// Output: [4,9]
// Explanation: [9,4] is also accepted.

class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        //frequency maps for the two vectors
        map<int, int> Map1, Map2;
        vector<int> answer;
        //collect the frequncy of numbers from the 2 vectors
        for (auto i: nums1) {
            Map1[i]++;
        }
        for (auto i: nums2) {
            Map2[i]++;
        }
        int common_frequency;
        //go through the numbers of any one vector and see how the frequencies are 
        //related in the 2 Maps
        for (auto i: nums1) {
            if (Map1[i] != 0 && Map2[i] != 0) {
                common_frequency = Map1[i] > Map2[i]? Map2[i]: Map1[i];
                for (int j = 0; j < common_frequency; j++) {
                    answer.push_back(i);
                }
                //reset the frequencies in both Maps
                Map1[i] = 0;
                Map2[i] = 0;
            }
        }
        return answer;
    }
};
