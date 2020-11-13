import random


def PolyHash(S, p, x):
    hash = 0
    for i in range(len(S) - 1, -1, -1):
        hash = (hash * x + ord(S[i])) % p
    return hash

def PrecomputeHashes(T, P, p, x):
    H = [None] * (len(T) - len(P) + 1)
    S = T[len(T)-len(P) : len(T)]
    H[len(T) - len(P)] = PolyHash(S, p, x)
    y = 1
    for i in range(1, len(P) + 1):
        y = (y * x) % p
    for i in range(len(T) - len(P) - 1, -1, -1):
        H[i] = (x*H[i+1] + ord(T[i]) - y*ord(T[i+len(P)])) % p
    return H

def RabinKarp(P, T):
    p = 10000000007
    x = random.randint(1, p)
    result = []
    pHash = PolyHash(P, p, x)
    H = PrecomputeHashes(T, P, p, x)
    for i in range(len(T) - len(P) + 1):
        if pHash != H[i]:
            continue
        if T[i : i+len(P)] == P:
            result.append(i)
    return result


def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

if __name__ == '__main__':
    print_occurrences(RabinKarp(*read_input()))
