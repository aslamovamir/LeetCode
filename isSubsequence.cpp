// Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

// A subsequence of a string is a new string that is formed from the original string by deleting 
// some (can be none) of the characters without disturbing the relative positions of the remaining 
// characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
  
// Example 1:

// Input: s = "abc", t = "ahbgdc"
// Output: true
// Example 2:

// Input: s = "axc", t = "ahbgdc"
// Output: false

class Solution {
public:
    bool isSubsequence(string s, string t) {
        //indexing below will indecate at what char of s we are looking for in t
        int indexing = 0;
        for (unsigned int i = 0; i < t.length(); i++) {
            if (s[indexing] == t[i]) {
                indexing++;
            }
        }  
        //if after the loop above the indexing is not equal to the length of s
        //it means we have not found all the chars of s in t
        if (indexing != s.length()) {
            return false;
        } else {
            return true; 
        }
    }
};
