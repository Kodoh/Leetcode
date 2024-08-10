class Solution {
public:
    string reverseVowels(string s) {
        int left = 0;
        int right = s.length() - 1;
        set<char> vowels = {'a', 'e', 'i', 'o', 'u'};

        while (left < right) {
            if (vowels.count(tolower(s[left])) && (vowels.count(tolower(s[right])))) {
                swap(s[left], s[right]);
                left++;
                right--;
            }
            else if (vowels.contains(tolower(s[left]))) {
                right--;
            }

            else if (vowels.contains(tolower(s[right]))) {
                left++;
            }
            else {
                left++;
                right--;   
            }
        }
        return s;
    }
};
