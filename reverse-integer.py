class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        x = abs(x)
        result = 0

        while x:
            result = result * 10 + x % 10
            x //= 10

        result *= sign
        return result if -2**31 <= result <= 2**31-1 else 0


if __name__ == '__main__':
    solution = Solution()
    assert solution.reverse(123) == 321
    assert solution.reverse(-123) == -321
    assert solution.reverse(120) == 21
    assert solution.reverse(1534236469) == 0
