type Edge = tuple[int, int]


class Graph:
    def __init__(
        self,
        number_of_nodes: int,
        edges: list[Edge]
    ) -> None:
        self.number_of_nodes = number_of_nodes
        self.adjacency_matrix = [[0] * number_of_nodes for _ in range(number_of_nodes)]

        for edge in edges:
            self.add_edge(edge)

    def add_edge(self, edge: Edge) -> None:
        n1, n2 = edge
        self.adjacency_matrix[n1][n2] = 1
        self.adjacency_matrix[n2][n1] = 1

    def remove_edge(self, edge: Edge) -> None:
        n1, n2 = edge
        self.adjacency_matrix[n1][n2] = 0
        self.adjacency_matrix[n2][n1] = 0

    def __str__(self) -> str:
        header = '\t' + '\t'.join(str(i) for i in range(self.number_of_nodes)) + '\n\n'
        values = ['\t'.join(str(i) for i in j) for j in self.adjacency_matrix]
        result = header + '\n'.join(f'{index}\t{value}' for index, value in enumerate(values))
        return result


if __name__ == '__main__':
    g1 = Graph(5, [(0, 1), (0, 4), (1, 4), (1, 3), (1, 2), (3, 2), (4, 3)])
    g1.add_edge((0, 3))
    g1.remove_edge((1, 0))
    print(g1)
