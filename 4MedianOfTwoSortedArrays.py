class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        i, j = 0, 0
        l = len(a) + len(b)
        merged = []
        while i < len(a) or j < len(b):
            if j == len(b) or (i < len(a) and a[i] < b[j]):
                merged.append(a[i])
                i += 1
            else:
                merged.append(b[j])
                j += 1

        if len(merged) % 2 == 0:
            return (merged[len(merged) // 2 - 1] + merged[len(merged) // 2]) / 2
        else:
            return merged[len(merged) // 2]
        
        
