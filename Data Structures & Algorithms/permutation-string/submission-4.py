

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_s = sorted(s1)
        s1_set = set(s1)
        while len(s2) >= len(s1):
            k = [g for x in s1_set if (g:=s2.find(x)) >= 0]
            if k == []:
                return False
            min_ind = min(k)
            check = s2[min_ind:min_ind + len(s1)]
            s2 = s2[min_ind + 1:]
            if s1_s == sorted(check):
                return True
        return False
        