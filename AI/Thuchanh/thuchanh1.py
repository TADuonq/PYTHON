import collections

def bfs(graph, root):

    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


if __name__ == '__main__':
    graph = {'S': ['A', 'B'], 
             'A': ['C', 'D'], 
             'B': ['E', 'F'],  
             'E': ['D'], 
             'F': ['I'],
             'C': ['G'], 
             'I': ['H'],
             'D': ['H'], 
             'H': ['G'],
             'G': []
             }
    print("Đồ thị duyệt theo BFS là: ")
    bfs(graph, 'S')