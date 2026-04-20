class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        hash_map={')':'(',']':'[','}':'{'}
        for i in s:
            if i in hash_map:
                top=stack.pop() if stack else '#'
                if hash_map[i]!=top:
                    return False   
            else:
                stack.append(i)
        return not stack   

        