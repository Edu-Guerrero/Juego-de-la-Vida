from time import sleep
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 500, 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game of Life")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
option = 0
color_options = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (255, 255, 0), (255, 0, 255), (0, 255, 255), (255, 255, 255)]
selector = color_options[option]

# Define grid size
rows, cols = 15, 15
cell_size = width // cols

def draw_grid():
    for x in range(0, width, cell_size):
        for y in range(0, height, cell_size):
            rect = pygame.Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(window, white, rect, 1)

# Create a 2D array to store the state of each cell
grid = [[0 for _ in range(cols)] for _ in range(rows)]
next_grid = [[0 for _ in range(cols)] for _ in range(rows)]

def draw_cells():
    for row in range(rows):
        for col in range(cols):
            color = selector if grid[row][col] == 1 else black
            rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
            pygame.draw.rect(window, color, rect)

def get_cell_pos(mouse_pos):
    x, y = mouse_pos
    return y // cell_size, x // cell_size

def print_current_matrix():
    for i in range(rows):
        for j in range(cols):
            print(grid[i][j], end=" ")
            if (i == 3 and j == 3) or (i == 0 and j == 0):
                neigh = get_neighbours(i, j)
                print("There are", neigh, "neighbours at", i, j)
        print() 
    print() 
    
def analyze_matrix():
    print("Analyzing matrix")
    for i in range(rows):
        for j in range(cols):
            neighbours = get_neighbours(i, j)
            if grid[i][j] == 1:
                if neighbours < 2 or neighbours > 3:
                    next_grid[i][j] = 0
                else:
                    next_grid[i][j] = 1
            else:
                if neighbours == 3:
                    next_grid[i][j] = 1
                else:
                    next_grid[i][j] = 0

    for i in range(rows):
        for j in range(cols):
            grid[i][j] = next_grid[i][j]

def get_neighbours(row, col):
    neighbours = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if grid[(row + i) % rows][(col + j) % cols] == 1 and (i != 0 or j != 0):
                neighbours += 1
    return neighbours

def reset_grid():
    for i in range(rows):
        for j in range(cols):
            grid[i][j] = 0

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            row, col = get_cell_pos(pygame.mouse.get_pos())
            grid[row][col] = 1 if grid[row][col] == 0 else 0
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                analyze_matrix()
            elif event.key == pygame.K_RETURN:
                timer = 0
                paused = True
                while paused:
                    analyze_matrix()
                    draw_cells()
                    draw_grid()
                    pygame.display.flip()
                    print(f"Working for {timer} seconds")
                    timer += 1
                    sleep(0.5)
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                            ("Stopped")
                            paused = False
            elif event.key == pygame.K_r:
                reset_grid()
            elif event.key == pygame.K_c:
                option += 1
                option %= len(color_options)
                selector = color_options[option]
                draw_cells()
                draw_grid()
                    

    window.fill(white)
    draw_cells()
    draw_grid()
    pygame.display.flip()

pygame.quit()
sys.exit()