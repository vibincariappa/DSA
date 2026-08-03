class Solution:
    def ValidAnagram(self, s, t):
        if len(s) != len(t):
            return False
#BruteForce Approach
#         t_list = list(t)

#         for ch in s:
#             found = False

#             for i in range(len(t_list)):
#                 if t_list[i] == ch:
#                     t_list[i] = None
#                     found = True
#                     break

#             if not found:
#                 return False

#         return True


#o(n) Approach

        # count = {}

        # for ch in s:
        #     count[ch] = count.get(ch,0)+1

        # for ch in t:
        #     if ch not in count:
        #         return False

        #     count[ch] -= 1

        #     if count[ch] < 0:
        #         return False

        # return True

#0(1) Approach

        count = [0]*26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        for ch in t:
            count[ord(ch) - ord('a')] -=1

        return all(x==0 for x in count)
    
    



s = input("Enter first string: ")
t = input("Enter second string: ")

sol = Solution()
print(sol.ValidAnagram(s, t))