class Solution {
public:
    int trap(vector<int>& height) {
        int l = 0;
        int r = height.size() - 1;
        int m_l = 0;
        int m_r = 0;
        int ret = 0;
        while(l < r){
            if (height[l] < height[r]){
                m_l = max(m_l,height[l]);
                ret += m_l - height[l];
                l++;
            } else{
                m_r = max(m_r,height[r]);
                ret += m_r - height[r];
                r--;
            }
        }
        return ret;
    }
};
