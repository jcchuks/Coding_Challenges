//https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/#/description
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        
        int counter = 0;
        int indx1 = 0;
        int length = numbers.size();
        int indx2 = length - 1;
        int sum ;
        vector<int> ans;
        while(counter < length && indx1 < indx2){
            sum = numbers[indx1] + numbers[indx2];
            if( sum == target){
                ans = {indx1 + 1, indx2 + 1};
                return ans;
            }else if(sum < target){
                indx1++;
            }else{
                --indx2;
            }
            
            counter++;
        }
        return ans;
        
    }
};
