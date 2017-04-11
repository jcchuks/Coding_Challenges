class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        c = 32
        while c > 0:
            res = res << 1
            v = 1 if n & 1 else 0
            n  = n >> 1
            res |= v 
            c -= 1
        return res
