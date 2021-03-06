// A string is good if there are no repeated characters.

// Given a string "s", return the number of good substrings of length three in "s".

// Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

// A substring is a contiguous sequence of characters in a string.
  
// Example 1:

// Input: s = "xyzzaz"
// Output: 1
// Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
// The only good substring of length 3 is "xyz".
// Example 2:

// Input: s = "aababcabc"
// Output: 4
// Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
// The good substrings are "abc", "bca", "cab", and "abc".

class Solution {
public:
    int countGoodSubstrings(string s) {
        set<char> RunSet;
        int answer = 0;
        bool found_dupl = false;
        for (int i=0; i<s.length(); i++) {
            if (i + 3 > s.length()) {
                break;
            }
            for (int j=i; j < i+3; j++) {
                if (RunSet.find(s[j]) == RunSet.end()) {
                    RunSet.insert(s[j]);
                } else {
                    found_dupl = true;
                    break;
                }
            }
            if (!found_dupl) {
                answer++;
            }
            found_dupl = false;
            RunSet.clear();
        }
        return answer;
    }
};
