// Question: https://leetcode.com/problems/container-with-most-water/
// C/C++ compatible solution
// Runtime: O(n)

int maxArea(int* height, int heightSize) {
    if(!height && heightSize < 2){
        return 0;
    }
    int max = 0;
    int left = 0;
    int right = heightSize - 1;
    int val = 0;
    int curr = 0;
    int leftval = 0;
    int rightval = 0;
    while(left < right){
        leftval = *(height + left);
        rightval = *(height + right);
        val = leftval < rightval ? leftval : rightval;
       
        curr = (right - left) * val;
        max = curr > max ? curr : max;
        if(leftval < rightval){
            left++;
        }else{
             right--;
        } 
    }
    return max ;
    
}
