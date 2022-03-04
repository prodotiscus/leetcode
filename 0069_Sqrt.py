class Solution:
    def mySqrt(self, x: int) -> int:
        return self.binSearch(x, 0, x)
    
    def binSearch(self, x: int, a: int, b: int):
        med = (a + b) / 2
        if int(med * med) == x:
            return int(med)
        elif int(med * med) < x:
            return self.binSearch(x, med, b)
        elif int(med * med) > x:
            return self.binSearch(x, a, med)
