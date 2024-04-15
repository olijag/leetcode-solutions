# https://leetcode.com/problems/binary-tree-preorder-traversal/
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None: # Tree is empty
            return []

        tree_to_list = [root] 
        answer = []
        
        while tree_to_list:
            node = tree_to_list.pop()
            if node:
                answer.append(node.val)
                if node.right:
                    tree_to_list.append(node.right)
                if node.left:
                    tree_to_list.append(node.left)
        
        return answer



def main() -> None:
    test_case = []
    solution = Solution()
    print(solution.preorderTraversal(test_case))

 
if __name__ == '__main__':
    main()