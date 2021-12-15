// Given a string s, return the longest palindromic substring in s.
// Example 1:

// Input: s = "babad"
// Output: "bab"
// Note: "aba" is also a valid answer.
// Example 2:

// Input: s = "cbbd"
// Output: "bb"
// Example 3:

// Input: s = "a"
// Output: "a"
// Example 4:

// Input: s = "ac"
// Output: "a"

class Solution {
public:
    string longestPalindrome(string s) {
        string answer = "";
        int max_length = 0;
        int left, right;
        for (unsigned int i = 0; i < s.length(); i++) {
            //odd length palindromes
            left = i;
            right = i;
            while (left >= 0 && right < s.length() && s[left] == s[right]) {
                if ((right - left + 1) > max_length) {
                    max_length = right - left + 1;
                    answer = s.substr(left, max_length);
                } 
                left--;
                right++;
            }
            //even length palindromes
            left = i;
            right = i+1;
            while (left >= 0 && right < s.length() && s[left] == s[right]) {
                if ((right - left + 1) > max_length) {
                    max_length = right - left + 1;
                    answer = s.substr(left, max_length);
                }
                left--;
                right++;
            }
        }
        
        return answer;
    }
};
