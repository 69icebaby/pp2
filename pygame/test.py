import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set default drawing parameters
drawing_color = BLACK
drawing_tool = "rectangle"
drawing_size = 20

# Define toolbar dimensions and positions
toolbar_height = 50
toolbar_color = (200, 200, 200)
toolbar_rect = pygame.Rect(0, 0, WIDTH, toolbar_height)
button_width = 50
button_padding = 10

# Define buttons for drawing tools
rect_button = pygame.Rect(button_padding, button_padding, button_width, button_width)
circle_button = pygame.Rect(rect_button.right + button_padding, button_padding, button_width, button_width)
eraser_button = pygame.Rect(circle_button.right + button_padding, button_padding, button_width, button_width)

# Define buttons for colors
black_button = pygame.Rect(WIDTH - 4 * (button_width + button_padding), button_padding, button_width, button_width)
red_button = pygame.Rect(black_button.right + button_padding, button_padding, button_width, button_width)
green_button = pygame.Rect(red_button.right + button_padding, button_padding, button_width, button_width)
blue_button = pygame.Rect(green_button.right + button_padding, button_padding, button_width, button_width)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if any tool button is clicked
            if rect_button.collidepoint(event.pos):
                drawing_tool = "rectangle"
            elif circle_button.collidepoint(event.pos):
                drawing_tool = "circle"
            elif eraser_button.collidepoint(event.pos):
                drawing_tool = "eraser"
            # Check if any color button is clicked
            elif black_button.collidepoint(event.pos):
                drawing_color = BLACK
            elif red_button.collidepoint(event.pos):
                drawing_color = RED
            elif green_button.collidepoint(event.pos):
                drawing_color = GREEN
            elif blue_button.collidepoint(event.pos):
                drawing_color = BLUE
        elif event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]: # Добавим проверку на движение мыши и нажатие левой кнопки
            # Draw on the window
            if drawing_tool == "rectangle":
                pygame.draw.rect(window, drawing_color, pygame.Rect(pygame.mouse.get_pos(), (drawing_size, drawing_size)))
            elif drawing_tool == "circle":
                pygame.draw.circle(window, drawing_color, pygame.mouse.get_pos(), drawing_size // 2)
            elif drawing_tool == "eraser":
                pygame.draw.rect(window, WHITE, pygame.Rect(pygame.mouse.get_pos(), (drawing_size, drawing_size)))
    
    # Update the display after each drawing operation
    pygame.display.update()

    # Clear the window
    window.fill(WHITE)

    # Draw the toolbar
    pygame.draw.rect(window, toolbar_color, toolbar_rect)

    # Draw tool buttons
    pygame.draw.rect(window, BLACK, rect_button)
    pygame.draw.circle(window, BLACK, (circle_button.centerx, circle_button.centery), button_width // 2)
    pygame.draw.rect(window, WHITE, eraser_button)

    # Draw color buttons
    pygame.draw.rect(window, BLACK, black_button)
    pygame.draw.rect(window, RED, red_button)
    pygame.draw.rect(window, GREEN, green_button)
    pygame.draw.rect(window, BLUE, blue_button)

    # Draw selected tool indicator
    if drawing_tool == "rectangle":
        pygame.draw.rect(window, (255, 0, 0), rect_button, 3)
    elif drawing_tool == "circle":
        pygame.draw.circle(window, (255, 0, 0), (circle_button.centerx, circle_button.centery), button_width // 2 + 3, 3)
    elif drawing_tool == "eraser":
        pygame.draw.rect(window, (255, 0, 0), eraser_button, 3)

    # Draw selected color indicator
    pygame.draw.rect(window, (255, 0, 0), (black_button.x - 2, black_button.y - 2, button_width + 4, button_width + 4), 3)
