class Solution:
    def MoveZero(self,nums):
        temp = []
#BruteForce
#Algorithm
# Create a temp list
# Iterate through and find non zero ekements
# Find the zero elements
# Append in temp list
# Copy the non zero and zero elements back to the array

        # for num in nums:
        #     if num != 0:
        #         temp.append(num)

        # while len(temp) < len(nums):
        #     temp.append(0)

        # for i in range(len(nums)):
        #     nums[i] = temp[i]

#TwoPointers
#Algorithm
# left = 0
# for right in range of 0 - n-1
#     if nums in right is not zero
#         swap nums in right with nums in lef
#         left += 1

        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

nums = [0,1,2,19,0,12]
sol = Solution()
sol.MoveZero(nums)
print(nums)