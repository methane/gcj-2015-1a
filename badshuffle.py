from __future__ import print_function
import random
import sys


N = 1000


def badshuffle(S):
    L = range(S)
    for i in xrange(S):
        x = random.randrange(S)
        L[i], L[x] = L[x], L[i]
    return L


def load_count():
    count = []
    with open('shuffle_count.txt') as f:
        count.append(map(int, f.readline().split()))
    return count

def main():
    T = int(sys.stdin.readline())
    assert T == 120

#    count = [[0] * N for _ in range(N)]
#    for _ in range(1000000):
#        L = badshuffle(N)
#        for pos, n in enumerate(L):
#            count[n][pos] += 1
#
    #for cs in count:
    #    print(' '.join(map(str, cs)))
    count = load_count()

    ts = []
    for t in range(1, T+1):
        _ = int(sys.stdin.readline())
        L = map(int, sys.stdin.readline().split())
        point = 0
        for pos, n in enumerate(L):
            point += count[n][pos]
        ts.append((t, point))
    ts.sort(key=lambda x: x[1])
    P = ts[len(ts)//2][1]
    ts.sort()

    for t, p in ts:
        y = 'GOOD' if p <= P else 'BAD'
        print("Case #{}: {}".format(t, y))

main()
