class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int, int> myMap;
        for (int i=0; i<arr.size();i++) {
            if (myMap.find(arr[i]) != myMap.end()) {
                myMap[arr[i]] += 1;
            }
            else {
                myMap[arr[i]] = 1;
            }
        }

        unordered_set<int> mySet;
        for (const auto& pair : myMap) {
            if (mySet.count(pair.second) > 0) {
                return false;
            }    
            mySet.insert(pair.second);
        }
        return true;
    }
};
