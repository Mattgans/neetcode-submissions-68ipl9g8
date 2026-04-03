class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> diffs;
        int count = 0;
        for (auto i: nums){
            int diff = target - i;
            if(diffs.find(diff) != diffs.end()){
                return {diffs[diff], count};
            }
            diffs.insert({i,count});
            count++;
        }
        return {};
    }
};
