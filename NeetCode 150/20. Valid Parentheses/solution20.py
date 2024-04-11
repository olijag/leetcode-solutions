# https://leetcode.com/problems/valid-parentheses/description/?envType=list&envId=m9svb8n2

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        control_stack = []
        matching_brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for bracket in s:
            if bracket in matching_brackets.values():
                control_stack.append(bracket)
            elif bracket in matching_brackets.keys():
                if not control_stack or control_stack.pop() != matching_brackets[bracket]:
                    return False

        return len(control_stack) == 0



test_case = '([{])}'  

def main():
    solution = Solution()
    return (solution.isValid())

if __name__ == "__main__":
    print(main(test_case))


# First attempt. Solution to check only the next bracket 
""" class Solution:
    def isValid(self, s: str) -> bool:
        # Create a dict of valid key-value pairs. 
        valid_bracket = { 
            '(': ')',
            '{': '}',
            '[': ']',
        }
        
        # Iterate through the string and check is next bracket is valid.
        for i in range(len(s)):
            if s[i+1] != valid_bracket[s[i]]:
                return False
        return True """