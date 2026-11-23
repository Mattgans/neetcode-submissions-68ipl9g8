class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int best = 0;
        int minl = prices[0];
        for (auto price: prices){
            best = max(best,price-minl);
            minl = min(price,minl);
        }
        return best;
    }
};
