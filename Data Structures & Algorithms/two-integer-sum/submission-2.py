class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dupe = {}

        for i, x in enumerate(nums):
            need = target - x
            if need in dupe:
                return [dupe[need], i]
            else:
                dupe[x] = i  


            
