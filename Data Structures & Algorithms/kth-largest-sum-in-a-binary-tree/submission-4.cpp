/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
#include <algorithm>
class Solution {
public:
    void best(TreeNode* root, int k, vector<long long>& levelsums){
        if (!root) return;
        if (k >= levelsums.size()){
            levelsums.push_back(0);
        }
        levelsums[k] += root->val;
        best(root->left, k+1, levelsums);
        best(root->right, k+1, levelsums);
    }
    long long kthLargestLevelSum(TreeNode* root, int k) {
        vector<long long> sums = {};
        best(root, 0, sums);
        std::sort(sums.begin(), sums.end(), std::greater<long long>());
        if (k > sums.size()){
            return -1;
        }
        return sums[k-1];
    }

};
