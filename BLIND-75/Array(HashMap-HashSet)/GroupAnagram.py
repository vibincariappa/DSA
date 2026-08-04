from collections import defaultdict
class Solution:

#Brute Force
    # def isAnagram(self,s,t):
    #     if len(s)!=len(t):
    #         return False

    #     t_list = list(t)

    #     for ch in s:
    #         found = False
        
    #         for i in range(len(t_list)):
    #             if t_list[i] == ch:
    #                 t_list[i] = None
    #                 found = True
    #                 break
                
    #         if not found:
    #             return False

    #     return True

    # def GroupAnagram(self,strs):
    #     result = []
    #     visited = [False]*len(strs)

    #     for i in range(len(strs)):
    #         if visited[i]:
    #             continue

    #         group = [strs[i]]
    #         visited[i] = True
        
    #         for j in range(i+1,len(strs)):
    #             if not visited[j] and self.isAnagram(strs[i], strs[j]):
    #                 group.append(strs[j])
    #                 visited[j] = True
    #         result.append(group)
    #     return result

#USing HashMap
    # def GroupAnagram(self,strs):
    #     group = default(list)

    #     for word in strs:
    #         key = "".join(sorted(word))
    #         group[key].append(word)

    #     return list(group.values())

    def GroupAnagram(self,strs):
        group = defaultdict(list)

        for word in strs:
            count = [0]*26

        for ch in word:
            count[ord(ch) - ord('a')] += 1
            group[tuple(count)].append(word)

        return list(group.values())

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

sol = Solution()
print(sol.GroupAnagram(words))