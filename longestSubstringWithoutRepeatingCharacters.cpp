// Given a string s, find the length of the longest substring without repeating characters.
// Example 1:

// Input: s = "abcabcbb"
// Output: 3
// Explanation: The answer is "abc", with the length of 3.
// Example 2:

// Input: s = "bbbbb"
// Output: 1
// Explanation: The answer is "b", with the length of 1.
// Example 3:

// Input: s = "pwwkew"
// Output: 3
// Explanation: The answer is "wke", with the length of 3.
// Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
// Example 4:

// Input: s = ""
// Output: 0

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        set<char> Set;
        int result=0;
        int iterator=0;
        if (s.length() == 0) {
            return 0;
        } else if (s.length() == 1) {
            return 1;
        }
        for (unsigned int i=0; i<s.length(); i++) {
            for (unsigned int j=i; j<s.length(); j++) {
                if (Set.find(s[j]) == Set.end()) {
                    iterator++;
                    Set.insert(s[j]);
                } else {
                    Set.clear();
                    result = max(result, iterator);
                    iterator = 0;
                    break;
                }
            }
        }
        return result;
    }
};
