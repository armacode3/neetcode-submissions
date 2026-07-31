class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        paired = list(zip(position, speed))

        sorted_paired = sorted(paired, key=lambda x: x[0], reverse=True) # Reversed order sorted pairs of position and speed (p, s)

        stack = []

        for i in range(len(position)):
            curr_time = (target - sorted_paired[i][0]) / sorted_paired[i][1] # (target - position) / speed

            stack.append(curr_time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

        