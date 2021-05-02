#BFS

import time
graph = {
  'Chennai Central' : ['Potheri','Chennai Beach'],
  'Chennai Beach' : ['Tambaram', 'Kattankulathur'],
  'Potheri' : ['Chennai Central'],
  'Kattankulathur' : [],
  'Tambaram' : ['Chennai Central'],
}

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0)
    print (s, end = " ")

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
t0=time.time()
bfs(visited, graph, 'Chennai Central')
t1=time.time() - t0
print('\nTime taken for execution: {}'.format(t1))