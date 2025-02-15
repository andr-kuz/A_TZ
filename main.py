from collections import defaultdict

input_list = []

with open("lng1.txt", "r") as file:
    reader = file.readlines()
    for i in reader:
        input_list.append(i.strip().split(";"))
graph = mk_graph(input_list)
res = return_grouped(input_list)

for i in range(len(res)):
    print(f"Group {i+1}: {res[i]}")


def mk_graph(array):
    graph = defaultdict(list)
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            for k in range(min(len(array[i]), len(array[j]))):
                if array[i][k] == array[j][k]:
                    graph[i].append(j)
                    graph[j].append(i)
                    break
    return graph


def dfs(node, visited, arr, graph):
    group = []
    stack = [node]
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            group.append(arr[current])
            for neighbor in graph[current]:
                if neighbor not in visited:
                    stack.append(neighbor)
    return group


def return_grouped(array):
    visited = set()
    result = []
    for i in range(len(array)):
        if i not in visited:
            group = dfs(i, visited, input_list, graph)
            result.append(group)
    return result
