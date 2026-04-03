#include <unordered_set>
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> ns;
        for (int n: nums){
            if (ns.find(n) != ns.end()) {
                return true;
            } else {
                ns.insert(n);
            }
        }
        return false;
    }
};
