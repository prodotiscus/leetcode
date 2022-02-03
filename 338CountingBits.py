class Solution:
    def countBits(self, n: int) -> List[int]:
        m = {}
        r = []
        for i in range(n+1):
            i_ = i
            k = 0
            while i != 0:
                k += i % 2
                i //= 2
                if i in m:
                    k += m[i]
                    break
            m[i_] = k
            r.append(k)
        return r
        
