def ucs(nodes, src, goal): 
    pq = {} 
    pq[src] = 0
    explored = []

    while True:
        sumd = 0
    #this is to sort the nodes dict 
        pq = dict(sorted(pq.items(), key = lambda a : a[1]))   

    #get the dictionary containing the neighbours and store it in varible neighbour
        lead = list(pq.keys())
        if lead[0] in explored:
            pq.pop(lead[0])
            continue
        neighbour = neighbourhood(lead[0], nodes)
    
    #calculating cost incurred upto that point
    
        sumd = pq[lead[0]]

    #deleting the current node from the dictionary
        pq.pop(lead[0])
        explored.append(lead[0])
    #emptying the list lead for reuse
        lead = []

    #calculating the cost incurred after having reached the neighbours
        for i in neighbour:
            neighbour[i] = neighbour[i] + sumd 
        sumd = 0

    #insert the neighbours into the priority queue
        for i in neighbour:
            pq[i] = neighbour[i]
            print(i)
        if goal in pq:
            print(pq[goal])
            break
            

def neighbourhood(ele, nodes):
    return nodes[ele]

nodes = {
        'a': {'b': 5,'d': 3},

        'b': {'c': 1},

        'c': {'e': 6, 'g': 8},

        'd': {'e': 2, 'f': 2},

        'e': {'b': 4},

        'f': {'g': 3},

        'g': {'e': 4}
        }


ucs(nodes, 'a', 'g')
