class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        double currentSum = accumulate(nums.begin(), nums.begin() + k, 0.0);
        double maxAverage = currentSum / k;

        for (int i = k; i < nums.size(); i++) {
            currentSum += nums[i] - nums[i - k];
            maxAverage = max(maxAverage, currentSum / k);
        }

        return maxAverage;
    }
};
