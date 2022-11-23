def swap(a, b, arr):
    arr[t] = arr[a]
    arr[a] = arr[b]
    arr[b] = arr[t]


def produceArr(arr):
    for i in range(0, len(arr)):
        if arr[i] == -1
    marker = i

    try:
        e1 = lambda arr: swap(marker, marker - 3, arr)
    except:
        e1 = []

    try:
        e2 = lambda arr: swap(marker, marker - 3, arr)
    except:
        e2 = []

    try:
        e3 = lambda arr: swap(marker, marker - 1, arr)
    except:
        e3 = []

    try:
        e4 = lambda arr: swap(marker, marker + 1, arr)
    except:
        e4 = []

    return [e1, e2, e3, e4]

def dls(src, target, maxDepth):
    if src = target : 
        return True

    if maxDepth <= 0: 
        return False

    if src not in graph:
        graph[src] = produceArr(src)        

    for i in graph[src]:
        if(dls(i, target, maxDepth - 1)):
            return True

    return False

def ids(src, target, maxDepth):
    graph = {
        src = produceArr(src)
            }
    
    for i in range(maxDepth):
        if(dls(src, target, i)):
            return True
        return False




src = [0, 1, 2, 3, 5, 4, 6, -1, 7, 8]
target = [0, 1, 2, 3, 4, 5, 6, 7, 8, -1]
ids(src, target, 1)