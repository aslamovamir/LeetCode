#include <stdio.h>
#include <stdbool.h>
#include <math.h>


int reverse(int x){

    int digits[30];
    int digits_size = 0;
    int remainder = x;
    int digit;
    int digits_indeces = 0;
    bool is_positive = false;
    if (x>=0){is_positive = true;}
    for (;;){
        digit = remainder % 10;
        if (remainder/10 == 0){
            digit = remainder;
            digits[digits_indeces] = digit;
            ++digits_size;
            break;
        }
        remainder /= 10;
        digits[digits_indeces] = digit;
        ++digits_indeces; ++digits_size;
    }
    int first_digit = digits[0];
    
    if (is_positive){
    if (digits_size > 10) return 0;
    else if(digits_size == 10 && digits[0] > 2) return 0;
    else if (digits_size == 10 && digits[0] == 2 && digits[1] > 1) return 0;
    else if (digits_size == 10 && digits[0] == 2 && digits[1] == 1 && digits[2] > 4) return 0;
    else if (digits_size == 10 && digits[0] == 2 && digits[1] == 1 && digits[2] == 4 && digits[3] > 7) return 0;
    else if (digits_size == 10 && digits[0] == 2 && digits[1] == 1 && digits[2] == 4 && digits[3] == 7 && digits[4]>4) return 0;
    else if (digits_size == 10 && digits[0] == 2 && digits[1] == 1 && digits[2] == 4 && digits[3] == 7 && digits[4]==4 && digits[5]>8) return 0;
    else if (digits_size == 10 && digits[0] == 2 && digits[1] == 1 && digits[2] == 4 && digits[3] == 7 && digits[4]==4 && digits[5]==8 && digits[6]>3) return 0;
    else if (digits_size == 10 && digits[0] == 2 && digits[1] == 1 && digits[2] == 4 && digits[3] == 7 && digits[4]==4 && digits[5]==8 && digits[6]==3 && digits[7]>6) return 0;
    else if (digits_size == 10 && digits[0] == 2 && digits[1] == 1 && digits[2] == 4 && digits[3] == 7 && digits[4]==4 && digits[5]==8 && digits[6]==3 && digits[7]==6 && digits[8]>4) return 0;
    else if (digits_size == 10 && digits[0] == 2 && digits[1] == 1 && digits[2] == 4 && digits[3] == 7 && digits[4]==4 && digits[5]==8 && digits[6]==3 && digits[7]==6 && digits[8]==4
            && digits[9] > 7) return 0;
    }
    else{
        if (digits_size > 10) return 0;
    else if(digits_size == 10 && digits[0] < -2) return 0;
    else if (digits_size == 10 && digits[0] == -2 && digits[1] < -1) return 0;
    else if (digits_size == 10 && digits[0] == -2 && digits[1] == -1 && digits[2] < -4) return 0;
    else if (digits_size == 10 && digits[0] == -2 && digits[1] == -1 && digits[2] == -4 && digits[3] < -7) return 0;
    else if (digits_size == 10 && digits[0] == -2 && digits[1] == -1 && digits[2] == -4 && digits[3] == -7 && digits[4]<-4) return 0;
    else if (digits_size == 10 && digits[0] == -2 && digits[1] == -1 && digits[2] == -4 && digits[3] == -7 && digits[4]==-4 && digits[5]<-8) return 0;
    else if (digits_size == 10 && digits[0] == -2 && digits[1] == -1 && digits[2] == -4 && digits[3] == -7 && digits[4]==-4 && digits[5]==-8 && digits[6]<-3) return 0;
    else if (digits_size == 10 && digits[0] == -2 && digits[1] == -1 && digits[2] == -4 && digits[3] == -7 && digits[4]==-4 && digits[5]==-8 && digits[6]==-3 && digits[7]<-6) return 0;
    else if (digits_size == 10 && digits[0] == -2 && digits[1] == -1 && digits[2] == -4 && digits[3] == -7 && digits[4]==-4 && digits[5]==-8 && digits[6]==-3 && digits[7]==-6 && digits[8]<-4) return 0;
    else if (digits_size == 10 && digits[0] == -2 && digits[1] == -1 && digits[2] == -4 && digits[3] == -7 && digits[4]==-4 && digits[5]==-8 && digits[6]==-3 && digits[7]==-6 && digits[8]==-4
            && digits[9] < -8) return 0;
    }
    int num_reversed = 0; int index_10 = digits_size - 1;
    for (int i = 0; i < digits_size; i++){
        num_reversed += digits[i] * pow(10, index_10);
        --index_10;
    }


    
    return num_reversed;
}
