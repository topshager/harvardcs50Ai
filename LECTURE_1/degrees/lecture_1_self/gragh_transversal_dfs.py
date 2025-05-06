from collections import deque
graph = {
  "A": ["B", "C"],
  "B": ["A", "D", "E"],
  "C": ["A", "F"],
  "D": [],
  "E": ["F"],
  "F": []
}
    
def dfs(graph,start="A"):
    stack = deque()
    visited = set()

    if start not in graph:
        return None


    stack.append((start,[start]))

    while stack:
        current ,path  = stack.pop()

        if current in visited:
            continue
        visited.add(current)

        for neighbor in graph.get(current,[]):
            if neighbor not in visited:
                stack.append((neighbor, path +[neighbor]))
    return visited,path
        
        

        
        
        

