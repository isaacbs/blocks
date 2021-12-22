'''Maze generation algorithms to be called on a grid'''

import random

def depth_first(graph):
    cmap = graph.random_colors()
    j = 0
    graph.print_maze(2000+j)
    graph.plot(2000+j, cmap)
    j += 1
    num_cells = graph.numCols*graph.numRows
    c_stack = []
    cur = graph.get_cell(0,0)
    cells_visited = 1

    while cells_visited < num_cells:
        neighbors = graph.get_neighbors(cur)

        if not neighbors:
            cur = c_stack.pop()
            continue

        dir, nCell = random.choice(neighbors)
        cur.destroy_wall(nCell, dir)
        nCell.visited = True
        cur.visited = True
        c_stack.append(cur)
        graph.print_maze(2000+j)
        graph.plot(2000+j, cmap)
        j += 1
        cur = nCell
        cur.visited = True
        cells_visited += 1
    graph.print_maze(2000+j)
    graph.plot(2000+j, cmap)


def binary(graph):
    cmap = graph.random_colors()
    j = 0
    graph.print_maze(1000+j)
    graph.plot(1000+j, cmap)
    j += 1
    for y in range(graph.numRows):
        for x in range(graph.numCols):
            neighbors = []
            if x > 0:
                neighbors.append(('W', graph.map[x-1][y]))
            if y > 0:
                neighbors.append(('N', graph.map[x][y-1]))
            if not neighbors:
                continue
            dir, cell = random.choice(neighbors)
            graph.map[x][y].visited = True
            graph.map[x][y].destroy_wall(cell, dir)
            graph.print_maze(1000+j)
            graph.plot(1000+j, cmap)
            j += 1

def sidewinder(graph):
    for y in range(graph.numRows):
        run = 0
        for x in range(graph.numCols):
            roll = [True, False, False]
            if y > 0 and (x+1 == graph.numCols or not random.choice(roll)):
                t = run + random.randint(0, x - run)
                graph.map[t][y].destroy_wall(graph.map[t][y-1], 'N')
                run = x + 1
            elif x+1 < graph.numCols:
                graph.map[x][y].destroy_wall(graph.map[x+1][y], 'E')

def kruskals(graph):
    edges = []
    sets = []
    for y in range(graph.numRows):
        for x in range(graph.numCols):
            neighbors = graph.get_neighbors(graph.map[x][y])
            sets.append({graph.map[x][y]})
            for dir, neighbor in neighbors:
                edges.append((graph.map[neighbor.x][neighbor.y], dir))
    while edges:
        curEdge, dir = random.choice(edges)
        if dir == 'W':
            s1 = 0
            s2 = 0
            for i in range(len(sets)):
                if graph.map[curEdge.x+1][curEdge.y] in sets[i]:
                    s1 = i
                if graph.map[curEdge.x][curEdge.y] in sets[i]:
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
                graph.map[curEdge.x+1][curEdge.y].destroy_wall(graph.map[curEdge.x][curEdge.y], 'W')

        elif dir == 'E':
            s1 = 0
            s2 = 0
            for i in range(len(sets)):
                if graph.map[curEdge.x-1][curEdge.y] in sets[i]:
                    s1 = i
                if graph.map[curEdge.x][curEdge.y] in sets[i]:
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
                graph.map[curEdge.x-1][curEdge.y].destroy_wall(graph.map[curEdge.x][curEdge.y], 'E')

        elif dir == 'S':
            s1 = 0
            s2 = 0
            for i in range(len(sets)):
                if graph.map[curEdge.x][curEdge.y-1] in sets[i]:
                    s1 = i
                if graph.map[curEdge.x][curEdge.y] in sets[i]:
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
                graph.map[curEdge.x][curEdge.y-1].destroy_wall(graph.map[curEdge.x][curEdge.y], 'S')

        elif dir == 'N':
            s1 = 0
            s2 = 0
            for i in range(len(sets)):
                if graph.map[curEdge.x][curEdge.y+1] in sets[i]:
                    s1 = i
                if graph.map[curEdge.x][curEdge.y] in sets[i]:
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
                graph.map[curEdge.x][curEdge.y+1].destroy_wall(graph.map[curEdge.x][curEdge.y], 'N')

        edges.remove((curEdge, dir))
