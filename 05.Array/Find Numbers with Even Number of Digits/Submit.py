
class Solution:
    def is_even_digit(self, num):
        digit = 1
        quotient = num
        while quotient >= 10:
            quotient = quotient/10
            digit += 1
        return (digit % 2 == 0)

    def findNumbers(self, nums: List[int]) -> int:
        even_digit_num = 0
        for num in nums:
            if self.is_even_digit(num):
                even_digit_num += 1
        return even_digit_num
        
# Time complexity: O(n)
# Space complexity: O(1)