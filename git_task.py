import pygame
import random

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
running = True
#refresh = False
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
            # refresh = False
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         refresh = True
        #         #grid = generate_grid()  # Regenerate grid when SPACE is presse
        # elif event.type == pygame.KEYUP:
        #     if event.key == pygame.K_SPACE:
        #         refresh = False

    # if refresh is True:
    #     sleep(1000)
    #     grid = generate_grid()

    #pygame.time.wait(5000)
    if pygame.time.get_ticks() % 5000  == 0:
        grid = generate_grid()
    
pygame.quit()