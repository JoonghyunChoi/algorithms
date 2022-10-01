def kmp(text, pattern):
    def lps(pattern):
        n = len(pattern)
        LPS = [0] * n
        j = 0

        for i in range(1, n):
            while j and pattern[i] != pattern[j]:
                j = LPS[j-1]
            if pattern[i] == pattern[j]:
                j += 1
                LPS[i] = j
        return LPS

    def kmp_():
        n, m = len(text), len(pattern)
        result = []
        LPS = lps(pattern)
        j = 0

        for i in range(n):
            while j and text[i] != pattern[j]:
                j = LPS[j-1]
            if text[i] == pattern[j]:
                if j == m-1:
                    result.append(i-j)
                    j = LPS[j]
                else:
                    j += 1
        return result
    return kmp_()