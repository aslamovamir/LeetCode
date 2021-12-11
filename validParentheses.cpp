// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

// An input string is valid if:

// Open brackets must be closed by the same type of brackets.
// Open brackets must be closed in the correct order.

class Solution {
public:
    bool isValid(string s) {
        if (s.length() == 1) {
            return false;
        }
        stack<char> Stack;
        for (unsigned int i=0; i<s.length(); i++) {
            if (s[i] == '(' || s[i] == '{' || s[i] == '[') {
                Stack.push(s[i]);
            } else {
                if (s[i] == ')') {
                    if (Stack.empty()) {
                        return false;
                    }
                    if (Stack.top() == '(') {
                        Stack.pop();
                    } else {
                        return false;
                    }
                } else if (s[i] == '}') {
                    if (Stack.empty()) {
                        return false;
                    }
                    if (Stack.top() == '{') {
                        Stack.pop();
                    } else {
                        return false;
                    }
                } else if (s[i] == ']') {
                    if (Stack.empty()) {
                        return false;
                    }
                    if (Stack.top() == '[') {
                        Stack.pop();
                    } else {
                        return false;
                    }
                }
            }
        }
        if (!Stack.empty()) {
            return false;
        }
        return true;
    }
};
