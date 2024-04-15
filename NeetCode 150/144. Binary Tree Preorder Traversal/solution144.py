# https://leetcode.com/problems/binary-tree-preorder-traversal/
# Time complexity O(n)
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None: # List is empty, return []
            return [] 

        root_to_list = [root]
        answer = []
        
        while root_to_list: # Iterate as long as there are objects in root_to_list
            node = root_to_list.pop() # Get the top of the stack 
            if node:
                answer.append(node.val) 
                if node.right:
                    root_to_list.append(node.right) # Append right first because left must be on top of the stack
                if node.left:
                    root_to_list.append(node.left) # Append left, ensures that left is on top of the stack
        
        return answer
    
def main() -> None:
    test_case = [1,2,3,4,5]
    solution = Solution()
    print(solution.preorderTraversal(test_case))

 
if __name__ == '__main__':
    main()