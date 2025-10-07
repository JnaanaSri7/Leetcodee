class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total_sum = n * (n + 1) //2
        count = n // m
        sum_multiples = m * (count * (count + 1) // 2)
        return total_sum - 2 * sum_multiples

        
