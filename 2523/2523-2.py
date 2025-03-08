class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        ans = [-1, -1]
        primes = []
        p = [0] * (10**6 + 1)
        for i in range(2, right + 1):
            if (not p[i]):
                if (left <= i <= right):
                    primes.append(i)
                for j in range(i * i, right + 1, i):
                    p[j] = 1
        if len(primes) < 2:
            return [-1, -1]
        elif len(primes) == 2:
            return primes
        else:
            ans = [primes[0], primes[1]]
            best = ans[1] - ans[0]
            for i in range(1, len(primes)):
                if primes[i] - primes[i - 1] <= 2:
                    return [primes[i - 1], primes[i]]
                if primes[i] - primes[i - 1] < best:
                    best = primes[i] - primes[i - 1]
                    ans = [primes[i - 1], primes[i]]
        return ans
