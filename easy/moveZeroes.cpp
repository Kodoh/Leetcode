class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int zeroPointer = 0;

        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != 0) {
                if (i != zeroPointer) {
                    nums[zeroPointer] = nums[i];
                    nums[i] = 0;
                }
                zeroPointer++;
            }
        }
    }
};
