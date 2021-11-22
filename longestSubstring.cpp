class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<char> longest_ss;
        int size = 0;
        int index;
        bool in_stack = false;
        bool checked = false;
        for (int i = 0; i < s.length(); i++) {
            cout<<"CYCLE: "<<s[i]<<endl;
            if (!checked) {
                index = i;
                checked = true;
            }
            for (int j = 0; j < longest_ss.size(); j++) {
                if (longest_ss[j] == s[i]) {
                    in_stack = true;
                    checked = false;
                }
            }
            if (in_stack) {
                in_stack = false;
                if (longest_ss.size() > size) {
                    size = longest_ss.size();
                }
                longest_ss.clear();
            } else {
                longest_ss.push_back(s[i]);
                for (int k = 0; k < longest_ss.size(); k++) {
                    cout<<longest_ss[k]<<" ";
                }
            }
            if (!checked) {
                i = index;
            }
            if (i == s.length()-1) {
                if (size < longest_ss.size()) {
                    size = longest_ss.size();
                }
            }
        }
        return size;
    }
};
