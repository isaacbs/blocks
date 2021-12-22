from collections import defaultdict
from collections import deque

def create_adj_matrix(map):
    adj_matrix = [[0 for j in range(map.numCols*map.numRows)] for i in range(map.numCols*map.numRows)]
    for x1 in range(map.numCols):
        for y1 in range(map.numRows):
            neighbors = map.get_no_wall_neighbors(map.map[x1][y1])
            adj_matrix[y1*map.numCols+x1][y1*map.numCols+x1] = 1
            for neighbor in neighbors:
                x2 = neighbor.x
                y2 = neighbor.y
                adj_matrix[y1*map.numCols+x1][y2*map.numCols+x2] = 1
                adj_matrix[y2*map.numCols+x2][y1*map.numCols+x1] = 1

    return adj_matrix

def print_adj(matrix):
    for row in matrix:
        print(row)
    
def print_list(aList):
    for i in aList:
        print(i, end ="")
        for j in aList[i]:
            print(" -> {}".format(j), end ="")
        print()

def convert(matrix):
    adjList = defaultdict(list)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
                    if matrix[i][j]== 1:
                        adjList[i].append(j)
    return adjList

def write_path(map, path):
    for i in path:
        y,x = divmod(i, map.numCols)
        map.map[x][y].insolution = True

def bfs_shortest_path(graph, start, goal):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = deque()
    queue.append([start])

    # return path if start is goal
    if start == goal:
        return "That was easy! Start = goal"

    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.popleft()
        # get the last node from the path
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # return path if neighbour is goal
                if neighbour == goal:
                    return new_path

            # mark node as explored
            explored.append(node)

    # in case there's no path between the 2 nodes 
    return "So sorry, but a connecting path doesn't exist :("


def dfs_shortest_path(graph, start, goal):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = deque()
    queue.append([start])

    # return path if start is goal
    if start == goal:
        return "That was easy! Start = goal"

    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop()
        # get the last node from the path
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # return path if neighbour is goal
                if neighbour == goal:
                    return new_path

            # mark node as explored
            explored.append(node)

    # in case there's no path between the 2 nodes 
    return "So sorry, but a connecting path doesn't exist :("

def manhattan(map, point, goal):
    x1, y1 = divmod(point, map.numCols)
    x2, y2 = divmod(goal, map.numCols)
    return x2-x1 + y2-y1



def a_star_algorithm(map, graph, start, stop):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_list = set([start])
        closed_list = set([])

        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {}

        g[start] = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start] = start

        while len(open_list) > 0:
            n = None

            # find a node with the lowest value of f() - evaluation function
            for v in open_list:
                if n == None or g[v] + manhattan(map, v, stop) < g[n] + manhattan(map, n, stop):
                    n = v;

            if n == None:
                print('Path does not exist!')
                return None

            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if n == stop:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start)

                reconst_path.reverse()

                # print('Path found: {}'.format(reconst_path))
                return reconst_path

            # for all neighbors of the current node do
            for m in graph[n]:
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + 1

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + 1:
                        g[m] = g[n] + 1
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None