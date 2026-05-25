class Solution:
    def monkeyMove(self, n: int) -> int:
        MOD = 10**9 + 7
        total = pow(2, n, MOD)
        return (total - 2) % MOD