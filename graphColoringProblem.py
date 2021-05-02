#Exp-2 Graph Coloring
colors=['red','green','blue']
print('Number of colors used: ', len(colors))
vertices=['1','2','3','4','5']
adj={'1':['2','5'],'2':['1','3','5'],'3':['2','4','5'],'4':['3','5'],'5':['4','1','2','3']}
result={}
for vertex in vertices:
  adj_color=[]
  neighbour=adj[vertex]
  for i in neighbour:
    if i in result.keys():
      adj_color.append(result[i])
  for color in colors:
    if color not in adj_color:
      break
  result[vertex]=color
for (vertex,color) in result.items():
  print("Color assigned to vertex",vertex,"adjacent to",adj[vertex],"is",color)
