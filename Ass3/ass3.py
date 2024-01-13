from collections import defaultdict, deque

class MyGraph:
    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_connection(self, u, v):
        self.adj_list[u].append(v)

    def traverse_dfs(self, start, order='left'):
        visited = set()
        stack = [(start, [])]
        result = []

        while stack:
            current, path = stack.pop()
            if current not in visited:
                visited.add(current)
                path = path + [current]
                result.append(path)
                stack.extend((neighbor, path) for neighbor in sorted(self.adj_list[current], reverse=(order == 'right')))

        return result

    def traverse_bfs(self, start, order='left'):
        visited = set()
        queue = deque([(start, [start])])
        result = []

        while queue:
            current, path = queue.popleft()
            #print("current: ", current, " path: ", path)
            if current not in visited:
                visited.add(current)
                result.append(path)
                queue.extend((neighbor, path + [neighbor]) for neighbor in self.adj_list[current] if neighbor not in visited)

        return result

    def detect_cycles(self, start, path, visited, cycles):
        visited[start] = True
        path = path + [start]
        # print("")
        # print("inside detect cycles for: ", start)
        # print("----------------------------")
        for neighbor in self.adj_list[start]:
            # print("in neighbor: ", neighbor)
            # print("visited: ", visited)
            if not visited[neighbor]:
                # print("found unvisited neighbor ", neighbor)
                self.detect_cycles(neighbor, path, visited, cycles)
            elif neighbor in path:
                # print("found cycle ending in: ", neighbor)
                cycle_start = path.index(neighbor)
                cycles.append(path[cycle_start:])
                # print("new cycles: ", cycles)
        
        visited[start] = False

    def detect_all_cycles(self):
        cycles = []
        visited = {node: False for node in self.adj_list}

        for node in self.adj_list:
            if not visited[node]:
                self.detect_cycles(node, [], visited, cycles)

        unique_cycles = []
        for cycle in cycles:
            min_index = min(range(len(cycle)), key=cycle.__getitem__)
            rotated_cycle = cycle[min_index:] + cycle[:min_index]
            if rotated_cycle not in unique_cycles:
                unique_cycles.append(rotated_cycle)

        return unique_cycles

    def check_bipartite(self):
        color = {}
        queue = deque([1])
        color[1] = 0

        while queue:
            current = queue.popleft()

            for neighbor in self.adj_list[current]:
                if neighbor not in color:
                    color[neighbor] = 1 - color[current]
                    queue.append(neighbor)
                elif color[neighbor] == color[current]:
                    return False

        return True

graph = MyGraph()
edges = [(1, 3), (1, 4), (2, 1), (2, 3), (3, 4), (4, 1), (4, 2)]

for edge in edges:
    graph.add_connection(edge[0], edge[1])

print("DFS:", graph.traverse_dfs(1))
print("BFS:", graph.traverse_bfs(1))
print("Cycles:", graph.detect_all_cycles())
print("Is Bipartite:", graph.check_bipartite())
