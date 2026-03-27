from collections import defaultdict

# Graph representation (same as your PDF)
graph = {
    1: [3, 2],
    2: [4],
    3: [5, 4],
    4: [1, 6],
    5: [6],
    6: []
}

visited = set()
stack = []

def dfs(v):
    visited.add(v)
    for u in graph[v]:
        if u not in visited:
            dfs(u)
    stack.append(v)

for v in graph:
    if v not in visited:
        dfs(v)
transpose = defaultdict(list)
for v in graph:
    for u in graph[v]:
        transpose[u].append(v)
visited.clear()

def dfs2(v, component):
    visited.add(v)
    component.append(v)
    for u in transpose[v]:
        if u not in visited:
            dfs2(u, component)
sccs = []

while stack:
    node = stack.pop()
    if node not in visited:
        component = []
        dfs2(node, component)
        sccs.append(sorted(component))
print("Strongly Connected Components:")
for comp in sccs:
    print("{" + ", ".join(map(str, comp)) + "}")
with open("scc_output.txt", "w") as f:
    f.write("Strongly Connected Components:\n")
    for comp in sccs:
        f.write("{" + ", ".join(map(str, comp)) + "}\n")
