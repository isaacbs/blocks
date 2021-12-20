import random
import math
from cell import Cell
import matplotlib
from matplotlib import colors as c
import matplotlib.pyplot as plt
import numpy
from PIL import Image
import glob
    

class Grid:
    """A grid of cells used to make up the maze"""
    def __init__(self, numCols, numRows):
        self.numCols = numCols
        self.numRows = numRows
    # map: list[Cell] = dc.field(default_factory=list)
        map = [[Cell(i, j) for j in range(numRows)] for i in range(numCols)]

    def create_grid(self):
        self.map = [[Cell(i, j) for j in range(self.numRows)] for i in range(self.numCols)]
        self.map[0][0].visited = True
    
    def get_cell(self, x, y):
        return self.map[x][y]

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
        

    def print_maze(self, num):
        rows = ['+-' * (self.numCols) + "+"]
        for r in range(self.numRows):
            row = ['|']
            for col in range(self.numCols):
                if col == self.numCols-1:
                    if self.map[col][r].visited:
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
                        if self.map[col][r].insolution:
                            if self.map[col][r].walls['E']:
                                row.append('*|')
                            else:
                                row.append('*.')
                        else:
                            if self.map[col][r].walls['E']:
                                row.append('.|')
                            else:
                                row.append('..')
                else:
                    if self.map[col][r].visited:
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
                                row.append('*.')
                        else:
                            if self.map[col][r].walls['E']:
                                row.append('.|')
                            else:
                                row.append('..')
            rows.append(''.join(row))
            row = ['+']



            for col in range(self.numCols):
                if r == self.numRows-1:
                    if self.map[col][r].visited:
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
                        if self.map[col][r].insolution:
                            if self.map[col][r].walls['S']:
                                row.append('-+')
                            else:
                                row.append('.+')
                        else:
                            if self.map[col][r].walls['S']:
                                row.append('-+')
                            else:
                                row.append('.+')
                else:
                    if self.map[col][r].visited:
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
                                row.append('.+')
                        else:
                            if self.map[col][r].walls['S']:
                                row.append('-+')
                            else:
                                row.append('.+')
            rows.append(''.join(row))
        maze_file = open("text/maze" + str(num) + ".txt", "w")
        maze_file.write('\n'.join(rows))
        maze_file.close()
        return '\n'.join(rows)




    def plot(self, number, cmap):
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

        plt.pcolormesh(maze, cmap=cmap)
        plt.axis('off')
        plt.xticks([]) # remove the tick marks by setting to an empty list
        plt.yticks([]) # remove the tick marks by setting to an empty list
        fname = 'output/maze' + str(number) + '.png'
        plt.savefig(fname, dpi=300, bbox_inches='tight',pad_inches=0, edgecolor='auto')

        plt.clf()
        return

    def random_colors(self):
        colors = ['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 
        'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r',
         'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 
         'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 
         'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r']


        c1 = random.choice(colors)

        cmap = matplotlib.colors.ListedColormap(numpy.random.rand (256,3))
        return cmap

    
    def create_gif(self):
        # Create the frames
        frames = []
        imgs = glob.glob("output/maze*.png")
        for i in imgs:
            new_frame = Image.open(i)
            frames.append(new_frame)
        
        # Save into a GIF file that loops forever
        frames[0].save('maze2.gif', format='GIF',
                    append_images=frames[1:],
                    save_all=True,
                    duration=100, loop=0)