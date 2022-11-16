graph = {
        '1' : ['2', '3', '4'],
        '2' : ['5', '6'],
        '5' : ['9', '10'],
        '6' : [],
        '3' : [],
        '4' : ['7', '8'],
        '7' : ['11', '12'],
        '8' : [],
        '9' : [],
        '10' : [],
        '11' : [],
        '12' : []
        }

  

def bfs(graph, start): 
    visited = [] 
    queue = []   
    visited.append(start)
    queue.append(start)
    print(start + " ")
    
    while queue:         
        m = queue.pop(0) 
       
        for child in graph[m]:
            if child not in visited:
                visited.append(child)
                queue.append(child)
                print(child + " ")

bfs(graph, '1')  
