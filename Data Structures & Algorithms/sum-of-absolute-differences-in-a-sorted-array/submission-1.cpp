class Solution {
public:
    vector<int> getSumAbsoluteDifferences(vector<int>& nums) {
        vector<int> m = {};
        for (int i = 0; i < nums.size(); i++){
            int total = 0;
            for(int j = 0; j < nums.size(); j++){
                total += abs(nums[i]-nums[j]);
            }
            m.push_back(total);
        }
        return m;
    }
};
