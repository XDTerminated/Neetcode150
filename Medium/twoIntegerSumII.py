class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        a = 0
        b = len(numbers) - 1

        while a < b:
            s = numbers[a] + numbers[b]

            if s == target:
                return [a + 1, b + 1]

            elif s < target:
                a+=1

            elif s > target:
                b -= 1
