class Solution:
    def countPrimes(self, n):
        prime = [True] * n
        prime[:2] = [False, False]

        for i in range(2, int(n**0.5) + 1):
            if prime[i]:
                for j in range(i*i, n, i):
                    prime[j] = False

        return sum(prime)