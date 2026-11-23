class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l = 0;
        int r = 1;
        int best = 0;
        while(r < prices.size()){
            if (prices[r] > prices[l]){
                best = max(best, prices[r] - prices[l]);
            } else {
                l = r;
            }
            r++;
        }
        return best;
    }
};
