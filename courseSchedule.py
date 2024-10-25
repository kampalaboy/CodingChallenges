#integer n 
#courses labeled 0 to n-1
#prerequisites[i] = [a,b] where you need to take course b before course a


#Depth First Search
# def dfs(graph, vertex, path, order, visited):
#     path.append(vertex)
#     for neighbor in graph[vertex]:
#         if neighbor in path:
#             return False
#         if neighbor not in visited:
#             visited.add(neighbor)
#             if not dfs(graph, vertex, path, order, visited):
#                 return False
#     path.remove(vertex)
#     order.append(path.pop())
#     return True

# def sort(graph):
#     visited = set()
#     path =[]
#     order =[]
#     for vertex in graph:
#         if vertex not in visited:
#             visited.add(vertex)
#             dfs(graph, vertex, path, order, visited)
#     return order[::-1]

# def course(n, prerequisites):
#     graph =[[] for i in range(n)]
#     for pre in prerequisites:
#         graph[pre[1]].append(pre[0])
#     visited = set()
#     path = set()
#     order = []
#     for course in range(n):
#         if course not in visited:
#             visited.add(course)
#             if not dfs(graph, course, path, order, visited):
#                 return False
#     return True

#Breadth First Search
from collections import deque

def course(n, prerequisites):
    graph =[[] for i in range(n)]
    indegree =[0 for i in range(n)]
    for pre in prerequisites:
        graph[pre[1]].append(pre[0])
        indegree[pre[0]] += 1
    order = []
    queue = deque([i for i in range(n) if indegree[i]==0])
    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbor in graph[vertex]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return len(order) == n  