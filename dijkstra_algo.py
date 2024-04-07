type Edge = tuple[int, int, int]


class WeightedGraph:
    def __init__(
        self,
        number_of_nodes: int,
        edges: list[Edge],
        *,
        directed: bool = False
    ) -> None:
        self.number_of_nodes = number_of_nodes
        self.__directed = directed
        self.adjacency_matrix = [[0] * number_of_nodes for _ in range(number_of_nodes)]

        for edge in edges:
            self.add_edge(edge)

    def add_edge(self, edge: Edge) -> None:
        n1, n2, weight = edge

        if n1 < 0 or n1 >= self.number_of_nodes or n2 < 0 or n2 >= self.number_of_nodes:
            raise ValueError("Invalid node number.")
        
        self.adjacency_matrix[n1][n2] = weight

        if not self.__directed:
            self.adjacency_matrix[n2][n1] = weight

    def shortest_path(self, source: int, target: int) -> ...:
       ...
    
    def __str__(self) -> str:
        header = '\t' + '\t'.join(str(i) for i in range(self.number_of_nodes)) + '\n\n'
        values = ['\t'.join(str(i) for i in j) for j in self.adjacency_matrix]
        result = header + '\n'.join(f'{index}\t{value}' for index, value in enumerate(values))
        return result
    

if __name__ == '__main__':
    g1 = WeightedGraph(6, [(0, 1, 4), (0, 2, 2), (1, 2, 5), (1, 3, 10), (2, 4, 3), (4, 3, 4), (3, 5, 11)], directed= True)
    print(g1)

    g2 = WeightedGraph(6, [(1, 2, 7), (2, 4, 15), (1, 3, 9), (3, 2, 10), (3, 4, 11), (5, 4, 6), (0, 5, 9), (0, 3, 2), (1, 0, 14)])
    print(g2)

    print(g1.shortest_path(0, 5))