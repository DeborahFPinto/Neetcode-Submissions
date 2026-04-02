class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_dup = (set(nums))

        if len(list(set_dup)) == len(nums):
            return False
        else:
            return True