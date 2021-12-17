// Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

// A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


// Example 1:

// Input: digits = "23"
// Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
// Example 2:

// Input: digits = ""
// Output: []
// Example 3:

// Input: digits = "2"
// Output: ["a","b","c"]

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> answer;
        if (digits.length() == 0) {
            return answer;
        }
        map<char, string> Map = {
                {'2', "abc"}, 
                {'3', "def"},
                {'4', "ghi"},
                {'5', "jkl"}, 
                {'6', "mno"}, 
                {'7', "pqrs"}, 
                {'8', "tuv"}, 
                {'9', "wxyz"}
        };
        
        if (digits.length() != 0) {
            backTrack(0, "", Map, digits, answer);
        }
        
        return answer;
    }
    
    void backTrack(int indexing, string curr_str, map<char, string> &Map, string &digits, vector<string> &answer) {
            if (curr_str.length() == digits.length()) {
                answer.push_back(curr_str);
                return;
            }
            for (unsigned int i = 0; i < Map[digits[indexing]].length(); i++) {
                backTrack(indexing + 1, curr_str + Map[digits[indexing]][i], Map, digits, answer);
            }
        }
};
