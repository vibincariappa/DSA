

class Solution:
    def MissingNumbers(self,nums):
#bruteforce
        # n = len(nums)

        # for i in range (0,n+1):
        #     if i not in nums:
        #         return i

#Optimal Solution - hashSet
        seen = set(nums)
        # n = len(nums)

        # for i in range(0,n+1):
        for i in range(0, len(nums)+1):
            if i not in seen:
                return i
sol = Solution()

print(sol.MissingNumbers([0,1,3]))