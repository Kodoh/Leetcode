class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map<char, char> mapping;
        set<char> seen;
        if (s.size() != t.size()) {
            return false;
        }

        for (int i=0; i<s.size();i++) {
            if (mapping.find(s[i]) != mapping.end()) {
                if (mapping[s[i]] != t[i]) {
                    return false;
                }
            }
            else{
                if (seen.count(t[i]) == 0) {
                    mapping[s[i]] = t[i];
                    seen.insert(t[i]);
                }
                else{
                    return false;
                }
            }
        }

        return true;
    }
};
