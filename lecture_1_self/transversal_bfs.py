from collections import deque
graph = {
  "A": ["B", "C"],
  "B": ["A", "D", "E"],
  "C": ["A", "F"],
  "D": [],
  "E": ["F"],
  "F": []
}


def bfs(graph,start="A"):
    queue =  deque()
    visited = set()

    if start not in graph:
        return  None
        
    queue.append((start,[start]))

    
    while queue:
        current ,path = queue.popleft()
        
        if current in visited:
            continue
        visited.add(current)

        for neighbor in graph.get(current,[]):
            if neighbor not in visited:
                queue.append((neighbor,path + [neighbor]))

    return visited