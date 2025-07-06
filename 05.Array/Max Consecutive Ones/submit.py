class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive = 0
        consecutive = 0
        for num in nums:
            if num == 1:
                consecutive += 1
            else:
                if consecutive > max_consecutive:
                    max_consecutive = consecutive
                consecutive = 0
        
        if consecutive > max_consecutive:
            max_consecutive = consecutive
        
        return max_consecutive

# Time complexity: O(n)
# Space complexity: O(1)
