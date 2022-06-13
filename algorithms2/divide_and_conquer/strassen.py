def strassen(A, B, n):
    def init_matrix(n):
        return [[0 for _ in range(n)] for _ in range(n)]

    def add(A, B):
        n = len(A)
        temp = init_matrix(n)
        for i in range(n):
            for j in range(n):
                temp[i][j] = A[i][j] + B[i][j]
        return temp

    def subtract(A, B):
        n = len(A)
        temp = init_matrix(n)
        for i in range(n):
            for j in range(n):
                temp[i][j] = A[i][j] - B[i][j]
        return temp

    def strassen_(A, B, n):
        if n == 1:
            C = init_matrix(1)
            C[0][0] = A[0][0] * B[0][0]
            return C

        C = init_matrix(n)
        k = n // 2

        A11 = init_matrix(k)
        A12 = init_matrix(k)
        A21 = init_matrix(k)
        A22 = init_matrix(k)
        B11 = init_matrix(k)
        B12 = init_matrix(k)
        B21 = init_matrix(k)
        B22 = init_matrix(k)

        for i in range(k):
            for j in range(k):
                A11[i][j] = A[i][j]
                A12[i][j] = A[i][j+k]
                A21[i][j] = A[i+k][j]
                A22[i][j] = A[i+k][j+k]
                B11[i][j] = B[i][j]
                B12[i][j] = B[i][j+k]
                B21[i][j] = B[i+k][j]
                B22[i][j] = B[i+k][j+k]

        M1 = strassen_(add(A11, A22), add(B11, B22), k)
        M2 = strassen_(add(A21, A22), B11, k)
        M3 = strassen_(A11, subtract(B12, B22), k)
        M4 = strassen_(A22, subtract(B21, B11), k)
        M5 = strassen_(add(A11, A12), B22, k)
        M6 = strassen_(subtract(A21, A11), add(B11, B12), k)
        M7 = strassen_(subtract(A12, A22), add(B21, B22), k)

        C11 = add(subtract(add(M1, M4), M5), M7)
        C12 = add(M3, M5)
        C21 = add(M2, M4)
        C22 = add(subtract(add(M1, M3), M2), M6)

        for i in range(k):
            for j in range(k):
                C[i][j] = C11[i][j]
                C[i][j+k] = C12[i][j]
                C[j+k][j] = C21[i][j]
                C[i+k][j+k] = C22[i][j]
        return C
    return strassen_(A, B, n)