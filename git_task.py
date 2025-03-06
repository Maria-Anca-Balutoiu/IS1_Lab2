import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 500, 500
GRID_SIZE = 10
CELL_SIZE = WIDTH // GRID_SIZE
REGENERATION_INTERVAL = 5000  # 5000 milliseconds = 5 seconds

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Procedural Color Grid (Regenerates every 5 seconds)")

# Function to generate a new random color grid
def generate_grid():
    return [[(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) 
             for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Initial grid
grid = generate_grid()
last_regeneration_time = pygame.time.get_ticks()  # Time of the last grid regeneration

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

    # Check if 5 seconds have passed to regenerate the grid
    current_time = pygame.time.get_ticks()
    if current_time - last_regeneration_time >= REGENERATION_INTERVAL:
        grid = generate_grid()  # Regenerate the grid
        last_regeneration_time = current_time  # Update the last regeneration time

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                grid = generate_grid()  # Regenerate grid when SPACE is pressed
                last_regeneration_time = current_time  # Reset the regeneration timer

pygame.quit()
