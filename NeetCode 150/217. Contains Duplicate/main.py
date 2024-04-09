# https://leetcode.com/problems/contains-duplicate/description/

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new_set = set()
        for i in nums:
            if i in new_set:
                return True
            else:
                new_set.add(i)
        return False
                


def main() -> None:
    test_case = [1,2,3,4,5,1]
    
    answer = Solution().containsDuplicate(nums=test_case)
    print(answer)

if __name__ == '__main__':
    main()