// Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

// Symbol       Value
// I             1
// V             5
// X             10
// L             50
// C             100
// D             500
// M             1000
// For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II.
//   The number 27 is written as XXVII, which is XX + V + II.

// Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, 
// the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to 
// the number nine, which is written as IX. There are six instances where subtraction is used:

// I can be placed before V (5) and X (10) to make 4 and 9. 
// X can be placed before L (50) and C (100) to make 40 and 90. 
// C can be placed before D (500) and M (1000) to make 400 and 900.
// Given an integer, convert it to a roman numeral.
// Example 1:

// Input: num = 3
// Output: "III"
// Example 2:

// Input: num = 4
// Output: "IV"

class Solution {
public:
    string intToRoman(int num) {
        string answer = "";
        stack<string> Stack;
        int index = 0;
        unsigned int running;
        
        map<int, string> Map = {{1, "I"}, {5, "V"}, {10, "X"}, {50, "L"}, {100, "C"}, {500, "D"}, {1000, "M"}};
        string run_str = "";
        
        while(num != 0) {
            running = num%10 * pow(10, index);
            num/=10;
            index++;
            if (running == 0) {
                continue;
            }
            if (running >= 1 && running < 5) {
                cout<<"BETWEEN 1 and 5"<<endl;
                if (running == 4) {
                    Stack.push("IV");
                } else {
                    Stack.push(Map[1]);
                    running -= 1;
                    while(running != 0) {
                        Stack.push(Map[1]);
                        running -= 1;
                    }
                }
            } else if (running >= 5 && running < 10) {
                if (running == 9) {
                    Stack.push("IX");
                } else {
                    run_str += Map[5];
                    running -= 5;
                    while (running != 0) {
                        run_str += Map[1];
                        running -= 1;
                    }
                    Stack.push(run_str);
                    run_str = "";
                }
            } else if (running >= 10 && running < 50) {
                if (running == 40) {
                    Stack.push("XL");
                } else {
                    run_str += Map[10];
                    running -= 10;
                    while (running != 0) {
                        run_str += Map[10];
                        running -= 10;
                    }
                    Stack.push(run_str);
                    run_str = "";
                }
            } else if (running >= 50 && running < 100) {
                if (running == 90) {
                    Stack.push("XC");
                } else {
                    run_str += Map[50];
                    running -= 50;
                    while (running != 0) {
                        run_str += Map[10];
                        running -= 10;
                    }
                    Stack.push(run_str);
                    run_str = "";
                }
            } else if (running >= 100 && running < 500) {
                if (running == 400) {
                    Stack.push("CD");
                } else {
                    run_str += Map[100];
                    running -= 100;
                    while (running != 0) {
                        run_str += Map[100];
                        running -= 100;
                    }
                    Stack.push(run_str);
                    run_str = "";
                }
            } else if (running >= 500 && running < 1000) {
                if (running == 900) {
                    Stack.push("CM");
                } else {
                    run_str += Map[500];
                    running -= 500;
                    while (running != 0) {
                        run_str += Map[100];
                        running -= 100;
                    }
                    Stack.push(run_str);
                    run_str = "";
                }
            } else {
                run_str += Map[1000];
                running -= 1000;
                while (running != 0) {
                    run_str += Map[1000];
                    running -= 1000;
                }
                Stack.push(run_str);
                run_str = "";
            }
        }
        while(!Stack.empty()) {
            // cout<<Stack.top();
            answer += Stack.top();
            Stack.pop();
        }
        return answer;
    }
};
