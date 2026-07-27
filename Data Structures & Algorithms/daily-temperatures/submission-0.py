class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # Minimum Stack

        result = [0 for i in range(len(temperatures))]

        # Both index and temperature
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                index = stack.pop()[1]
                days_waited = i - index
                result[index] = days_waited
            
            stack.append([temp, i])

        return result
                

