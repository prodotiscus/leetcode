class Solution:
    def __init__(self):
        self.d = {}
    
    def myPow(self, x, n):
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n == -1:
            return 1 / x

        if n in self.d:
            return self.d[n]

        self.d[n] = self.myPow(x, n // 2) * self.myPow(x, n // 2) * self.myPow(x, n % 2)
        return self.d[n]
