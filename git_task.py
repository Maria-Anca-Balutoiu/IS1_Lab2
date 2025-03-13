import pygame
import random
import time
# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 500, 500
GRID_SIZE = 10
CELL_SIZE = WIDTH // GRID_SIZE

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Procedural Color Grid (Press SPACE to Regenerate)")

# Function to generate a new random color grid
def generate_grid():
    return [[(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) 
             for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Initial grid
grid = generate_grid()

# Main loop
now_time = time.time()
counter_time = time.time() + 5
running = True
while running:
    initial_time = time.time()
    screen.fill((0, 0, 0))
    
    # Draw the grid
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            pygame.draw.rect(screen, grid[y][x], 
                             (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()

    # Event handling
    now_time = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if now_time > counter_time :
        grid = generate_grid()  # Regenerate grid when SPACE is pressed
        counter_time = time.time() + 5

pygame.quit()