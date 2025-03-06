import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 500, 500
GRID_SIZE = 10
CELL_SIZE = WIDTH // GRID_SIZE
UPDATE_EVENT = pygame.USEREVENT + 1
UPDATE_INTERVAL = 5000  # 5 seconds

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Procedural Color Grid ")

# Function to generate a new random color grid
def generate_grid():
    return [[(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) 
             for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Initial grid
grid = generate_grid()

# Set timer event to update grid every 5 seconds
pygame.time.set_timer(UPDATE_EVENT, UPDATE_INTERVAL)

# Main loop
running = True
while running:
    screen.fill((0, 0, 0))
    
    # Draw the grid
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            pygame.draw.rect(screen, grid[y][x], 
                             (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == UPDATE_EVENT:
            grid = generate_grid()  # Regenerate grid every 5 seconds

pygame.quit()