class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int,int> hashmap;
        int res;
        int occur = 0;
        for(int i = 0;i<nums.size();i++) {
            if (hashmap.count(nums[i]) == 0) {
                hashmap[nums[i]] = 1;
            }
            else {
                hashmap[nums[i]]++;
            }

            if (hashmap[nums[i]] > occur) {
                occur = hashmap[nums[i]];
                res = nums[i];
            }
        }

        return res;
    }
};
