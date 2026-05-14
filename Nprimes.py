import math
N = int(input())
cp = 2
while N > 0:
#   print( f"{cp=}, {range(2, int(math.sqrt(cp))+1)=}")
    for i in range(2, int(math.sqrt(cp))+1):
        if cp % i == 0:
            break;
    else:
        print( cp, N )
        N -= 1
    cp += 1
