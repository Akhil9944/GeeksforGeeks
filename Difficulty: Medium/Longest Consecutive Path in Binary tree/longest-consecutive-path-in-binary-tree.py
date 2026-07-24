'''
# Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def longestConsecutive(self, root):
        if not root:
            return -1
        
        self.max_len = 0
        
        def dfs(node, expected_val, curr_len):
            if not node:
                return
            
            # Check if this node continues the consecutive sequence
            if node.data == expected_val:
                curr_len += 1
            else:
                curr_len = 1
                
            # Update the global maximum length
            self.max_len = max(self.max_len, curr_len)
            
            # Recur for left and right subtrees
            dfs(node.left, node.data + 1, curr_len)
            dfs(node.right, node.data + 1, curr_len)
            
        # Start DFS with initial values
        dfs(root, root.data, 0)
        
        # If no sequence of length >= 2 exists, return -1
        return self.max_len if self.max_len > 1 else -1