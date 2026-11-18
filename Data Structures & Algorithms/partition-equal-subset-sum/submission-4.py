class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2 != 0:
            return False

        part = int(sum(nums) / 2)

        lst = {0}

  

        for x in nums:
            lst1 = set()
            for j in lst:
                if x + j == part:
                    return True
                lst1.add(x + j)
            lst.update(lst1)



        return False