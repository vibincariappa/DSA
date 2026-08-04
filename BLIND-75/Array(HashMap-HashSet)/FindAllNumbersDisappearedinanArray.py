

class Solution:
    def findDisappearedNumbers(self,nums):
#Brute force approach        
#         n = len(nums)
#         answer =[]

#         for i in range (1, n+1):
#             found = False

#             for num in nums:
#                 if num == i:
#                     found =True
#             if not found:
#                 answer.append(i)
#         return answer

#o(n) approach
        seen = set(nums)
        answer = []

        for i in range(1, len(nums) + 1):
            if i not in nums:
                answer.append(i)
        return answer
sol = Solution()

print(sol.findDisappearedNumbers([4,3,2,7,8,2,3,1]))  # [5, 6]
print(sol.findDisappearedNumbers([1,1]))              # [2]
print(sol.findDisappearedNumbers([1,2,3,4]))          # []


