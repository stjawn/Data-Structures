def siftDown(a, i):
    global swaps
    n = len(a)
    min_index = i
    l = (2 * i) + 1
    r = (2 * i) + 2
    # print(i,l,r)
    if l < n and a[l] < a[min_index]:
        min_index = l
    if r < n and a[r] < a[min_index]:
        min_index = r
    if min_index != i:
        swaps.append((i, min_index))
        # print(swaps)
        a[i], a[min_index] = a[min_index], a[i]
        siftDown(a, min_index)


def build_heap(data):
    global swaps
    for i in range(((len(data) // 2) - 1), -1, -1):
        siftDown(data, i)
    # print(data)
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)

swaps = []
if __name__ == "__main__":
    main()
