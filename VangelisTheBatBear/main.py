from collections import defaultdict


class Graph:

    def __init__(self, verti):
        self.V = verti
        self.graph = defaultdict(list)

    def addEdge(self, v, w):
        self.graph[v].append(w)
        self.graph[w].append(v)

    def isCyclicUtil(self, v, visited, parent):

        visited[v] = True
        for j in self.graph[v]:
            if not visited[j]:
                if self.isCyclicUtil(j, visited, v):
                    return True
            elif parent != j:
                return True

        return False

    def isCyclic(self):
        visited = [False] * self.V
        for t in range(self.V):
            if not visited[t]:
                if self.isCyclicUtil(t, visited, -1):
                    return True
        return False


def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield number


input_parser = parser()


def get_word():
    global input_parser
    return next(input_parser)


def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)


if __name__ == '__main__':
    tests = get_number()
    for k in range(0, tests):
        n_vertices = get_number()
        m_edges = get_number()
        g = Graph(n_vertices)
        for i in range(0, m_edges):
            first_vertex = get_number()
            second_vertex = get_number()
            g.addEdge(first_vertex, second_vertex)
        if g.isCyclic():
            print(1)
        else:
            print(0)
