

class Solution:
    def ValidParenthesis(self,s):
#BruteForce
        # while '()' in s or '[]' in s or '{}' in s:
        #     s = s.repalce("()","")
        #     s = s.replace("[]","")
        #     s = s.replace("{}","")

        # return s == ""

#Optimal Solution using Stack
        stack = []
        pairs ={
            ')' : '(',
            ']' : '[',
            '}' : '{' 
        }

        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return len(stack) == 0

sol = Solution()
print(sol.ValidParenthesis("()[]{}"))
print(sol.ValidParenthesis("(}"))