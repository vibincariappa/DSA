#containsduplicate - Psuedocode

# class Solution:
#     def ContainsDuplicate(self,nums):
#         n = len(nums) #determines the length of the arrray 

#         for i in range(n): #iterates through the array -> nums = [1,2,3,1]
#             for j in range(i+1,n): #iterates through the array starting from the next index of i
#                 if nums[i] == nums[j]: #checks if element at index i is equal to elemnet in index j
#                     return True
#         return False

#ContainsDuplicate - Using HashSEt


#Algorithm to check if an array contains duplicate elements

# create set()
# iterate number through our array
#     if number already exists in the set retrun True
# if does not exist add the number to th set
# if the number already exist in the set return false


class Solution:
    def ContainsDuplicate(self,nums):
        seen = set() #creates a set to store unique elements

        for num in nums: #iterates through the array
            if num in seen: #checks if the element is already in the set
                return True #if it is, returns True
            seen.add(num) #if not, adds the element to the set
        return False #if no duplicates are found, returns False




nums = list(map(int, input("Enter Numbers: ").split()))
sol = Solution()
print(sol.ContainsDuplicate(nums))


