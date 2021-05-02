# DFS

import time
graph = {
    'Sony' : ['Noise','Beats'],
    'Beats' : ['Skullcandy', 'Boat'],
    'Noise' : ['Sony'],
    'Boat' : [],
    'Skullcandy' : ['Sony'],
}

visited = set() # Set to keep track of visited nodes.

def dfs(visited, graph, node):
    if node not in visited:
        print (node,end=' ')
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
t0=time.time()
dfs(visited, graph, 'Sony')
t1=time.time() - t0
print('\nTime taken for execution: {}'.format(t1))