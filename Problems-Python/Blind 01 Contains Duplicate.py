class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Set are unordered, unchangeable, and do not allow duplicate values. Hash Performance.
        check = set()
        for num in nums:
            if num in check:
                return True
            else:
                check.add(num)
        return False
