from typing import Generator

def mk_graph(array):
    graph = defaultdict(list)
    for i, value in enumerate(array):
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


def split_file_newlines(file_name: str) -> list[str]:
    lines = []
    with open(file_name, 'r') as file:
        lines = file.read().splitlines()
    return lines

def map_values(lines: list[str]) -> list[list[str]]:
    map = []
    for line_i, line in enumerate(lines):
        map.append([])
        for value_i, value in enumerate(line.split(';')):
            map[line_i].append(f'{value_i}:{value}')
    return map


def find_needle(needle: str, map: list[list[str]]) -> Generator[int, None, None]:
    for line_i, line in enumerate(map):
        if needle in line:
            yield line_i
            continue


def group_values(split_file_content: list[str], map: list[list[str]]):
    groups = {}
    for group_n, line in enumerate(map):
        groups[group_n] = []
        for value in line:
            for line_i in find_needle(value, map):
                groups[group_n].append(split_file_content[line_i])
    return groups


if __name__ == '__main__':
    newlines_split = split_file_newlines('lng.txt')
    mapped_values = map_values(newlines_split)
    grouped_values = group_values(newlines_split, mapped_values)
    for group_n, values in grouped_values.items():
        print(f'Group {group_n + 1}')
        for value in values:
            print(f'  {value}')
