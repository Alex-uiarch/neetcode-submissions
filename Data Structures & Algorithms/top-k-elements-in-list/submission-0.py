class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        visited = {}
        for x in nums:
            if x in visited:
                visited[x] += 1
            else:
                visited[x] = 1

        sorted_visited = sorted(visited, key=lambda key: visited[key], reverse=True)

        lst = []
        for i in range(k):
            lst.append(sorted_visited[i])
        return lst

        
