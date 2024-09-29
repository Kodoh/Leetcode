class Solution {
public:
    bool wordPattern(string pattern, string s) {
        unordered_map<char, string> charToWord;
        unordered_map<string, char> wordToChar;

        vector<string> split_s;
        stringstream ss(s);
        string word;
                
        while (ss >> word) {
            split_s.push_back(word);
        }

        if (split_s.size() != pattern.length()) {
            return false;
        }

        for (int i = 0; i < pattern.size(); i++) {
            char p = pattern[i];
            string w = split_s[i];

            if (charToWord.count(p) > 0) {
                if (charToWord[p] != w) {
                    return false;
                }
            } else {
                charToWord[p] = w;
            }

            if (wordToChar.count(w) > 0) {
                if (wordToChar[w] != p) {
                    return false;
                }
            } else {
                wordToChar[w] = p;
            }
        }

        return true;
    }
};
