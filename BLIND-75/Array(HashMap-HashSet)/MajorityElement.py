class Solution:
    def MajorityElements(self,nums):

#BruteForce
        # for num in nums:
        #     count = 0
        #     n = len(nums)

        #     for value in nums:
        #         if value == num:
        #             count += 1
        #     if count > n // 2:
        #         return num


#Hashmap
        # count = {}

        # for num in nums:
        #     count[num] = count.get(num,0)+1

        # for num,freq in count.items():
        #     if freq > len(nums) // 2:
        #         return num

#using sort function

        nums.sort()
        return nums[len(nums)//2]
        
sol = Solution()
print(sol.MajorityElements([3,2,3]))