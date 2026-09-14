class Solution:
    def trap(self, height: List[int]) -> int:
        lst = []
        n = len(height) 

        max_left = [0] * n
        max_right = [0] * n

        max_left[0] = height[0]
        max_right[n -1] = height[n - 1]

        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], height[i])


        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i])





        for i in range(len(height)):
            current = height[i]

            

            water = min(max_left[i], max_right[i]) - current
            if water < 0:
                water = 0
            lst.append(water)
        return sum(lst)


        

        


