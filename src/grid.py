import random
import math

from cell import Cell
from dataclasses import dataclass
import dataclasses as dc
from collections import defaultdict
from collections import deque
import matplotlib
from matplotlib import colors as c
import matplotlib.pyplot as plt

class Grid:
    """A grid of cells used to make up the maze"""
    def __init__(self, numCols, numRows):
        self.numCols = numCols
        self.numRows = numRows
    # map: list[Cell] = dc.field(default_factory=list)
        map = [[Cell(i, j) for j in range(numRows)] for i in range(numCols)]

    def create_grid(self):
        self.map = [[Cell(i, j) for j in range(self.numRows)] for i in range(self.numCols)]
    
    def get_cell(self, x, y):
        return self.map[x][y]

    def print_maze(self, num):
        rows = ['+-' * (self.numCols) + "+"]
        for r in range(self.numRows):
            row = ['|']
            for col in range(self.numCols):
                if col == self.numCols-1:
                    if self.map[col][r].insolution:
                        if self.map[col][r].walls['E']:
                            row.append('*|')
                        else:
                            row.append('* ')
                    else:
                        if self.map[col][r].walls['E']:
                            row.append(' |')
                        else:
                            row.append('  ')
                else:
                    if self.map[col][r].insolution and self.map[col+1][r].insolution:
                        if self.map[col][r].walls['E']:
                            row.append('*|')
                        else:
                            row.append('**')
                    elif self.map[col][r].insolution:
                        if self.map[col][r].walls['E']:
                            row.append('*|')
                        else:
                            row.append('* ')
                    else:
                        if self.map[col][r].walls['E']:
                            row.append(' |')
                        else:
                            row.append('  ')
            rows.append(''.join(row))
            row = ['+']
            for col in range(self.numCols):
                if r == self.numRows-1:
                    if self.map[col][r].insolution:
                        if self.map[col][r].walls['S']:
                            row.append('-+')
                        else:
                            row.append(' +')
                    else:
                        if self.map[col][r].walls['S']:
                            row.append('-+')
                        else:
                            row.append(' +')
                else:
                    if self.map[col][r].insolution and self.map[col][r+1].insolution:
                        if self.map[col][r].walls['S']:
                            row.append('-+')
                        else:
                            row.append('*+')
                    elif self.map[col][r].insolution:
                        if self.map[col][r].walls['S']:
                            row.append('-+')
                        else:
                            row.append(' +')
                    else:
                        if self.map[col][r].walls['S']:
                            row.append('-+')
                        else:
                            row.append(' +')
            rows.append(''.join(row))
        maze_file = open("text/maze" + str(num) + ".txt", "w")
        maze_file.write('\n'.join(rows))
        maze_file.close()
        return '\n'.join(rows)




    def plot(self, number):
        maze = []
        with open("text/maze" + str(number) + ".txt", 'r') as file:
            for line in file:
                line = line.rstrip()
                row = []
                for c in line:
                    if c == ' ':
                        row.append(1) # spaces are 1s
                    elif c == '*':
                        row.append(2)
                    else:
                        row.append(0) # walls are 0s
                maze.append(row)



        
        plt.axes().set_aspect('equal') #set the x and y axes to the same scale
        # plt.axes().invert_yaxis() #invert the y-axis so the first row of data is at the top


        colors = ['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 
        'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r',
         'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 
         'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 
         'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r']


        c1 = random.choice(colors)
        c2 = random.choice(colors)

        cMap = c1
        plt.pcolormesh(maze, cmap=cMap)
        plt.axis('off')
        plt.xticks([]) # remove the tick marks by setting to an empty list
        plt.yticks([]) # remove the tick marks by setting to an empty list
        fname = 'output/maze' + str(number) + '.png'
        plt.savefig(fname, dpi=300, bbox_inches='tight',pad_inches=0, edgecolor='auto')

        plt.clf()
        return

    def get_neighbors(self, cell):
        directions = [('W', (-1, 0)), ('E', (1, 0)), ('S', (0, 1)), ('N', (0, -1))]
        neighbors = []
        for dir, (changeX, changeY) in directions:
            tempX = cell.x + changeX
            tempY = cell.y + changeY
            if ((0 <= tempX < self.numCols) and (0 <= tempY < self.numRows)):
                n = self.get_cell(tempX, tempY)
                if n.walls_exist():
                    neighbors.append((dir, n))
        return neighbors

    def get_no_wall_neighbors(self, cell):
        neighbors = []
        if not cell.walls['E'] and (0 <= cell.x+1 < self.numCols):
            neighbors.append(self.map[cell.x+1][cell.y])

        if not cell.walls['W'] and (0 <= cell.x-1 < self.numCols):
            neighbors.append(self.map[cell.x-1][cell.y])

        if not cell.walls['S'] and (0 <= cell.y+1 < self.numRows):
            neighbors.append(self.map[cell.x][cell.y+1])

        if not cell.walls['N'] and (0 <= cell.y-1 < self.numRows):
            neighbors.append(self.map[cell.x][cell.y-1])

        return neighbors
        

    def create_adj_matrix(self):
        adj_matrix = [[0 for j in range(self.numCols*self.numRows)] for i in range(self.numCols*self.numRows)]
        for x1 in range(self.numCols):
            for y1 in range(self.numRows):
                neighbors = self.get_no_wall_neighbors(self.map[x1][y1])
                adj_matrix[y1*self.numCols+x1][y1*self.numCols+x1] = 1
                for neighbor in neighbors:
                    x2 = neighbor.x
                    y2 = neighbor.y
                    adj_matrix[y1*self.numCols+x1][y2*self.numCols+x2] = 1
                    adj_matrix[y2*self.numCols+x2][y1*self.numCols+x1] = 1

        return adj_matrix

    def print_adj(self, matrix):
        for row in matrix:
            print(row)
        
    def print_list(self, aList):
        for i in aList:
            print(i, end ="")
            for j in aList[i]:
                print(" -> {}".format(j), end ="")
            print()

    def convert(self, matrix):
        adjList = defaultdict(list)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                        if matrix[i][j]== 1:
                            adjList[i].append(j)
        return adjList

    def write_path(self, path):
        for i in path:
            y,x = divmod(i, self.numCols)
            self.map[x][y].insolution = True

    def depth_first(self):
        num_cells = self.numCols*self.numRows
        c_stack = []
        cur = self.get_cell(0,0)
        cells_visited = 1

        while cells_visited < num_cells:
            neighbors = self.get_neighbors(cur)

            if not neighbors:
                cur = c_stack.pop()
                continue

            dir, nCell = random.choice(neighbors)
            cur.destroy_wall(nCell, dir)
            c_stack.append(cur)
            cur = nCell
            cells_visited += 1

    def binary(self):
        for y in range(self.numRows):
            for x in range(self.numCols):
                neighbors = []
                if x > 0:
                    neighbors.append(('W', self.map[x-1][y]))
                if y > 0:
                    neighbors.append(('N', self.map[x][y-1]))
                if not neighbors:
                    continue
                dir, cell = random.choice(neighbors)
                self.map[x][y].destroy_wall(cell, dir)

    def sidewinder(self):
        for y in range(self.numRows):
            run = 0
            for x in range(self.numCols):
                roll = [True, False, False]
                if y > 0 and (x+1 == self.numCols or not random.choice(roll)):
                    t = run + random.randint(0, x - run)
                    self.map[t][y].destroy_wall(self.map[t][y-1], 'N')
                    run = x + 1
                elif x+1 < self.numCols:
                    self.map[x][y].destroy_wall(self.map[x+1][y], 'E')

    def kruskals(self):
        edges = []
        sets = []
        for y in range(self.numRows):
            for x in range(self.numCols):
                neighbors = self.get_neighbors(self.map[x][y])
                sets.append({self.map[x][y]})
                for dir, neighbor in neighbors:
                    edges.append((self.map[neighbor.x][neighbor.y], dir))
        while edges:
            curEdge, dir = random.choice(edges)
            if dir == 'W':
                s1 = 0
                s2 = 0
                for i in range(len(sets)):
                    if self.map[curEdge.x+1][curEdge.y] in sets[i]:
                        s1 = i
                    if self.map[curEdge.x][curEdge.y] in sets[i]:
                        s2 = i
                if s1 != s2:
                    s3 = sets[s1].union(sets[s2])
                    if s1 < s2:
                        sets.remove(sets[s1])
                        sets.remove(sets[s2-1])
                    else:
                        sets.remove(sets[s1])
                        sets.remove(sets[s2])
                    sets.append(s3)
                    self.map[curEdge.x+1][curEdge.y].destroy_wall(self.map[curEdge.x][curEdge.y], 'W')

            elif dir == 'E':
                s1 = 0
                s2 = 0
                for i in range(len(sets)):
                    if self.map[curEdge.x-1][curEdge.y] in sets[i]:
                        s1 = i
                    if self.map[curEdge.x][curEdge.y] in sets[i]:
                        s2 = i
                if s1 != s2:
                    s3 = sets[s1].union(sets[s2])
                    if s1 < s2:
                        sets.remove(sets[s1])
                        sets.remove(sets[s2-1])
                    else:
                        sets.remove(sets[s1])
                        sets.remove(sets[s2])
                    sets.append(s3)
                    self.map[curEdge.x-1][curEdge.y].destroy_wall(self.map[curEdge.x][curEdge.y], 'E')

            elif dir == 'S':
                s1 = 0
                s2 = 0
                for i in range(len(sets)):
                    if self.map[curEdge.x][curEdge.y-1] in sets[i]:
                        s1 = i
                    if self.map[curEdge.x][curEdge.y] in sets[i]:
                        s2 = i
                if s1 != s2:
                    s3 = sets[s1].union(sets[s2])
                    if s1 < s2:
                        sets.remove(sets[s1])
                        sets.remove(sets[s2-1])
                    else:
                        sets.remove(sets[s1])
                        sets.remove(sets[s2])
                    sets.append(s3)
                    self.map[curEdge.x][curEdge.y-1].destroy_wall(self.map[curEdge.x][curEdge.y], 'S')

            elif dir == 'N':
                s1 = 0
                s2 = 0
                for i in range(len(sets)):
                    if self.map[curEdge.x][curEdge.y+1] in sets[i]:
                        s1 = i
                    if self.map[curEdge.x][curEdge.y] in sets[i]:
                        s2 = i
                if s1 != s2:
                    s3 = sets[s1].union(sets[s2])
                    if s1 < s2:
                        sets.remove(sets[s1])
                        sets.remove(sets[s2-1])
                    else:
                        sets.remove(sets[s1])
                        sets.remove(sets[s2])
                    sets.append(s3)
                    self.map[curEdge.x][curEdge.y+1].destroy_wall(self.map[curEdge.x][curEdge.y], 'N')

            edges.remove((curEdge, dir))
    
    def bfs_shortest_path(self, graph, start, goal):
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
    

    def dfs_shortest_path(self, graph, start, goal):
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

    def manhattan(self, point, goal):
        x1, y1 = divmod(point, self.numCols)
        x2, y2 = divmod(goal, self.numCols)
        return x2-x1 + y2-y1

    def a_star(self, graph, start, goal):
        # This contains the distances from the start node to all other nodes, initialized with a distance of "Infinity"
        distances = [float("inf")] *len(graph[0])

        # The distance from the start node to itself is of course 0
        distances[start] = 0

        # This contains the priorities with which to visit the nodes, calculated using the heuristic.
        priorities = [float("inf")] * len(graph)

        # start node has a priority equal to straight line distance to goal. It will be the first to be expanded.
        priorities[start] = self.manhattan(start, goal)

        # This contains whether a node was already visited
        visited = [False] * len(graph)

        # While there are nodes left to visit...
        while True:
            # ... find the node with the currently lowest priority...
            lowest_priority = float("inf")
            lowest_priority_index = -1
            for i in range(len(priorities)):
                # ... by going through all nodes that haven't been visited yet
                if priorities[i] < lowest_priority and not visited[i]:
                    lowest_priority = priorities[i]
                    lowest_priority_index = i
                    # print(i)
                    # print('priority')
                    # print(priorities[i])
                    # print('\n')

            if lowest_priority_index == -1:
                # There was no node not yet visited --> Node not found
                return -1

            elif lowest_priority_index == goal:
                '''Uncomment for printing path'''
                path = [0 for i in range(distances[lowest_priority_index]+1)]
                for i in range(len(distances)):
                    for j in range(len(distances)):
                        if j == distances[i] and distances[i] != 'inf':
                            path[j] = i
                print(path)
                return distances[lowest_priority_index]

            # print("Visiting node " + lowestPriorityIndex + " with currently lowest priority of " + lowestPriority)

            # ...then, for all neighboring nodes that haven't been visited yet....
            for i in range(len(graph[lowest_priority_index])):
                if graph[lowest_priority_index][i] != 0 and not visited[i]:
                    # ...if the path over this edge is shorter...
                    if distances[lowest_priority_index] + graph[lowest_priority_index][i] < distances[i]:
                        # ...save this path as new shortest path
                        distances[i] = distances[lowest_priority_index] + graph[lowest_priority_index][i]

                        priorities[i] = distances[i] + self.manhattan(i, goal)
                        # print("Updating distance of node " + i + " to " + distances[i] + " and priority to " + priorities[i])

                    # Lastly, note that we are finished with this node.
                    visited[lowest_priority_index] = True
                    # print("Visited nodes: " + visited)
                    # print("Currently lowest distances: " + distances)


    def a_star_algorithm(self, graph, start, stop):
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
                    if n == None or g[v] + self.manhattan(v, stop) < g[n] + self.manhattan(n, stop):
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