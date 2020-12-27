# Find the topological list ordering of the graph

class Graph:
    def __init__(self,n):
        self.adj_list = {}
        self.visited = {}
        self.topological_list = []
        self.size = n + 1
        # Initializing adjacency list of each vertex into an empty list
        for i in range(1,n+1):
            self.visited[i] = 0
            self.adj_list[i] = []

    def initialize_adj_list(self, m):
        # Filling the adjacency list
        for _ in range(m):
            a,b = map(int, input().split())
            self.adj_list[a].append(b)

    def explore(self,x):
        # Exploring the graph in depth first order
        self.visited[x] = 1
        try:
            for node in self.adj_list[x]:
                if not self.visited[node]:
                    self.explore(node)
            if not self.adj_list[x]:
                self.topological_list.append(x)
                self.remove_element(x)
        except KeyError:
            pass

    def dfs(self):
        for node in range(1,self.size):
            if not self.visited[node]:
                self.explore(node)
        for node in range(1,self.size):
            if node not in self.topological_list:
                self.topological_list.append(node)

    def remove_element(self,x):
        # removes element from adjacency list (both as values and key)
        self.adj_list.pop(x)
        for ele in self.adj_list.keys():
            try:
                self.adj_list[ele].remove(x)
            except ValueError:
                pass
        


if __name__ == '__main__':
    # Taking input : no.of vertices, edges
    n, m = map(int, input().split())
    graph = Graph(n)
    graph.initialize_adj_list(m)
    (graph.dfs())
    print(*graph.topological_list[::-1])

