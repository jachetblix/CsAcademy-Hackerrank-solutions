import math
A, B = ( int(temp) for temp in input().split() )
D = math.ceil( ( 1<<B ) / A )
print(D)