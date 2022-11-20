def SOR(A, b, x, N, tol, w):
    maxIterations = 1000000
    xprev = [0.0 for i in range(N)]
    for i in range(maxIterations):
        for j in range(N):
            xprev[j] = x[j]
        for j in range(N):
            summ = 0.0
            for k in range(N):
                if (k != j):
                    summ = summ + A[j][k] * x[k]
            #x[j] = (b[j] - summ) / A[j][j]
            x[j] = w*(b[j] - summ) / A[j][j] + (1-w)*xprev[j]
        diff1norm = 0.0
        oldnorm = 0.0
        for j in range(N):
            diff1norm = diff1norm + abs(x[j] - xprev[j])
            oldnorm = oldnorm + abs(xprev[j])
        if oldnorm == 0.0:
            oldnorm = 1.0
        norm = diff1norm / oldnorm
        if (norm < tol) and i != 0:
            print("Sequence converges to [", end="")
            for j in range(N - 1):
                print(x[j], ",", end="")
            print(x[N - 1], "]. Took", i + 1, "iterations.")
            return
    print("Doesn't converge.")

matrix2 = [[3.0, 1.0], [2.0, 6.0]]
vector2 = [5.0, 9.0]
guess = [0.0, 0.0]
SOR(matrix2, vector2, guess, 2, 0.00000000000001, 0.5)
