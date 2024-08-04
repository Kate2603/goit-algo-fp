import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, colors, labels):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    node_colors = [colors.get(node[0], '#ffffff') for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=node_colors)
    plt.show()

def generate_color(index, total):
    # Генерує кольори від темного до світлого
    r = int(255 * index / total)
    g = int(0)
    b = int(255 * (1 - index / total))
    return '#%02X%02X%02X' % (r, g, b)

def visualize_dfs(tree_root):
    stack = [tree_root]
    visited = set()
    colors = {}
    index = 0

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            colors[node.id] = generate_color(index, len(visited))
            index += 1
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    
    draw_tree(tree_root, colors, labels={node.id: node.val for node in visited})

def visualize_bfs(tree_root):
    queue = deque([tree_root])
    visited = set()
    colors = {}
    index = 0

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            colors[node.id] = generate_color(index, len(visited))
            index += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    draw_tree(tree_root, colors, labels={node.id: node.val for node in visited})

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення обходу в глибину
print("DFS Visualization:")
visualize_dfs(root)

# Відображення обходу в ширину
print("BFS Visualization:")
visualize_bfs(root)
