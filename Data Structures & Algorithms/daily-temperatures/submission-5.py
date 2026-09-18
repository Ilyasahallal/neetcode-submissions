class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        stack=[]
        result=[0]*n
        for i in range(n):
            if not stack:
                stack.append(i)
            else:
                while stack and temperatures[i] > temperatures[stack[-1]]:
                    a=stack[-1]
                    result[a] = i-a
                    stack.pop()
                stack.append(i)
        return result
