import math
N, M, S = (int(s) for s in input().split())
print(int((S * math.ceil(math.log2(N))) + ((N - 1) * M)))