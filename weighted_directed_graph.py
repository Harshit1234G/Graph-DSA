type Edge = tuple[int, int] | tuple[int, int, int]


class Graph:
    def __init__(
        self,
        number_of_nodes: int,
        edges: list[Edge],
        *,
        weighted: bool = False,
        directed: bool = False
    ) -> None:
        self.number_of_nodes = number_of_nodes
        self.__directed = directed
        self.__weighted = weighted
        self.data = [[] for _ in range(number_of_nodes)]

        for edge in edges:
            self.add_edge(edge)

    def add_edge(self, edge: Edge) -> None:
        if self.__weighted and self.__directed:
            n1, n2, weight = edge
            self.data[n1].append((n2, weight))

        elif self.__weighted:
            n1, n2, weight = edge
            self.data[n1].append((n2, weight))
            self.data[n2].append((n1, weight))

        elif self.__directed:
            n1, n2 = edge
            self.data[n1].append(n2)

        else:
            n1, n2 = edge
            self.data[n1].append(n2)
            self.data[n2].append(n1)

    def __str__(self) -> str:
        return '\n'.join(f'{node}: {neighbours}' for node, neighbours in enumerate(self.data))


if __name__ == '__main__':
    g1 = Graph(5, [(0, 1), (0, 4), (1, 4), (1, 3), (1, 2), (3, 2), (4, 3)])
    print(g1)
    g2 = Graph(5, [(0, 1), (1, 2), (2, 4), (4, 2), (3, 0), (2, 3)], directed= True)
    print(g2)
    g3 = Graph(6, [(0, 1, 4), (0, 2, 2), (1, 2, 5), (1, 3, 10), (2, 4, 3), (4, 3, 4), (3, 5, 11)], weighted= True)
    print(g3)
    g4 = Graph(6, [(0, 1, 4), (0, 2, 2), (1, 2, 5), (1, 3, 10), (2, 4, 3), (4, 3, 4), (3, 5, 11)], weighted= True, directed= True)
    print(g4)
