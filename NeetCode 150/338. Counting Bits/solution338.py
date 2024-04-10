#https://leetcode.com/problems/counting-bits/?envType=list&envId=m9svb8n2
# Notes after finished: 
# This solution too slow.


from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:        
        def calcValue(arg: int) -> int:
            # Using built-in function bin() to find the integer in binary representation.   
            # It has to be stripped [2:] because the first two characters are 0b, which is not wanted.
            toBinary = bin(arg)[2:] 
            temp_list = [int(i) for i in toBinary]
            sum = 0 
            for j in temp_list:
                sum += j
            
            return sum
        ans = list()
        for i in range(n + 1):
            ans.append(calcValue(i))
        
        return ans

def main() -> None:
    solution = Solution()

    print(solution.countBits(n=5))
 
if __name__ == '__main__':
    main()