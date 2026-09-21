class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        count_s2 = {}
        left = 0
        

        for x in s1:
            if x not in count:
                count[x] = 1
            else:
                count[x] += 1


        for right in range(len(s2)):

            if s2[right] not in count_s2:
                count_s2[s2[right]] = 1
            else:
                count_s2[s2[right]] += 1

            print(count_s2)


            if sum([count[x] for x in count]) == sum([count_s2[x] for x in count_s2]) and count == count_s2:
                return True
            elif sum([count[x] for x in count]) == sum([count_s2[x] for x in count_s2]):
                count_s2[s2[left]] -= 1
                if count_s2[s2[left]] == 0:
                    del count_s2[s2[left]]

                left += 1

        return False
