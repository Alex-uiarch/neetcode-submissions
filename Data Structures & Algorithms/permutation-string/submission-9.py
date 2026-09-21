class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_s = sorted(s1)
        s1_set = set(s1)
        while len(s2) >= len(s1):
            min_ind = None
            for i, ch in enumerate(s2):
                if ch in s1_set:
                    min_ind = i
                    break
            if min_ind == None:
                return False
            # k = [g for x in s1_set if (g:=s2.find(x)) >= 0]
            # if k == []:
            #     return False
            # min_ind = min(k)
            if s1_s == sorted(s2[min_ind:min_ind + len(s1)]):
                return True
            s2 = s2[min_ind + 1:]
        return False
