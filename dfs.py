def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            dfs(visited, graph, i)
visited=set()
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}
dfs(visited,graph,'A')

# Time Complexity : O(V+E)
# Space Complexity : O(V)
