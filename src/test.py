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
    g.print_maze(k)
    g.plot(k)
    a = time.time()
    g.dfs_shortest_path(adj,0,height*width-1)
    b = time.time()
    g.bfs_shortest_path(adj,0, height*width-1)
    c = time.time()
    g.a_star_algorithm(adj,0,height*width-1)
    d = time.time()
    print('Time taken to compute the solution with Depth First Search')
    print(b-a)
    print('Time taken to compute the solution with Breadth First Search')
    print(c-b)
    print('Time taken to compute the solution with A* Search')
    print(d-c)
    print('+--------------------------------------------+')
    times = [b-a,c-b,d-c]
    return times


# depth_first_times = []
# for i in range(1,51):
#     for j in range(5):
#         depth_first_times.append(run_tests('depth_first', i, i, i))

# with open("depth_first.csv","w+") as my_csv:
#     csvWriter = csv.writer(my_csv,delimiter=',')
#     csvWriter.writerows(depth_first_times)
# print(depth_first_times)

# binary_times = []
# for i in range(1,51):
#     for j in range(5):
#         binary_times.append(run_tests('binary', i, i, i+50))
    
# with open("binary.csv","w+") as my_csv:
#     csvWriter = csv.writer(my_csv,delimiter=',')
#     csvWriter.writerows(binary_times)
# print(binary_times)

# sidewinder_times = []
# for i in range(1,51):
#     for j in range(5):
#         sidewinder_times.append(run_tests('sidewinder', i, i, i+100))
    
# with open("sidewinder.csv","w+") as my_csv:
#     csvWriter = csv.writer(my_csv,delimiter=',')
#     csvWriter.writerows(sidewinder_times)
# print(sidewinder_times)

kruskals_times = []
for i in range(1,50):
    for j in range(5):
        kruskals_times.append(run_tests('kruskals', i, i, i+150))
    
with open("kruskals.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(kruskals_times)
print(kruskals_times)