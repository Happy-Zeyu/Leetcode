class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        Q, K, V = 0, 1, 1
        for _ in range(3, n+1):
            Q, K, V = K, V, Q + K + V
        return V

solu = Solution()
print(solu.tribonacci(n = 7))

