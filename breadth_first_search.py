type Edge = tuple[int, int]


class Graph:
    """
    This class represents a graph data structure.

    Attributes:
        number_of_nodes (int): The total number of nodes in the graph.
        data (list[list[int]]): An adjacency list representation of the graph.
    """

    def __init__(
        self,
        number_of_nodes: int,
        edges: list[Edge]
    ) -> None:
        self.number_of_nodes = number_of_nodes
        self.data = [[] for _ in range(number_of_nodes)]

        for n1, n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)

    def breadth_first_search(self, root: int) -> tuple[list[int], list[int], list[int]]:
        """
        Performs a Breadth-First Search (BFS) on the graph starting from a given root node.

        Parameters:
            root (int): The index of the node to start the BFS from.

        Returns:
            tuple[list[int], list[int], list[int]]: A tuple containing three elements:
                - queue (list[int]): The order in which nodes were explored during the BFS.
                - distance (list[int]): The distance of each node from the root node.
                - parent (list[int]): The parent node of each node in the search path.
        """
        queue = []
        graph_length = len(self.data)
        discovered = [False] * graph_length  # Keeps track of visited nodes
        # Stores distance from root for each node
        distance = [None] * graph_length
        # Records the parent node in the search path
        parent = [None] * graph_length

        # Mark the root node as discovered and initialize its distance
        discovered[root] = True
        queue.append(root)
        distance[root] = 0

        index = 0

        # BFS exploration loop - continues until all reachable nodes are explored
        while index < len(queue):
            # Dequeue the current node being explored
            current = queue[index]
            index += 1

            # Iterate through neighbors of the current node
            for node in self.data[current]:
                # If the neighbor hasn't been discovered yet
                if not discovered[node]:
                    # Update distance (one more than current node's distance)
                    distance[node] = 1 + distance[current]
                    # Set the current node as the parent of the neighbor in the search path
                    parent[node] = current
                    # Mark the neighbor as discovered to avoid revisiting
                    discovered[node] = True
                    # Enqueue the neighbor for further exploration in the next level
                    queue.append(node)

        # Return the BFS exploration results
        return queue, distance, parent


if __name__ == '__main__':
    g1 = Graph(5, [(0, 1), (0, 4), (1, 4), (1, 3), (1, 2), (3, 2), (4, 3)])
    print(g1.breadth_first_search(3))
