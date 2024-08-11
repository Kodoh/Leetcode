class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int current = 0;
        int right = accumulate(nums.begin(), nums.end(), 0.0);
        for (int i = 0; i<nums.size();i++) {
            right -= nums[i];
            if (current == right) {
                return i;
            }
            current += nums[i];
        }
        return -1;
    }
};
