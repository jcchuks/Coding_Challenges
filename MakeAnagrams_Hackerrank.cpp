//https://www.hackerrank.com/challenges/ctci-making-anagrams 


#include <cmath>
#include <string>
#include <cstdio>
#include <vector>
#include <iostream>
#include <unordered_map>

using namespace std;

int number_needed(string a, string b) {
    int length_of_a = a.size();
    int length_of_b = b.size();
    int larger =  length_of_a >= length_of_b ? length_of_a : length_of_b; 
    int forward = 0;
    unordered_map<char,int> count_of_chars  ;
    while(forward < larger){ 
        if (forward < length_of_a ){
            if(count_of_chars.find(a[forward]) == count_of_chars.end()){
                count_of_chars[a[forward]] = 1;
            }else{
                count_of_chars[a[forward]] += 1;
            }
        }
        if (forward < length_of_b  ){
             if(count_of_chars.find(b[forward]) == count_of_chars.end()){
                count_of_chars[b[forward]] = -1;
            }else{
                count_of_chars[b[forward]] -= 1;
            }
        }
        ++forward;
    }
    int result = 0;
    for(unordered_map<char,int>::const_iterator itr 
            = count_of_chars.begin(), itr_end = count_of_chars.end();
             itr != itr_end; ++itr)
    {
        result += abs(itr->second);
    }
    
    return result;
   
}

int main(){
    string a;
    cin >> a;
    string b;
    cin >> b;
    cout << number_needed(a, b) << endl;
    return 0;
}
