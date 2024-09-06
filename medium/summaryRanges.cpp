class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> res; 
        
        if (nums.empty()) 
            return res;

        int left = 0; 

        for (int right = 1; right <= nums.size(); ++right) {
            if (right == nums.size() || nums[right] != nums[right - 1] + 1) {
                if (right - left == 1) {
                    res.push_back(to_string(nums[left]));
                } else { 
                    res.push_back(to_string(nums[left]) + "->" + to_string(nums[right - 1]));
                }
                left = right; 
            }
        }

        return res;
    }
};
