class Solution {
    public int romanToInt(String s) {
        int total=0;
        int [] equiv = {1, 5, 10, 50, 100, 500, 1000};
        char [] c_equiv = {'I', 'V', 'X', 'L', 'C', 'D', 'M'};
        
                int [] input = new int [s.length()];
        for (int i = 0; i < s.length(); i++) {
            for (int j = 0; j < equiv.length; j++) {
                if (s.charAt(i) == c_equiv[j]) {
                    input[i] = equiv[j];
                }
            }
        }
        for (int y = 0; y < input.length; y++) {
            System.out.print(input[y] + " ");
            }
        for (int k = 0; k < input.length-1; k++) {
            if (input[k] >= input [k+1]) {
               total += input[k];
            }
            else {
               total -= input[k];
            }
        }
        total += input[input.length-1];
        return total;
    }
}
