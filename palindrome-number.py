class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x):
            return False

        reverse = 0

        while x > reverse:
            reverse = reverse * 10 + x % 10
            x //= 10

        return x == reverse or reverse // 10 == x


if __name__ == '__main__':
    solution = Solution()
    assert solution.isPalindrome(121)
    assert not solution.isPalindrome(-121)
    assert not solution.isPalindrome(10)
