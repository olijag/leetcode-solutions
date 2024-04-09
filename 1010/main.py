from typing import List

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]):
        for i in time:
            for j in time:
                if j != i:
                    if (time[i] + time[j]) % 60 == 0:
                        return (i, j)
                
def main() -> None:
    solution = Solution()
    time = [30, 20, 150, 100, 40]  # Example list of song durations
    result = solution.numPairsDivisibleBy60(time)
    print(result)
 
if __name__ == '__main__':
    main()