class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        count = -1
        temp = n
        while n!=0:
            n = int(n/2)
            count+=1
        if (2**count)==temp:
            return True
        else:
            return False
s = Solution()
print(s.isPowerOfTwo(131071))