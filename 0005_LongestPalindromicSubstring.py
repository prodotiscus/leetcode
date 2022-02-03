class Solution:
    def longestPalindrome(self, s: str) -> str:
        idx_of_mx = 0
        idx_of_mx_2 = 0
        d1 = [0] * len(s)
        d2 = [0] * len(s)
        l = 0
        r = 0
        i = 0
        while i < len(s):
            print(i,end=' ')
            if i > r:
                j = 1
                while i - j >= 0 and i + j < len(s) and s[i-j] == s[i+j]:
                    d1[i] += 1
                    j += 1
                j -= 1
                l = i - j
                r = i + j
            elif d1[l + r - i] >= r - i:
                d1[i] = r - i
                print('inside',end=' ')
                j = 1
                while i - (r - i) - j >= 0 and r + j < len(s) and s[i - (r - i) - j] == s[r + j]:
                    d1[i] += 1
                    j += 1
                j -= 1
                r = i + d1[i]
                l = i - d1[i]
            else:
                print('else',end=' ')
                d1[i] = d1[l + r - i]
            if d1[i] > d1[idx_of_mx]:
                idx_of_mx = i
            print(d1[i], end=' ')
            print('r=', r, ' l=',l)
            i += 1
        #
        l = 0
        r = -1
        i = 1
        print('\n')
        while i < len(s):
            print(i,end=' ')
            if i > r:
                j = 1
                while i - j >= 0 and i + j - 1 < len(s) and s[i-j] == s[i+j-1]:
                    d2[i] += 1
                    j += 1
                j -= 1
                l = i - j
                r = i + j - 1
                print('trivial',end =' ')
            elif d2[l + r - i + 1] >= r - i + 1:
                #print('r - i + 1 = ', r - i + 1, 'd2')
                d2[i] = r - i + 1
                print('inside',end=' ')
                j = 1
                while i - (r - i + 1) - j >= 0 and r + j < len(s) and s[i - (r - i + 1) - j] == s[r + j]:
                    print('j=',j,'; ',s[i-(r-i+1)-j], '; ', s[r+j])
                    d2[i] += 1
                    j += 1
                j -= 1
                r = i + d2[i] - 1
                l = i - d2[i]
            else:
                print('else',end=' ')
                d2[i] = d2[l + r - i + 1]
            if d2[i] > d2[idx_of_mx_2]:
                idx_of_mx_2 = i
            print('d2 =', d2[i], ' r now ', r)
            i += 1
        #
        print()
        print(idx_of_mx)
        print(d1[idx_of_mx])
        print(idx_of_mx_2)
        print(d2[idx_of_mx_2])
        #while i < len(s):
        ans = ''
        # for i in range(0, 1 + 1)
        if d1[idx_of_mx]*2 + 1 >= d2[idx_of_mx_2]*2:
            ans = s[idx_of_mx]
            for i in range(d1[idx_of_mx]): # for i in range(0, 1) 
                print(ans)
                ans = s[idx_of_mx-1-i] + ans + s[idx_of_mx+1+i]
        else:
            for i in range(d2[idx_of_mx_2]): # for i in range(0, 1) 
                print('kek')
                ans = s[idx_of_mx_2 - i - 1] + ans + s[idx_of_mx_2 + i]
        return ans
