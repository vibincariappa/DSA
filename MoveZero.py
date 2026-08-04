#BruteForce

class Solution:
    def MoveZero(self,nums):
        temp = []

        for num in nums:
            if num != 0:
                temp.append(num)

        while len(temp) < len(nums):
            temp.append(0)

        for i in range(len(nums)):
            nums[i] = temp[i]

nums = [0,1,2,19,0,12]
sol = Solution()
sol.MoveZero(nums)
print(nums)