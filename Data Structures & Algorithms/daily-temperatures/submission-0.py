class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            temp = temperatures[i]
            if not s or temp <= s[-1][0]:
                s.append((temp, i))
            else:
                while s and temp > s[-1][0]:
                    popped = s.pop()
                    result[popped[1]] = i - popped[1]
                s.append((temp, i))
        return result
        