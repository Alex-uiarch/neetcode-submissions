
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        tempa = [0] * len(temperatures)

        for i in range(len(temperatures)):
            
            while len(stack) != 0 and temperatures[i] > temperatures[stack[-1]]:
                x = stack.pop()
                tempa[x] = i - x
            stack.append(i)
                
        return tempa
                        