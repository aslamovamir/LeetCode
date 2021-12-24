// You are given an array of strings words (0-indexed).

// In one operation, pick two distinct indices i and j, where words[i] is a non-empty string, and move any character from words[i] to any position in words[j].

// Return true if you can make every string in words equal using any number of operations, and false otherwise.
// Example 1:

// Input: words = ["abc","aabc","bc"]
// Output: true
// Explanation: Move the first 'a' in words[1] to the front of words[2],
// to make words[1] = "abc" and words[2] = "abc".
// All the strings are now equal to "abc", so return true.
// Example 2:

// Input: words = ["ab","a"]
// Output: false
// Explanation: It is impossible to make all the strings equal using the operation.

class Solution {
public:
    bool makeEqual(vector<string>& words) {
        map<char,int> Map;
        for (unsigned int i=0; i<words.size(); i++) {
            for (unsigned int j=0; j<words[i].length(); j++) {
                Map[words[i][j]]++;
            }
        }
        for (map<char, int>::iterator iter = Map.begin(); iter != Map.end(); iter++) {
            if (iter->second%words.size() != 0) {
                return false;
            }
        }
        
        return true;
    }
};
