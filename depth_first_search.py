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

    def depth_first_search(self, root: int) -> list[int]:
        """
        Performs a Depth-First Search (DFS) on the graph starting from a given root node.

        Parameters:
            root (int): The index of the node to start the DFS from.

        Returns:
            - queue (list[int]): The order in which nodes were explored during the DFS.
        """
        # Create a stack to keep track of nodes to be explored
        stack = []

        # Initialize a discovered list to mark visited nodes (False means not visited)
        discovered = [False] * len(self.data)

        # Push the root node onto the stack to begin exploration
        stack.append(root)

        # List to store the explored nodes in the DFS order
        result = []

        # Loop as long as there are nodes to explore in the stack
        while len(stack) > 0:

            # Pop the current node from the stack
            current = stack.pop()

            # Check if the current node is not yet discovered (visited)
            if not discovered[current]:
                # Mark the current node as discovered
                discovered[current] = True

                # Add the current node to the result list (exploration order)
                result.append(current)

                # Loop through the neighbors of the current node
                for node in self.data[current]:
                    # If a neighbor is not yet discovered, push it onto the stack for further exploration
                    if not discovered[node]:
                        stack.append(node)

        # Return the list of explored nodes in the DFS order
        return result

if __name__ == '__main__':
    g1 = Graph(5, [(0, 1), (0, 4), (1, 4), (1, 3), (1, 2), (3, 2), (4, 3)])
    print(g1.depth_first_search(3))
