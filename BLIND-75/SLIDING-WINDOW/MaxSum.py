class Solution():
    def MaxSum(selef,nums,k):
        #Brute Force
        # n = len(nums)
        # maximum = float('-inf')

        # for i in range(n -k +1):
        #     total =0 
        #     for j in range(i, i+k):
        #         total += nums[j]
        #         maximum = max(maximum,total)

        # return maximum/k


        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k,len(nums)):
            window_sum += nums[i]
            window_sum -= nums[i-k]
            max_sum = max(max_sum,window_sum)
        return max_sum/k

nums = [1,12,-5,-6,50,3]
k = 4
sol = Solution()
print(sol.MaxSum(nums,k))