#https://leetcode.com/submissions/detail/104038255/
#Intuition:  for each doPal(), we place two pointers side by side and compare the substrings, then move the right pointer one step
#right and compare with the left pointer, then move the left pointer  one step one step left and compare with the right pointer. --repeat.
#Note flags.
class Solution {
private:
    int low,high,maxlen = 0;
public:
    string longestPalindrome(string s) {
        int len = s.length();
        if (len < 2){return s;}
        int roll = len -1;
        maxlen = 0;
        while(roll >= 0){ 
            doPal(s,roll,len-1);
            --roll;
        }
         
        return s.substr(low, high-low +1);
    }
   
    
    void doPal(string s, int i,   int indx){
        int l = i - 1 ;
        int r = i ;
        int sm = 0; int bg = 0; 
        bool flagA = false;bool flagB = false;
        while(l >= 0 && r <= indx  ){
              
              if ((s[l] == s[r] && flagA) || (r-l <= 1 && s[l] == s[r]) ){ 
                  sm = l;
                  bg = r;
                  flagA = true;
              } else{
                  flagA = false;
              }
              ++r;
              if((r<=indx && s[l] == s[r] && flagB) || (r-l <= 2 &&  s[l] == s[r]) ){ 
                  sm = l;
                  bg= r;
                  flagB = true;
                   
              } else{
                  flagB = false;
              }
             --l;  
             
             if ( !flagA && !flagB ){
                 break;
             }
        } 
        
        if (bg - sm  > maxlen){
            maxlen = bg - sm  ;
            low = sm; high = bg; 
        }
    }
        
    
};
