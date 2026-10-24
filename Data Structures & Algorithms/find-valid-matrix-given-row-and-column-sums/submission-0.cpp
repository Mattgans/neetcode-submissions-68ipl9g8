class Solution {
public:
    vector<vector<int>> restoreMatrix(vector<int>& rowSum, vector<int>& colSum) {
        // GREED BABY
        vector<vector<int>> m(rowSum.size(), vector<int>(colSum.size(), 0));
        m[0][0] = max(rowSum[0],colSum[0]);
        for (int i = 0; i < rowSum.size(); i++){
            int cur = 0;
            for (int j = 0; j < colSum.size(); j++){
                m[i][j] = min(rowSum[i]-cur,colSum[j]);
                cur += min(rowSum[i]-cur,colSum[j]);
                colSum[j] -= m[i][j];
            }
        }
        return m;
    }
};
