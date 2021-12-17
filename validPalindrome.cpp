// A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric 
// characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

// Given a string s, return true if it is a palindrome, or false otherwise.
  
// Example 1:

// Input: s = "A man, a plan, a canal: Panama"
// Output: true
// Explanation: "amanaplanacanalpanama" is a palindrome.
// Example 2:

// Input: s = "race a car"
// Output: false
// Explanation: "raceacar" is not a palindrome.
// Example 3:

// Input: s = " "
// Output: true
// Explanation: s is an empty string "" after removing non-alphanumeric characters.
// Since an empty string reads the same forward and backward, it is a palindrome.
  
class Solution {
public:
    bool isPalindrome(string s) {
        //idea: we will append all the letters and digits to a an empty string
        //then, the subtring if the first half of the string is compared with the 
        //second half reversed in letters
        string converted_str = "";
        
        //we will convert letters to lowercase
        //if the char is not a letter or a digit, we ignore it
        //the variable below will count the total number of letters found
        int letter_count = 0;
        for (auto itr: s) {
            if (isalpha(itr) || isdigit(itr)) {
                converted_str += tolower(itr);
            }
        }
        if (converted_str.length() == 0) {
            return true;
        }
        //first half of the converted string
        string first_half = converted_str.substr(0, converted_str.length()/2);
        
        //for the second half the converted string, we will go two characters at a time,
        //one taken from the start of the first half substring, and one from the back of the
        //converted string until the middle of the converted string
        int middle = converted_str.length()%2 == 0? converted_str.length()/2: converted_str.length()/2 + 1;
        for (unsigned int i = converted_str.length()-1, j = 0; i >= middle; i--, j++) {
            if (converted_str[i] != first_half[j]) {
                return false;
            }
        }   
        
        return true;
    }
};
