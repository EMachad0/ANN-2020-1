E = [[4,1,1,6], [2,5,2,3], [1,2,4,11]] # matrix estendida do sistema
# 4x+y+z=6 --> x = (6 - y - z) / 4
# 2x+5y+2z=3 --> y = (3 - 2x - 2z) / 5
# x+2y+4z=11 --> z = (11 - x - 2y) / 4

def test(matrix, vec):
    err = []
    for row in matrix:
        prod = abs(sum([col * vec for col, vec in zip(row[:-1], vec)]) - row[-1])
        err.append(prod)
    return err

n  = 20
itr = {}
chute = [0,0,0]
for i in range(n):
    xn = []
    for j, row in enumerate(E):
        chute = xn + chute[len(xn):] # this line updates chute
        subs = sum([el * chute[k] for k, el in enumerate(row[:-1]) if k != j])
        subs = (row[-1] - subs) / row[j]
        xn.append(subs)
    print(i, xn, test(E, xn))
    chute = xn

