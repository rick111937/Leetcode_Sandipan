class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        if num > 0:
            digits = sorted(str(num))
            for i, d in enumerate(digits):
                if d != '0':
                    smallest = [digits[i]] + digits[:i] + digits[i+1:]
                    return int("".join(smallest))
        else:
            digits = sorted(str(-num), reverse=True)
            return -int("".join(digits))