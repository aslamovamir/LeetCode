// Write an algorithm to determine if a number n is happy.

// A happy number is a number defined by the following process:

// Starting with any positive integer, replace the number by the sum of the squares of its digits.
// Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
// Those numbers for which this process ends in 1 are happy.
// Return true if n is a happy number, and false if not.

class Solution {
public:
    bool isHappy(int n) {
        if (n == 1) { return true; }
        long index = 0;
        int digit;
        int run_sum = 0;
        while (true) {
                while (true) {
                digit = n%10;
                run_sum += digit*digit;
                n/=10;
                if (n/10 == 0) {
                    run_sum += n*n;
                    break;
                }
            }
            if (run_sum == 1) {
                return true;
            } else {
                n = run_sum;
                run_sum = 0;
                index++;
                if (index == 10) {
                    return false;
                }
            }
        }
    }
};
