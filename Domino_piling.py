n, m = list(map(int, input().split(' ')))


def Domino_piling(n, m):
    area = n * m
    return int(area/2)


print(Domino_piling(n, m))
