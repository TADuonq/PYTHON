graph = {'S' : ['A', 'B'],
         'A' : ['C', 'D'],
         'B' : ['E', 'F'],
         'C' : ['G'],
         'D' : ['H'],
         'E' : ['D'],
         'F' : ['I'],
         'I' : ['H'],
         'H' : ['G'],
         'G' : []
        }

visited = []
queue = []

def bfs(visited, graph, node): 
  visited.append(node)
  queue.append(node)

  while queue:          
    m = queue.pop(0)
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

print("Đồ thị duyệt theo BFS là")
bfs(visited, graph, 'S')   