import numpy as np

def FP(x, a, kMax, epsX, epsF):
    for k in range(1, kMax + 1):
        ck = (x[0] + x[1]) / 2
        fk = F(ck, a)

        if fk * F(x[0], a) > 0:
            x[0] = ck
            x[1] = x[1]
        else:
            x[0] = x[0]
            x[1] = ck

        if abs(x[1] - x[0]) < epsX or abs(fk) < epsF:
            break

    x_star = (x[0] + x[1]) / 2
    error = abs(x[1] - x[0])
    residual = fk

    return x_star, error, residual
