from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

def siftDown(a, i):
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
        a[i], a[min_index] = a[min_index], a[i]
        siftDown(a, min_index)

def siftUp(a, i):
    while i > 0 and a[(i-1)//2] > a[i]:
        a[(i-1)//2], a[i] = a[i], a[(i-1)//2]
        i = (i-1)//2


def changePriority(a, i, p):
    p_old = a[i]
    a[i] = p
    if p > p_old:
        siftUp(a, i)
    else:
        siftDown(a, i)


def buildHeap(data):
    for i in range(((len(data) // 2) - 1), -1, -1):
        siftDown(data, i)


def assign_jobs(n_workers, jobs):
    assignments = [] * len(jobs)
    start_times = [] * len(jobs)
    workers = buildHeap(n_workers)
    for i in range(len(jobs)):
        assignments[i] = [i]

def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
