class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int current = 0;
        int maxGain = current;

        for (int i = 0; i<gain.size();i++) {
            current = current + gain[i];
            maxGain = max(maxGain,current);
        }

        return maxGain;
    }
};
