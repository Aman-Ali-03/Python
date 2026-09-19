class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        while(k!=0):
            mini = min(nums)
            nums[nums.index(mini)] = mini*multiplier
            k-=1
        return nums

s1 = Solution()
print(s1.getFinalState([2,1,3,5,6],5,2))