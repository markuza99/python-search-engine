class Graph:

    def __init__(self):
        self._graph_dict = {}

    def incident_edges(self, v):
        if v not in self._graph_dict:
            raise Exception('Vertex not found')

        for key in self._graph_dict:
            if v in self._graph_dict[key]:
                yield key

    def add_edge(self, u, v):
        if u not in self._graph_dict:
            self._graph_dict[u] = []

        if v in self._graph_dict[u]:
            return

        self._graph_dict[u].append(v)

    def add_vertex(self, vertex):
        if vertex in self._graph_dict:
            pass
        else:
            self._graph_dict[vertex] = []