class Graph:
    def __init__(self,n):
        self.adj_list = {}
        self.visited = {}
        self.dest = 0
        self.result = 0
        # Initializing adjacency list of each vertex into an empty list
        for i in range(1,n+1):
            self.visited[i] = 0
            self.adj_list[i] = []

    def initialize_adj_list(self, m):
        # Filling the adjacency list
        for _ in range(m):
            a,b = map(int, input().split())
            self.adj_list[a].append(b)
            self.adj_list[b].append(a)

    def reach(self, x):
        self.visited[x] = 1
        if self.dest in self.adj_list[x]:
            self.result = 1
            return
        # Depth First Search
        for node in self.adj_list[x]:
            if not self.visited[node]:
                self.reach(node)


if __name__ == '__main__':
    # Taking input : no.of vertices, edges
    n, m = map(int, input().split())
    maze = Graph(n)
    maze.initialize_adj_list(m)
    # Taking input: the nodes between which we are to find if a path exists
    src, maze.dest = map(int, input().split())
    maze.reach(src)
    print(maze.result)
