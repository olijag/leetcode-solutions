# https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        new_list = ['0'] * 32  # Initialize a list of '0's of length 32
        for i in range(32):
            new_list[31 - i] = str(n & 1)  # Get the least significant bit and place it in the reversed position
            n >>= 1  # Shift n right by 1 to process the next bit

        # Join the list and convert it to an integer
        reversed_num = int(''.join(new_list), 2)
        return reversed_num