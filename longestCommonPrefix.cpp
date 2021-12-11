// Write a function to find the longest common prefix string amongst an array of strings.

// If there is no common prefix, return an empty string "".
// Example 1:

// Input: strs = ["flower","flow","flight"]
// Output: "fl"
// Example 2:

// Input: strs = ["dog","racecar","car"]
// Output: ""
// Explanation: There is no common prefix among the input strings.

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string answer = "";
        char running;
        int index = 0;
        bool found_diff = false;
        bool atstart = true;
        while(!found_diff) {
            for (unsigned int i = 0; i < strs.size(); i++) {
                if (index >= strs[i].length()) {
                    found_diff = true;
                    break;
                }
                if (atstart) {
                    atstart = false;
                    running = strs[i][index];
                    continue;
                }
                if (running != strs[i][index]) {
                    found_diff = true;
                    break;
                }
            }
            if (!found_diff) {
                answer += running;
                atstart = true;
                index++;
            }
        }
        return answer;
    }
};
