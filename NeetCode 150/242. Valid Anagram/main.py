# https://leetcode.com/problems/valid-anagram/submissions/1227665413/
# Notes after finished: 
# At first try of solving this, I've used for-loop which went through 
# each element in each list and comapred them. This took too much runtime.
# After that I've tried with list(), but had trouble with sorting it so it 
# would be easy to compare, at the end, I've read documentation for list() 
# and came up on sorted() which helped me solving this. 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_t = sorted(t)
        list_s = sorted(s)

        if list_t == list_s:
            return True
        else:
            return False



def main() -> None:
    solution = Solution()
    answer = solution.isAnagram(s="string", t="tsrgni")
    print(answer)
 
if __name__ == '__main__':
    main()