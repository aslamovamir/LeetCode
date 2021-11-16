class Solution {
public:
    int lengthOfLastWord(string s) {
        int length = 0;
        int spaces = 0;
        
        for (int i = s.length()-1; i >= 0; i--) {
            if (s[i] == ' ') {
                spaces++;
            } else {
                break;
            }
        }
        
        for (int i = s.length()-1-spaces; i >= 0; i--) {
            if (s[i] == ' ') {
                break;
            } else {
                length++;
            }
        }
        
        
        return length;
    }
};
