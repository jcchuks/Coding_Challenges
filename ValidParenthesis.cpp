//https://leetcode.com/problems/valid-parentheses/#/description

#define SEE(array,item) std::find(array.begin(),array.end(),item) != array.end()

class Solution {
public:
    bool isValid(string s) {
        vector<char> stack;
        vector<char> closers = {')','}',']'};
        
        int size = s.size();
        unordered_map<char,char> xters;
        xters['('] = ')';
        xters['{'] = '}';
        xters['['] = ']';
        char curr;
        unordered_map<char,char>::iterator itr;
        for(char& it : s){
            curr = it;
            itr = xters.find(curr);
            if( itr != xters.end()){
                stack.push_back(curr);
            }else if (SEE(closers,curr)){
                if (!stack.empty()){
                char val = stack.back();
                stack.pop_back();
                if (xters[val] != curr){
                    return false;
                }
                }else{
                    return false;
                }
                
            }
        }
        if (stack.empty()){return true;}
        
        return false;
        
        
    }
};
