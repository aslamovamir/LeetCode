class Solution {
public:
    bool isPalindrome(int x) {
        string newX = to_string(x);
for(int i=0, j=1; i < newX.size(); i++, j++){
    if(newX[i] == newX[newX.size()-j]){
    }else{
        return false;
    }
}
return true;
    }
};
