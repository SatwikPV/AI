def square(arr):
    graph = {
            arr : produceArr() 
            }

    visited = []
    queue = []

    visited.append(arr)
    queue.append(arr)
    print(arr + " ")
    
    while queue:
        m = queue.pop(0)

        if m not in graph:
            graph[m] = produceArr(m)

        for child in graph[m]:
            if child not in visited:
                visited.append(child)
                queue.append(child)
                print(child)

def produceArr(arr):
    for i in range(0, len(arr)):
        if arr[i] == -1
    marker = i

    
    try:
        e1 = lambda arr: swap(marker, marker-3, arr)
    except:
        e1 = []

    try:
        e2 = lambda arr: swap(marker, marker+3, arr)
    except:
        e2 = []

    try:
        e3 = lambda arr: swap(marker, marker-1, arr)
    except:
        e3 = []
    
    try:
        e4 = lambda arr: swap(marker, marker+1, arr)
    except:
        e4 = []

return [e1, e2, e3, e4]

    

def swap(a, b, arr):
    arr[t] = arr[a]
    arr[a] = arr[b]
    arr[b] = arr[t]

    return arr

arr = [0, 1, 2, 3, 8, 4, -1, 5, 6, 7]


