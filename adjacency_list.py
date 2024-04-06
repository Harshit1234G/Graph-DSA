type Edge = tuple[int, int]


class Graph:
    def __init__(
        self,
        number_of_nodes: int,
        edges: list[Edge]
    ) -> None:
        self.number_of_nodes = number_of_nodes
        self.data = [[] for _ in range(number_of_nodes)]

        for edge in edges:
            self.add_edge(edge)

    def add_edge(self, edge: Edge) -> None:
        n1, n2 = edge
        self.data[n1].append(n2)
        self.data[n2].append(n1)

    def remove_edge(self, edge: Edge) -> None:
        n1, n2 = edge
        self.data[n1].remove(n2)
        self.data[n2].remove(n1)

    def __str__(self) -> str:
        return '\n'.join(f'{node}: {neighbours}' for node, neighbours in enumerate(self.data))


if __name__ == '__main__':
    graph = Graph(5, [(0, 1), (0, 4), (1, 4), (1, 3), (1, 2), (3, 2), (4, 3)])
    print(graph)
    graph.add_edge((0, 3))
    graph.add_edge((2, 0))
    graph.add_edge((4, 2))
    print(graph)
    graph.remove_edge((0, 3))
    print(graph)
