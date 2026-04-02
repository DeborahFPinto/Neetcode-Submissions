class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        tam = len(numbers)

        for i in range(tam):
            if target - numbers[i] in numbers:
                return [i + 1, numbers.index(target - numbers[i]) + 1]

