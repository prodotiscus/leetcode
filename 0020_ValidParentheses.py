class Solution:
    def isValid(self, s: str) -> bool:
        ob = {
            1: 0,
            2: 0,
            3: 0
        }
        inc = []
        for e, c in enumerate(s):
            print(ob[1], ob[2], ob[3])
            if ob[1] < 0 or ob[2] < 0 or ob[3] < 0:
                return False
            elif c == "(":
                ob[1] += 1
                inc.append(1)
            elif c == ")":
                if inc and inc.pop() != 1:
                    return False
                ob[1] -= 1
            elif c == "{":
                ob[2] += 1
                inc.append(2)
            elif c == "}":
                if inc and inc.pop() != 2:
                    return False
                ob[2] -= 1
            elif c == "[":
                ob[3] += 1
                inc.append(3)
            elif c == "]":
                if inc and inc.pop() != 3:
                    return False
                ob[3] -= 1
        return ob[1] == ob[2] == ob[3] == 0
