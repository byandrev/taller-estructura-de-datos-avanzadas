class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> p;
        if(root == nullptr) return p;
        vector<int> left = inorderTraversal(root->left);
        p.insert(p.end(), left.begin(), left.end());
        p.push_back(root->val);
        vector<int> right = inorderTraversal(root->right);
        p.insert(p.end(), right.begin(), right.end());
        return p;
    }
};
