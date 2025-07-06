class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_sum = 0
        for people in accounts:
            sum = 0
            for acct in people:
                sum += acct
            if sum > max_sum:
                max_sum = sum
        
        return max_sum

        