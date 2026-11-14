class Solution:



        
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0] 
        lsts = []

        left = 0
        right = 0

        lst1 = []
        for right in range(len(nums)):
            if nums[right] == 0:
                lst1.append(0)
                lsts.append(nums[left: right])
                left = right + 1
            elif right == len(nums) - 1:
                lsts.append(nums[left: ])



        


        for x in lsts:
            dct = {}
            
            for i in range(len(x)):
                if x[i] < 0:
                    dct[i] = x[i]

            if len(dct) % 2 == 0:
                if len(x) > 0:
                    uns = 1
                    for x1 in x:
                        uns *= x1

                    lst1.append(uns)

            else:
                if len(dct) == 1:
                    if len(x[ :list(dct)[0]]) != 0:
                        uns = 1
                        for x1 in x[ :list(dct)[0]]:
                            uns *= x1
                        max1 = uns
                    else:
                        max1 = float('-inf')

                    if len(x[list(dct)[0] + 1: ]) != 0:
                        uns = 1
                        for x1 in x[list(dct)[0] + 1: ]:
                            uns *= x1
                        max2 = uns
                    else:
                        max2 = float('-inf')

                    lst1.append(max(max1, max2))
                    



                else:

                    if len(x[ :list(dct)[-1]]) != 0:
                        uns = 1
                        for x1 in x[ :list(dct)[-1]]:
                            uns *= x1
                        max1 = uns
                    else:
                        max1 = float('-inf')

                    if len(x[list(dct)[0] + 1: ]) != 0:
                        uns = 1
                        for x1 in x[list(dct)[0] + 1: ]:
                            uns *= x1
                        max2 = uns
                    else:
                        max2 = float('-inf')
                    lst1.append(max(max1, max2))


        return max(lst1)
                