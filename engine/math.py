def transpose(A):
    n = len(A)
    m = len(A[0])

    result = []
    for j in range(m):
        row = []
        for i in range(n):
            value = A[i][j]
            row.append(value)
        result.append(row)

    return result

def dot(A, B):

    if (type(A) in [int, float]) and (type(B) in [int, float]):
        return A * B

    elif (type(A) in [int, float]) and type(B) == list:
        result = []
        for i in range(len(B)):
            value = A * B[i]
            result.append(value)
        
        return result

    elif type(A) == list and (type(B) in [int, float]):
        return dot(B, A)

    n = len(A)
    m = len(A[0])

    result = []
    for i in range(n):
        row = []
        for j in range(m):
            vA = Vector(A[i])
            vB = Vector(transpose(B)[j])
            value = vA.dot(vB)
            row.append(value)
        result.append(row)

    return result

def identity(n):
    result = []
    for i in range(n):
        row = []
        for j in range(m):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        result.append(row)

    return result
    