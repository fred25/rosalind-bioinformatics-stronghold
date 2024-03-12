def is_interleaved(A:str, B:str, C:str) -> bool:
    if not A and not B and not C:
        return True
    if not C:
        return False
    
    if A and C[0] == A[0]:
        return is_interleaved(A[1:], B, C[1:])
    
    if B and C[0] == B[0]:
        return is_interleaved(A, B[1:], C[1:])
    
    return False

if __name__ == "__main__":
    import sys
    
    s = ""
    DNAS = []
    n = 0
        
    with open(sys.argv[1]) as file:
        data = file.read().split("\n")
        s = data.pop(0)
        DNAS = data
        n = len(DNAS)
    
    matrix = []
    
    for i in range(n):
        matrix.append([])
        for j in range(n):
            A = DNAS[i]
            B = DNAS[j]
            l = len(A) + len(B)
            for k in range(len(s) - l + 1):
                if max(is_interleaved(A, B, s[k:k+l]), is_interleaved(B, A, s[k:k+l])) > 0:
                    matrix[i].append(1)
                    break
            else:
                matrix[i].append(0)  
    for i in matrix:
        print(*i)