import pygame

# Initialize pygame
pygame.init()

# List to store painted shapes
painting = []

# Clock for controlling the frame rate
timer = pygame.time.Clock()
fps = 60

# Initial active color and shape
activeColor = (0, 0, 0)
activeShape = 0

# Screen dimensions
w = 800
h = 600

# Create the display window
screen = pygame.display.set_mode([w, h])
pygame.display.set_caption("Paint")

# Function to draw the display including buttons for shapes and colors
def drawDisplay():
    # Draw top bar
    pygame.draw.rect(screen, 'gray', [0, 0, w, 100])
    pygame.draw.line(screen, 'black', [0, 100], [w, 100])
    
    # Define shapes buttons
    rect = [pygame.draw.rect(screen, 'black', [10, 10, 80, 80]), 0]  # Square button
    pygame.draw.rect(screen, 'white', [20, 20, 60, 60])  # Square shape
    
    circ = [pygame.draw.rect(screen, 'black', [100, 10, 80, 80]), 1]  # Circle button
    pygame.draw.circle(screen, 'white', [140, 50], 30)  # Circle shape
    
    right_triangle = [pygame.draw.rect(screen, 'black', [190, 10, 80, 80]), 2]  # Right triangle button
    pygame.draw.polygon(screen, 'white', [(230, 90), (190, 90), (230, 10)])  # Right triangle shape
    
    equilateral_triangle = [pygame.draw.rect(screen, 'black', [280, 10, 80, 80]), 3]  # Equilateral triangle button
    height = 80 * (3 ** 0.5) / 2
    pygame.draw.polygon(screen, 'white', [
        (320, 90 - height),
        (320 - 40, 90),
        (320 + 40, 90)
    ])  # Equilateral triangle shape
    
    rhombus = [pygame.draw.rect(screen, 'black', [370, 10, 80, 80]), 4]  # Rhombus button
    pygame.draw.polygon(screen, 'white', [
        (410, 50),
        (370, 70),
        (410, 90),
        (450, 70)
    ])  # Rhombus shape
    
    # Define color buttons
    colors = [
        [pygame.draw.rect(screen, (0, 0, 255), [w - 35, 10, 25, 25]), (0, 0, 255)],  # Blue
        [pygame.draw.rect(screen, (255, 0, 0), [w - 35, 35, 25, 25]), (255, 0, 0)],  # Red
        [pygame.draw.rect(screen, (0, 255, 0), [w - 60, 10, 25, 25]), (0, 255, 0)],  # Green
        [pygame.draw.rect(screen, (255, 255, 0), [w - 60, 35, 25, 25]), (255, 255, 0)],  # Yellow
        [pygame.draw.rect(screen, (0, 0, 0), [w - 85, 10, 25, 25]), (0, 0, 0)],  # Black
        [pygame.draw.rect(screen, (255, 0, 255), [w - 85, 35, 25, 25]), (255, 0, 255)],  # Magenta
        [pygame.draw.rect(screen, (255, 255, 255), [w - 150, 20, 25, 25]), (255, 255, 255)]  # White
    ]
    
    # List to hold shape buttons
    shapes = [rect, circ, right_triangle, equilateral_triangle, rhombus]
    
    return colors, shapes

# Function to draw the painted shapes on the screen
def drawPaint(paints):
    for paint in paints:
        color, position, shape = paint
        # Draw the shapes based on the 'shape' type
        if shape == 0:  # Square
            pygame.draw.rect(screen, color, [position[0] - 15, position[1] - 15, 30, 30])
        elif shape == 1:  # Circle
            pygame.draw.circle(screen, color, position, 15)
        elif shape == 2:  # Right Triangle
            points = [
                (position[0], position[1]),
                (position[0], position[1] - 30),
                (position[0] + 30, position[1])
            ]
            pygame.draw.polygon(screen, color, points)
        elif shape == 3:  # Equilateral Triangle
            height = 30 * (3 ** 0.5) / 2
            points = [
                (position[0], position[1] - height),
                (position[0] - 15, position[1] + 15),
                (position[0] + 15, position[1] + 15)
            ]
            pygame.draw.polygon(screen, color, points)
        elif shape == 4:  # Rhombus
            points = [
                (position[0], position[1] - 15),
                (position[0] - 15, position[1]),
                (position[0], position[1] + 15),
                (position[0] + 15, position[1])
            ]
            pygame.draw.polygon(screen, color, points)
            
# Function to draw shapes being painted by the user
def draw():
    global activeColor, activeShape, mouse
    if mouse[1] > 100:
        if activeShape == 0:  # Square
            pygame.draw.rect(screen, activeColor, [mouse[0] - 15, mouse[1] - 15, 30, 30])
        elif activeShape == 1:  # Circle
            pygame.draw.circle(screen, activeColor, mouse, 15)
        elif activeShape == 2:  # Right Triangle
            points = [
                (mouse[0], mouse[1]),
                (mouse[0], mouse[1] - 30),
                (mouse[0] + 30, mouse[1])
            ]
            pygame.draw.polygon(screen, activeColor, points)
        elif activeShape == 3:  # Equilateral Triangle
            height = 30 * (3 ** 0.5) / 2
            points = [
                (mouse[0], mouse[1] - height),
                (mouse[0] - 15, mouse[1] + 15),
                (mouse[0] + 15, mouse[1] + 15)
            ]
            pygame.draw.polygon(screen, activeColor, points)
        elif activeShape == 4:  # Rhombus
            points = [
                (mouse[0], mouse[1] - 15),
                (mouse[0] - 15, mouse[1]),
                (mouse[0], mouse[1] + 15),
                (mouse[0] + 15, mouse[1])
            ]
            pygame.draw.polygon(screen, activeColor, points)

# Main function
def main():
    global activeColor, activeShape, painting, mouse
    run = True
    while run:
        timer.tick(fps)
        screen.fill('white')
        colors, shapes = drawDisplay()
        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]
        
        # Paint shapes when mouse is clicked
        if click and mouse[1] > 100:
            painting.append((activeColor, (mouse[0], mouse[1]), activeShape))
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_SPACE:
                    painting = []
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Change active color or shape based on button clicked
                for color_button in colors:
                    if color_button[0].collidepoint(event.pos):
                        activeColor = color_button[1]
                for shape_button in shapes:
                    if shape_button[0].collidepoint(event.pos):
                        activeShape = shape_button[1]

        # Draw painted shapes and shapes being painted
        drawPaint(painting)
        draw()
        pygame.display.flip()

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
