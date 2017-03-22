/*
* https://www.testdome.com/questions/cpp/path/8511?testId=34&testDifficulty=Hard
* Code implementing change directory function e.g cd ./.././../x  
* when current directory is /a/b/c/d  
* gives /a/b/x
*/


#include <iostream>
#include <string>
#include <stdexcept>

class Path
{
public:
    Path(std::string path)
    {
        currentPath = path;
    }

    std::string getPath() const
    {
        return currentPath;
    }

    Path cd(std::string newStr) const
    { 
        std::string newPath = newStr;
         std::string curr_dir;
         int pos = -1;
         while( !newPath.empty()){
             pos = newPath.find(separator);
             if(pos>-1){
                 curr_dir = newPath.substr(0,pos);
                 newPath.erase(0,pos+separator.length());
                 if (curr_dir == ".."){
                     back();
                 }else if(curr_dir == "."){
                     continue;
                 }else{
                     append(curr_dir);
                 }
                     
             }else{
                  
                 if(!newPath.empty()){
                     if (newPath == ".."){
                         back();
                     }else{
                         append(newPath); 
                     }
                 }else{
                     break;
                 }
                 newPath.erase(0);
             }
         }
        
        return *this;
    }
    
    

private:
    mutable std::string currentPath;
    std::string separator = "/";
    
    void back() const{
       std::size_t posi = 0;
       if (!currentPath.empty()){ 
           posi = currentPath.find_last_of(separator);
           if (posi == currentPath.length()){
               currentPath.erase(posi);
               posi = currentPath.find_last_of(separator);
           }
           currentPath.erase(posi);
       }
        
    }
    
    void append(std::string path) const{ 
       currentPath.append("/").append(path);
    }
};

#ifndef RunTests
int main()
{
    Path path("/a/b/c/d");
    std::cout << path.cd("../..").getPath();
}
#endif
