# Definition for a graph node (adjacency list representation).
class GraphNode:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self):
        return f'GraphNode({self.val})'


def buildGraph(edges, directed=False):
    """
    Build a graph from a list of [u, v] edges.
    Returns a dict mapping val -> GraphNode.

    Example:
        edges = [[1,2],[1,3],[2,4]]
        graph = buildGraph(edges)  # undirected by default
    """
    graph = {}

    for u, v in edges:
        if u not in graph:
            graph[u] = GraphNode(u)
        if v not in graph:
            graph[v] = GraphNode(v)
        graph[u].neighbors.append(graph[v])
        if not directed:
            graph[v].neighbors.append(graph[u])

    return graph


def buildGraphFromAdjList(adj_list):
    """
    Build a graph from an adjacency list (list of lists).
    Index i represents node i's neighbors.

    Example:
        adj_list = [[1,2],[0,3],[0,3],[1,2]]
        graph = buildGraphFromAdjList(adj_list)
    """
    nodes = [GraphNode(i) for i in range(len(adj_list))]
    for i, neighbors in enumerate(adj_list):
        nodes[i].neighbors = [nodes[n] for n in neighbors]
    return nodes


def displayGraph(graph):
    """
    Display adjacency list for a graph dict (val -> GraphNode).
    """
    for val, node in sorted(graph.items()):
        neighbors = ', '.join(str(n.val) for n in node.neighbors)
        print(f'{val}: [{neighbors}]')
