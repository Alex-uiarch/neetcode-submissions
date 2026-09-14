class Solution:
    def groupAnagrams(self, strs: List[str]):

        visited = {}
        for x in strs:
            
            xs = "".join(sorted(x))

            if xs in visited:
                visited[xs].append(x)
            else:
                visited[xs] = [x]

        lst = []

        for x in visited:

            lst.append(visited[x])

        return lst

        

