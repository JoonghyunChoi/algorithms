def rabin_karp(text, pattern):
    n, m = len(text), len(pattern)   # 1 <= m <= n
    w = 3**(m-1)

    def _hash():
        t_hash = p_hash = 0
        for i in range(m):
            t_hash += ord(text[i])*(3**(m-1-i))
            p_hash += ord(pattern[i])*(3**(m-1-i))
        return t_hash, p_hash

    def rolling_hash(t_hash, i):
        t_hash = 3*(t_hash-ord(text[i])*w) + ord(text[i+m])
        return t_hash

    def rabin_karp_():
        t_hash, p_hash = _hash()
        result = []

        for i in range(n-m+1):
            if t_hash == p_hash:
                j = 0
                while j < m:
                    if text[i+j] == pattern[j]:
                        j += 1
                    else:
                        break
                if j == m:
                    result.append(i)
            if i < n-m:
                t_hash = rolling_hash(t_hash, i)
        return result
    return rabin_karp_()