class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''

        for x in strs:
            length = len(x)
            s += str(length) + '#' + str(x)

        return s
    
    def decode(self, s: str) -> List[str]:
        lst = []
        char = ''
        while s:
            length = ''
            for x in s:
                if x != '#':
                    length += x
                if x == '#':
                    break
                    
            length = int(length)
            print(length)
            

            for i in range(len(str(length)) + 1, length + len(str(length)) + 1):
                char += s[i]
            lst.append(char)

            s = s[length + len(str(length)) + 1: ]
            char = ''
        return lst






