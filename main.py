__author__ = 'Arman Malekzade'
adj_list = [
    [[1, 4], [2, 3], [4, 7]],
    [[0, 4], [2, 6], [3, 5]],
    [[0, 3], [1, 6], [4, 8], [3, 11]],
    [[1, 5], [2, 11], [4, 2], [6, 10], [5, 2]],
    [[2, 8], [3, 2], [6, 5]],
    [[3, 2], [6, 3]],
    [[3, 10], [4, 5], [5, 3]]
]


class Graph:

    def __init__(self, adj):
        self.adj_list = adj

    def dijkstra(self, start, goal):
        visited = []
        values = []
        path = []
        for i in range(len(self.adj_list)):
            visited.append(False)
            values.append(1000)
        current = start
        values[current] = 0
        number_of_visited_nodes = 0
        path.append(start)
        print 'Starting at node ', start
        while (not current == goal) and number_of_visited_nodes < len(self.adj_list):
            visited[current] = True
            number_of_visited_nodes += 1
            current_neighbours = self.adj_list[current]
            selected_i = -1
            selected_v = 1000
            j = 0
            print 'Neighbours of ', current, 'are: ', current_neighbours
            for n in current_neighbours:
                print 'Exploring node', n[0], 'which is a neighbour of', current
                if not visited[n[0]]:
                    print n[0], 'was not visited before...'
                    values[n[0]] = min(values[n[0]], values[current] + n[1])
                    print 'The value of', n[0], 'becomes', values[n[0]]
                    if values[n[0]] < selected_v:
                        print 'This values is less than the previous selected value, which was', selected_v
                        selected_i = j
                        selected_v = values[n[0]]
                        print 'So, The new selected value is', selected_v, 'which belongs to node', self.adj_list[current][selected_i][0]
                j += 1
            for i in range(len(current_neighbours)):
                if not i == selected_i:
                    values[current_neighbours[i][0]] = 1000
            print 'The Selected neighbour is', self.adj_list[current][selected_i][0]
            current = self.adj_list[current][selected_i][0]
            path.append(current)
        return path

g = Graph(adj_list)
print g.dijkstra(0, 5)
