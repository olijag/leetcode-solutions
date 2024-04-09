# https://leetcode.com/problems/two-sum/?envType=list&envId=m9svb8n2

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_dict = {}

        for i, num in enumerate(nums):
            new_target = target - num 
            if new_target in new_dict:
                return [i, new_dict[new_target]]
               
            new_dict[num] = i    

            
def main() -> None:
    solution = Solution()
    
    answer = solution.twoSum(nums = [3,3], target = 6)

    print(answer)
 
if __name__ == '__main__':
    main()