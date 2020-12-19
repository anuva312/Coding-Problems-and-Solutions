class Graph:
    def __init__(self,n):
        self.adj_list = {}
        self.visited = {}
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
        # Exploring the graph in depth first order
        self.visited[x] = 1
        for node in self.adj_list[x]:
            if not self.visited[node]:
                self.reach(node)

    def dfs(self):
        # Initializing no.of connected components to 0
        cc=0
        for node in self.adj_list.keys():
            if not self.visited[node]:
                self.reach(node)
                cc+=1
        return cc


if __name__ == '__main__':
    # Taking input : no.of vertices, edges
    n, m = map(int, input().split())
    maze = Graph(n)
    maze.initialize_adj_list(m)
    print(maze.dfs())

