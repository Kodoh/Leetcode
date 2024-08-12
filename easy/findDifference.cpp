class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        vector<vector<int>> res = {{},{}};
        
        unordered_set<int> s1(nums1.begin(), nums1.end());
        unordered_set<int> s2(nums2.begin(), nums2.end());
        
        for (const auto& elem : s1) {
            if (s2.count(elem) > 0) {
                s2.erase(elem);
            }
            else {
                res[0].push_back(elem);
            }
        }

        for (const auto& elem : s2) {
            res[1].push_back(elem);
        }

        return res;
    }
};
