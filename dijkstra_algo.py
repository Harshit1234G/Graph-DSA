from typing import NoReturn


# Type Annotation
type Edge = tuple[int, int, int]


# Main class
class WeightedGraph:
    """
    # Weighted Graph
    Represents a weighted graph using an adjacency matrix.

    ## Attributes:
    - `number_of_nodes` (int): The number of nodes in the graph.
    - `__directed` (bool): Whether the graph is directed or undirected, default False.
    - `adjacency_matrix` (list[list[int]]): The adjacency matrix representing the graph.

    ## Functions:
    - `add_edge()`: For adding an edge to the graph.
    - `shortest_path()`: Gives the shortest path from `source` to `target` using Dijkstra's algorithm.
    """
    def __init__(
        self,
        number_of_nodes: int,
        edges: list[Edge],
        *,
        directed: bool = False
    ) -> None:
        self.number_of_nodes = number_of_nodes
        self.__directed = directed

        # initializing adjacency matrix
        self.adjacency_matrix = [[0] * number_of_nodes for _ in range(number_of_nodes)]

        # creating edges in adjacency matrix
        for edge in edges:
            self.add_edge(edge)

    def add_edge(self, edge: Edge) -> None | NoReturn:
        n1, n2, weight = edge

        # if n1 and n2 are out of range
        if n1 < 0 or n1 >= self.number_of_nodes or n2 < 0 or n2 >= self.number_of_nodes:
            raise ValueError("Invalid node number.")

        # adding edge, either directed or undirected
        self.adjacency_matrix[n1][n2] = weight

        if not self.__directed:
            self.adjacency_matrix[n2][n1] = weight

    def shortest_path(self, source: int, target: int) -> list[int] | NoReturn:
        """
        Finds the shortest path from a source node to a target node using Dijkstra's algorithm.

        Parameters:
        - `source` (int): The starting node index.
        - `target` (int): The destination node index.

        Returns:
        - list[int]: A list of nodes representing the shortest path from source to target, or an empty list if no path exists.

        Raises:
        - ValueError: If the source or destination node is outside the valid range.
        """
        # checking source and target are in range or not.
        if source < 0 or source >= self.number_of_nodes or target < 0 or target >= self.number_of_nodes:
            raise ValueError("Invalid node number.")
        
        # setting all distances to infinity
        distances = [float('inf')] * self.number_of_nodes
        # setting all previous nodes to -1
        previous = [-1] * self.number_of_nodes
        # setting distance of source to 0 (as distance from source to source must be 0)
        distances[source] = 0
        # visited nodes
        visited = set()

        while visited != set(range(self.number_of_nodes)):
            # finding the unvisited node with minimum tentative distance
            min_index = self.__find_min_index(distances, visited)
            
            if min_index == -1:    # No unvisited nodes left (all distances are infinity)
                break

            # mark min_index as visited
            visited.add(min_index)

            # finding the shortest path
            for neighbor in range(self.number_of_nodes):
                # check for existing edge
                if self.adjacency_matrix[min_index][neighbor] > 0 and neighbor not in visited:
                    # new tentative distance
                    new_dist = distances[min_index] + self.adjacency_matrix[min_index][neighbor]
                    # updating distance and previous if new distance is less
                    if new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        previous[neighbor] = min_index

        # reconstructing the path
        path = []
        while target != -1:
            path.append(target)
            target = previous[target]

        return path[::-1]

    def __find_min_index(self, distances: list[float], visited: set) -> int:
        min_dist = float('inf')
        min_index = -1

        for i in range(self.number_of_nodes):
            if i not in visited and distances[i] < min_dist:
                min_dist = distances[i]
                min_index = i

        return min_index

    def __str__(self) -> str:
        header = '\t' + '\t'.join(str(i) for i in range(self.number_of_nodes)) + '\n\n'
        values = ['\t'.join(str(i) for i in j) for j in self.adjacency_matrix]
        result = header + '\n'.join(f'{index}\t{value}' for index, value in enumerate(values))
        return result


if __name__ == '__main__':
    g1 = WeightedGraph(6, [(0, 1, 4), (0, 2, 2), (1, 2, 5), (1, 3, 10), (2, 4, 3), (4, 3, 4), (3, 5, 11)], directed=True)
    print(g1)
    print(g1.shortest_path(0, 5))

    g2 = WeightedGraph(6, [(1, 2, 7), (2, 4, 15), (1, 3, 9), (3, 2, 10), (3, 4, 11), (5, 4, 6), (0, 5, 9), (0, 3, 2), (1, 0, 14)])
    print(g2)
    print(g2.shortest_path(1, 5))
