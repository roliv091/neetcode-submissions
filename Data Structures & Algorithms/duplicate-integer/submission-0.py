class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupeCheck = set()

        for n in nums:
            if n in dupeCheck:
                return True
            dupeCheck.add(n)
        return False