class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char,int> seen;
        
        for (int i=0; i<magazine.size(); i++) {
            if (seen.count(magazine[i]) > 0) {
                seen[magazine[i]]++;
            }
            else {
                seen[magazine[i]] = 1;
            }
        }

        for (int i=0; i<ransomNote.size(); i++) {
            if (seen[ransomNote[i]] == 0) {
                return false;
            } 
            seen[ransomNote[i]]--;
        }
        return true;
    }
};
