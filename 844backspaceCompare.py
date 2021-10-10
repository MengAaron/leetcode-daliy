class Solution:
    @staticmethod
    def backspaceCompare(s: str, t: str) -> bool:
        i, j, skipS, skipT = len(s) - 1, len(t) - 1, 0, 0
        while i >= 0 or j >= 0:
            # print(i,j,s[i],t[j])
            while i >= 0:
                print(i, j, s[i], t[j])
                if s[i] == '#':
                    skipS += 1
                    i -= 1
                elif skipS > 0:
                    i -= 1
                    skipS -= 1
                else:
                    break
            while j >= 0:
                if t[j] == '#':
                    skipT += 1
                    j -= 1
                elif skipT > 0:
                    j -= 1
                    skipT -= 1
                else:
                    break
            print(i,j,s[i],t[j],2222)
            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False
            if (i < 0 and j >= 0) or (i >= 0 and j < 0):
                return False
            i -= 1
            j -= 1

        return True


if __name__ == '__main__':
    s = 'a#c'
    t = 'b'
    print(Solution.backspaceCompare(s, t))

