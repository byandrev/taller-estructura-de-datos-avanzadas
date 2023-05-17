#include <bits/stdc++.h>
#define fastIO ios::sync_with_stdio(0), cin.tie(0), cout.tie(0)
using namespace std;


vector<string> split(const string& str, char delimiter) {
    vector<string> tokens;
    size_t start = 0;
    size_t end = str.find(delimiter);

    while (end != string::npos) {
        tokens.push_back(str.substr(start, end - start));
        start = end + 1;
        end = str.find(delimiter, start);
    }

    tokens.push_back(str.substr(start));
    return tokens;
}


struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;

    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

TreeNode* deserialize(const std::string& str) {
    if (str == "{}") {
        return nullptr;
    }

    std::vector<TreeNode*> nodes;
    std::stringstream ss(str.substr(1, str.length() - 2));
    std::string token;
    
    while (std::getline(ss, token, ',')) {
        if (token == "null") {
            nodes.push_back(nullptr);
        } else {
            nodes.push_back(new TreeNode(std::stoi(token)));
        }
    }
    
    std::queue<TreeNode*> children;
    TreeNode* root = nodes[0];
    children.push(root);

    int i = 1;
    while (!children.empty() && i < nodes.size()) {
        TreeNode* node = children.front();
        children.pop();

        if (i < nodes.size()) {
            node->left = nodes[i];
            if (nodes[i]) {
                children.push(nodes[i]);
            }
            i++;
        }

        if (i < nodes.size()) {
            node->right = nodes[i];
            if (nodes[i]) {
                children.push(nodes[i]);
            }
            i++;
        }
    }

    return root;
}


int maxValue(TreeNode* node) {
    if (node == NULL) {
        return INT_MIN;
    }

    int value = node->val;
    int leftMax = maxValue(node->left);
    int rightMax = maxValue(node->right);

    return max(value, max(leftMax, rightMax));
}

int minValue(TreeNode* node) {
    if (node == NULL) {
        return INT_MAX;
    }

    int value = node->val;
    int leftMax = minValue(node->left);
    int rightMax = minValue(node->right);

    return min(value, min(leftMax, rightMax));
}

bool isValidBST(TreeNode* node) {
    map<long long, long long> mp;

    if (node == NULL) return true;

    if (mp.count(node->val) > 0) return false;
    else mp[node->val] = 1;

    if (node->left != NULL && maxValue(node->left) > node->val) return false;
    if (node->right != NULL && minValue(node->right) < node->val) return false;
    if (!isValidBST(node->left) || !isValidBST(node->right)) return false;

    return true;
}


int main() {
    fastIO;

    int t; cin >> t;

    while (t--) {
        string s; cin >> s;
        TreeNode* root = deserialize(s);
        cout << (isValidBST(root) ? "true" : "false") << endl;
    }

    return 0;
}