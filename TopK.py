class Solution:
    def TopK(self,nums,k):
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        result = []

        for _ in range(k):
            max_freq = -1
            max_element = None

            for num in freq:
                if freq[num] > max_freq:
                    max_freq = freq[num]
                    max_element = num

            result.append(max_element)
            del freq[max_element]

        return result
nums = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter k: "))

sol = Solution()
print(sol.TopK(nums, k))