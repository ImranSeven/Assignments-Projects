import heapq

class TreeMap:

    def __init__(self, roads, solulus):
        """
        Function description:
        Initializes a TreeMap object representing the forest with roads and Solulu trees.

        :Input:
        roads: List of tuples (u, v, w) that represent roads, where u is the starting tree ID and v is 
               the ending ending tree ID with time taken w.

        solulus: List of tuples (x, y, z) representing Solulu trees where x is the tree ID where the tree is a Solulu tree,
                 y is the time required to claw and destroy the Solulu tree, and z is the tree ID to which you will be teleported to

        :Output, return or postcondition:
        None

        Complexities: 
        For all further complexities analysis below;

        |T| is the number of unique trees;
        |R| is the number of roads.

        :Time complexity:
        O(|T| + |R|)

        :Time complexity analysis:
        The method constructs the adjacency list, which takes O(|T| + |R|) time

        :Space complexity:
        O(|T| + |R|)

        :Space complexity analysis:
        The method constructs the adjacency list, which uses O(|T| + |R|) space.
        """

        # Initialize roads and solulus
        self.roads = roads
        self.solulus = solulus
        self.exit = []

        # Determine the number of trees, multiplied by 2 to account for the duplicated graph
        self.num_trees = ((max(max(road[0], road[1]) for road in roads) + 1) * 2)
        
        # Determine the length in the duplicated graph
        self.duplicated_length = self.num_trees // 2

        # Build the adjacency list
        self.adjacency_list = self._build_adjacency_list()

        # Connecting original graph to duplicated graph
        for x, y, z in self.solulus:
            self.adjacency_list[x].append((z + self.duplicated_length, y))

    def _build_adjacency_list(self):
        """
        Function description:
        Constructs the adjacency list for the forest graph.

        :Input:
        None

        :Output, return or postcondition:
        Adjacency list representing the forest graph.

        :Time complexity:
        O(|T| + |R|)

        :Time complexity analysis:
        The method iterates through the roads and builds the adjacency list, which takes O(|T| + |R|) time.

        :Space complexity:
        O(|T| + |R|)

        :Space complexity analysis:
        The method constructs the adjacency list, which uses O(|T| + |R|) space.
        """
         
        # Initialize empty adjacency list for each tree
        adjacency_list = [[] for _ in range(self.num_trees)]

        # Add directed roads to the adjacency list
        for u, v, w in self.roads:
            adjacency_list[u].append((v, w))

            # Add a duplicate graph
            adjacency_list[u + self.duplicated_length].append((v + self.duplicated_length, w))
        
        return adjacency_list

    def escape(self, start, exits): # Main Function
        """
        Function description:
        Determines the quickest path whilst taking into account the requirement to destroy a Solulu tree, 
        from the start tree to one of the exit trees.

        Approach description: 
        Firstly, I represent the forest, consisting of trees and roads between them, as a graph. I then construct an adjacency list to represent the graph. 
        Additionally, I also created a duplicated graph to account for the requirement of destroying a Solulu tree. When constructing the adjacency list, 
        connections are established between Solulu trees and their teleportation destinations in the duplicated graph. After that, I used Dijkstra's algorithm 
        to find the shortest path from the starting tree to each tree in the forest. The algorithm uses a priority queue to explore neighboring trees based on 
        their distances from the starting tree. This is done to identify the shortest paths. Once the shortest path to one of the exit trees is determined, 
        the method reconstructs this path using the predecessor list in the Dijkstra's algorithm. This reconstructed path includes the necessary steps to 
        destroy a Solulu tree, ensuring that the forest's seal is broken and the exit can be reached.

        :Input:
        start: Starting tree ID.
        exits: Exit tree IDs.

        :Output, return or postcondition:
        Tuple containing total time taken to exit the forest and the route taken as a list of tree IDs.

        :Time complexity:
        O(|R| log |T|)

        :Time complexity analysis:
        The method implements Dijkstra's algorithm using a priority queue, which takes O(|R| log |T|) time.

        :Space complexity:
        O(|T| + |R|)

        :Space complexity analysis:
        The method uses a priority queue and additional lists to store distances and predecessors, which uses O(|T| + |R|) space.
        """

        # Initialize priority queue with the starting tree
        priority_queue = []
        heapq.heappush(priority_queue, (0, start))

        # Initialize distances and predecessors arrays
        distance = [float('inf')] * self.num_trees
        distance[start] = 0
        predecessor = [None] * self.num_trees
        
        # Run Dijkstra's algorithm
        while priority_queue:
            _, u = heapq.heappop(priority_queue)

            # Iterate through neighbors of current tree
            for v, time_taken in self.adjacency_list[u]:

                # Relax edges if shorter path found
                if distance[v] > distance[u] + time_taken:    
                    distance[v] = distance[u] + time_taken
                    predecessor[v] = u

                    # Push updated distance to priority queue
                    heapq.heappush(priority_queue, (distance[v], v))    

        # Find the exit tree with the shortest distance
        min_dist = distance[exits[0] + self.duplicated_length]
        min_tree = self.duplicated_length + exits[0]

        for v in exits:
            if distance[v + self.duplicated_length] < min_dist:
                min_dist = distance[v + self.duplicated_length]
                min_tree = self.duplicated_length + v

        # If no path found, return None
        if min_dist == float('inf'):
            return None

        # Once shortest exit is found, call find path to get path as list
        path = self.find_path(min_tree, predecessor)
        return (min_dist, path)


    def find_path(self, exit, predecessor):
        """
        Function description:
        Reconstructs the path from the exit tree to the starting tree using the predecessor list generated during Dijkstra's algorithm.

        :Input:
        exit: Exit tree ID.
        predecessor: List of predecessors generated during Dijkstra's algorithm.

        :Output, return or postcondition:
        List of tree IDs representing the path from the exit tree to the starting tree.

        :Time complexity:
        O(|T|)

        :Time complexity analysis:
        The method iterates through the predecessors list to reconstruct the path, which takes O(|T|) time.

        :Space complexity:
        O(|T|)

        :Space complexity analysis:
        The method constructs the path list, which uses O(|T|) space.
        """ 

        path = []
        current_tree = exit
        prev_node = None  # Keep track of the previous node to compare with the current one

        # Reconstruct the path by backtracking from the exit node to the start node
        while current_tree is not None:

            # If the current node is not a duplicate or is different from the previous one, add it to the path
            if current_tree != prev_node:
                if current_tree >= self.duplicated_length:
                    path.append(current_tree - self.duplicated_length)  # Subtract duplicated length to get the original tree ID
                    prev_node = current_tree - self.duplicated_length   # Update the previous node
                else:
                    path.append(current_tree)
                    prev_node = current_tree    # Update the previous node
            current_tree = predecessor[current_tree]    # Move to the previous node in the path
        
        # Reverse the path to get the correct order
        return path[::-1]