class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        temperatures
        n = len(temperatures)
        answer = [0] * n
        stack = []

        for i, v in enumerate(temperatures):
            while stack and stack[-1][0] < v:
                stack_v, stack_i = stack.pop()
                answer[stack_i] = i - stack_i

            stack.append((v, i))
        
        return answer