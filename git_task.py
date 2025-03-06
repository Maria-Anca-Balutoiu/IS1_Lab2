import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 500, 500
GRID_SIZE = 10
CELL_SIZE = WIDTH // GRID_SIZE
UPDATE_INTERVAL = 5000  # 5000 ms = 5 secunde

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Procedural Color Grid (Regenerates Every 5 Seconds)")

# Function to generate a new random color grid
def generate_grid():
    return [[(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) 
             for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Initial grid
grid = generate_grid()
last_update_time = pygame.time.get_ticks()  # Store the initial time

# Main loop
running = True
while running:
    screen.fill((0, 0, 0))
    
    # Check if 5 seconds have passed
    current_time = pygame.time.get_ticks()
    if current_time - last_update_time > UPDATE_INTERVAL:
        grid = generate_grid()
        last_update_time = current_time  # Reset the timer

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

pygame.quit()
