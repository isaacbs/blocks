from grid import Grid
import time
import csv

def run_tests(alg, width, height,k):
    print('Tests on ' + alg + ' maze generation algorithm')
    print('Maze size: ' + str(width) + ' by ' + str(height))
    print('+--------------------------------------------+')
    g = Grid(width,height)
    g.create_grid()
    if alg == 'depth_first':
        g.depth_first()
    elif alg == 'binary':
        g.binary()
    elif alg == 'sidewinder':
        g.sidewinder()
    else:
        g.kruskals()

    mat = g.create_adj_matrix()
    adj = g.convert(mat)
    # g.print_maze(k)
    # g.plot(k)


    a1 = time.time()
    g.dfs_shortest_path(adj,0,height*width-1)
    a2 = time.time()
    g.dfs_shortest_path(adj,0,height*width//2-1)
    b1 = time.time()
    g.bfs_shortest_path(adj,0, height*width-1)
    b2 = time.time()
    g.bfs_shortest_path(adj,0, height*width//2-1)
    c1 = time.time()
    g.a_star_algorithm(adj,0,height*width-1)
    c2 = time.time()
    g.a_star_algorithm(adj,0,height*width//2-1)
    d = time.time()



    print('Time taken to compute the solution with Depth First Search')
    print(a2-a1)
    print('Time taken to compute the solution with Depth First Search to middle of right hand side')
    print(b1-a2)
    print('Time taken to compute the solution with Breadth First Search')
    print(b2-b1)
    print('Time taken to compute the solution with Breadth First Search to middle of right hand side')
    print(c1-b2)
    print('Time taken to compute the solution with A* Search')
    print(c2-c1)
    print('Time taken to compute the solution with A* Search to middle of right hand side')
    print(d-c2)
    print('+--------------------------------------------+')
    times = [a2-a1,b1-a2,b2-b1,c1-b2,c2-c1,d-c2]
    return times


depth_first_times = []
for i in range(10,26):
    for j in range(5):
        depth_first_times.append(run_tests('depth_first', i, i, i))

with open("depth_first_change.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(depth_first_times)
print(depth_first_times)

binary_times = []
for i in range(10,26):
    for j in range(5):
        binary_times.append(run_tests('binary', i, i, i+50))
    
with open("binary_change.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(binary_times)
print(binary_times)

sidewinder_times = []
for i in range(10,26):
    for j in range(5):
        sidewinder_times.append(run_tests('sidewinder', i, i, i+100))
    
with open("sidewinder_change.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(sidewinder_times)
print(sidewinder_times)

kruskals_times = []
for i in range(10,26):
    for j in range(5):
        kruskals_times.append(run_tests('kruskals', i, i, i+150))
    
with open("kruskals_change.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(kruskals_times)
print(kruskals_times)