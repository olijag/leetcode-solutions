# https://leetcode.com/problems/binary-tree-postorder-traversal/
# This question is very similar to 144 Binary tree preorder traversal

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: # Tree is empty
            return []
        
        stack = [root] # Create a stack
        visit = [False] # Create a stack for visited nodes
        result = []

        while stack: # As long as there are nodes in the stack
            node, visited = stack.pop(), visit.pop() 
            if node:
                if visited:
                    result.append(node.val)
                else: 
                    stack.append(node)
                    visit.append(True) # Node has been visited, add True
                    stack.append(node.right)
                    visit.append(False) # Right and left node has not yet been visited, add False for right and left node
                    stack.append(node.left)
                    visit.append(False)
        return result 
            
                
def main() -> None:
    test_case = []
    solution = Solution()
    print(solution.postorderTraversal(test_case))
 
if __name__ == '__main__':
    main()    