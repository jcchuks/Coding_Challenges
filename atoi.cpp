#define toDigit(c)(c-'0')
class Solution {
public:
    int myAtoi(string str) {
        int size = str.size();
        int counter = 0;
        long numbers = 0;
        int sign = 1;
        
        if (isspace(str[counter]) ){
            while (counter < size && isspace(str[counter])){
                counter  += 1;
            }
        }
        
        if(str[counter] == '-'){ 
            sign = -1;
            counter += 1;
        }else if (str[counter] == '+'){
            counter += 1;
        }
        else if (!isdigit(str[counter])){
            return 0;
        }
        while (counter < size ){
            char a = str[counter];
           
            if (isdigit(a)){
                numbers = 10 * numbers; 
                numbers += toDigit(a);   
            } else{
                return numbers * sign;
            }
            counter += 1; 
       
            if ( numbers > 2147483647 && sign > 0){
                return 2147483647;
            }else if (numbers*sign <= -2147483648 && sign < 0 ){
                return -2147483648;
            }
        }
 
        return numbers * sign;  
    }
};
