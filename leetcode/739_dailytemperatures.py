class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = [0] * len(temperatures)
        stack = []
        for i,temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                ret[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append([temp, i])
        return ret