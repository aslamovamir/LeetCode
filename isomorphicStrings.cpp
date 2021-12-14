// Given two strings s and t, determine if they are isomorphic.

// Two strings s and t are isomorphic if the characters in s can be replaced to get t.

// All occurrences of a character must be replaced with another character while preserving the order of characters.
// No two characters may map to the same character, but a character may map to itself.
// Example 1:

// Input: s = "egg", t = "add"
// Output: true
// Example 2:

// Input: s = "foo", t = "bar"
// Output: false
// Example 3:

// Input: s = "paper", t = "title"
// Output: true

#include <map>
#include <vector>

class Solution {
public:
    bool isIsomorphic(string s, string t) {

        map<char, vector<int>> Hash1;
        map<char, vector<int>> Hash2;
        map<char, char> Check1;
        map<char, char> Check2;
        
        for (unsigned int i = 0; i < s.length(); i++) {
            if (Hash1[s[i]].size() == 1) {
                Check1[s[i]] = t[i];
            }
            Hash1[s[i]].push_back(i);
        }

        for (unsigned int i = 0; i < t.length(); i++) {
            if (Hash2[t[i]].size() == 1) {
                Check2[t[i]] = s[i];
            }
            Hash2[t[i]].push_back(i);
        }
        
        if (Check1.size() != Check2.size()) {
            return false;
        }
        
        for (auto it = Check1.begin(); it != Check1.end(); it++) {
            if (Hash1[it->first].size() != Hash2[it->second].size()) {
                return false;
            } else {
                for (unsigned int i = 0; i < Hash1[it->first].size(); i++) {
                    if (Hash1[it->first][i] != Hash2[it->second][i]) {
                        return false;
                    }
                }
            }
        }
        
        return true;
    }
};
