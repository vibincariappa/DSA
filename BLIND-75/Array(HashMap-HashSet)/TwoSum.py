#BruteForce psuedo-code


# for i from 0 to n
#     for j form i+1 to n
#         if nums[i] == nums[j]
#             if nums[i] == nums[j]
#             return True




#Bruteforce application

#         n = len(nums)

#         for i in range(n):
#             for j in range(i+1,n):
#                 if nums[i] + nums[j] == target:
#                     return [i,j]

#         return []

#TwoSum - Using HashMap
class Solution:
    def TwoSum(self,nums, target):
        # seen = {}
        # for i, num in enumerate(nums):
        #     complement = target -num
        #     if complement in seen:
        #         return[seen[complement],i]
        #     seen[num] = i
        # return
    
nums = list(map(int,input("Enter you Nums: ").split()))
target = int(input("Target:"))
sol = Solution()
print(sol.TwoSum(nums,target))
