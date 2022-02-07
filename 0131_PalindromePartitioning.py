class Solution:
    @staticmethod
    def is_palindrome(s):
        for i in range((len(s) + 1) // 2):
            if s[i] != s[-i-1]:
                return False
        return True

    def partition(self, s):
        if len(s) == 1:
            return [[s]]
        if s == '':
            return [[]]
        ans = []
        for i in range(len(s)):
            #print('i =', i)
            if self.is_palindrome(s[0:i+1]):
                variants = self.partition(s[i+1:])
                for v in variants:
                    #print('v =', v)
                    #print(s[0:i+1] +)
                    ans.append([s[0:i+1]] + v)
        return ans
