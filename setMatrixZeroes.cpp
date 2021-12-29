// Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

// You must do it in place.
  
// Example 1:
// Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
// Output: [[1,0,1],[0,0,0],[1,0,1]]

// Example 2:
// Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
// Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        //0 tracker
        vector<vector<int>> tracker;
        //the first element of the array is row number amd the second is the column number
        vector<int> row_col;
        for (int i = 0; i < matrix.size(); i++) {
            for (int j = 0; j < matrix[0].size(); j++) {
                if (matrix[i][j] == 0) {
                    //get the row
                    row_col.push_back(i);
                    //get the column
                    row_col.push_back(j);
                    //push the pair into a tracker
                    tracker.push_back(row_col);
                    //reset the pair
                    row_col.clear();
                }
            }
        }

        //set the corresponding rows and columns to 0
        for (int i = 0; i < tracker.size(); i++) {
            //get the rows
            for (int j = 0; j < matrix[tracker[i][0]].size(); j++) {
                matrix[tracker[i][0]][j] = 0;
            }
            //get the columns
            for (int j = 0 ; j < matrix.size(); j++) {
                matrix[j][tracker[i][1]] = 0;
            }
        }
      tracker.clear();
    }
};
