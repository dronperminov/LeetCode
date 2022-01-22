class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip(' ')

        if not s:
            return 0

        sign = -1 if s[0] == '-' else 1
        index = 1 if s[0] in ['+', '-'] else 0
        number = 0

        while index < len(s) and s[index].isdigit():
            number = number * 10 + int(s[index])
            index += 1

        return max(-2**31, min(2**31 - 1, sign * number))


if __name__ == '__main__':
    solution = Solution()
    assert solution.myAtoi("42") == 42
    assert solution.myAtoi("   -42") == -42
    assert solution.myAtoi("4193 with words") == 4193
    assert solution.myAtoi("+1") == 1
    assert solution.myAtoi("+") == 0
