# Importing necessary modules
import pygame
import random

# Initializing pygame
pygame.init()

# Setting up window dimensions and frames per second
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
FPS = 30

# Creating the game window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)

# Creating a clock to control the frame rate
clock = pygame.time.Clock()

# Flag to control game loop termination
done = False

# Background color
bg = (0, 0, 0)

# Paddle attributes
paddleW = 150  # Paddle width
paddleH = 25   # Paddle height
paddleSpeed = 20  # Paddle movement speed
paddle = pygame.Rect(WINDOW_WIDTH // 2 - paddleW // 2, WINDOW_HEIGHT - paddleH - 30, paddleW, paddleH)  # Paddle rectangle

# Ball attributes
ballRadius = 20   # Ball radius
ballSpeed = 6     # Ball movement speed
ball_rect = int(ballRadius * 2 ** 0.5)  # Square enclosing the ball
ball = pygame.Rect(random.randrange(ball_rect, WINDOW_WIDTH - ball_rect), WINDOW_HEIGHT // 2, ball_rect, ball_rect)  # Ball rectangle
dx, dy = 1, -1  # Ball movement direction

# Game score
game_score = 0  # Initial score
game_score_fonts = pygame.font.SysFont('comicsansms', 40)  # Font for displaying score
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))  # Text surface for score
game_score_rect = game_score_text.get_rect()  # Rectangle for score display
game_score_rect.center = (210, 20)  # Position for score display

# Sound for collision
collision_sound = pygame.mixer.Sound(r"C:\Users\baurs\Desktop\pp2\lab9\arkanoid pics\Catch.mp3")

# Time variables for game events
time_elapsed = 0
speed_increase_interval = 1000  # Interval for increasing ball speed (milliseconds)
speed_increase_amount = 0.2     # Amount of speed increase
shrink_paddle_interval = 5000    # Interval for shrinking paddle (milliseconds)
shrink_paddle_amount = 10        # Amount of paddle shrinkage

# Pause state
is_paused = False

# Function to detect collision between ball and objects
def detect_collision(dx, dy, ball, rect):
    # Algorithm to detect collision and adjust ball movement
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    elif delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy

# Block settings
block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50) for i in range(10) for j in range(4)]  # Creating blocks
color_list = [(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)) for i in range(10) for j in range(4)]  # Colors for blocks

# Randomly choosing unbreakable blocks
unbreakable_block_list = []
for _ in range(5):
    random_index = random.randint(0, len(block_list) - 1)
    unbreakable_block_list.append(block_list.pop(random_index))

unbreakable_color_list = [(0, 0, 255) for _ in range(len(unbreakable_block_list))]  # Color for unbreakable blocks

# Bonus brick types with perks and messages
bonus_brick_types = {
    "longer_paddle": {"color": (0, 255, 0), "perk": "paddle", "message": "Longer paddle!"},
    "increase_speed": {"color": (255, 165, 0), "perk": "speed", "message": "Speed Up!"},
}

# Generating bonus bricks
bonus_brick_list = []
for _ in range(5):
    random_index = random.randint(0, len(block_list) - 1)
    bonus_brick_type = random.choice(list(bonus_brick_types.keys()))
    bonus_brick_list.append((block_list.pop(random_index), bonus_brick_type))

# Game over screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

# Win screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = winfont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

# Message variables
message_font = pygame.font.SysFont('comicsansms', 40)
last_message = ""  # Last message displayed
last_message_rect = None  # Rectangle for last message

# Main game loop
while not done:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Pause toggle
                is_paused = not is_paused
            if is_paused:
                if event.key == pygame.K_w:
                    paddleW += 10
                    paddle = pygame.Rect(paddle.left, paddle.top, paddleW, paddleH)  # Adjust paddle size
                if event.key == pygame.K_s and paddleW > 10:
                    paddleW -= 10
                    paddle = pygame.Rect(paddle.left, paddle.top, paddleW, paddleH)  # Adjust paddle size
                if event.key == pygame.K_d:
                    ballRadius += 1
                if event.key == pygame.K_a and ballRadius > 1:
                    ballRadius -= 1

    # Pause screen
    if is_paused:
        screen.fill((100, 100, 100))
        pause_text = game_score_fonts.render('Game Paused. Press P to resume.', True, (255, 255, 255))
        settings_text_1 = game_score_fonts.render(
            f'Paddle Width: {paddleW}, Ball Radius: {ballRadius}.', True,
            (255, 255, 255))
        settings_text_2 = game_score_fonts.render(
            'W/S: Adjust paddle. D/A: Adjust ball.', True,
            (255, 255, 255))

        screen.blit(pause_text, (WINDOW_WIDTH / 2 - pause_text.get_width() / 2, WINDOW_HEIGHT / 2 - pause_text.get_height() / 2 - 20))
        screen.blit(settings_text_1, (WINDOW_WIDTH / 2 - settings_text_1.get_width() / 2, WINDOW_HEIGHT / 2 + 20))
        screen.blit(settings_text_2, (WINDOW_WIDTH / 2 - settings_text_2.get_width() / 2, WINDOW_HEIGHT / 2 + 80))

        pygame.display.flip()
        continue

    # Clearing the screen
    screen.fill(bg)

    # Drawing blocks
    [pygame.draw.rect(screen, color_list[color], block) for color, block in enumerate(block_list)]
    [pygame.draw.rect(screen, (0, 0, 255), block) for block in unbreakable_block_list]

    # Drawing paddle and ball
    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)

    # Moving the ball
    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy

    # Handling ball collisions with window boundaries
    if ball.centerx < ballRadius or ball.centerx > WINDOW_WIDTH - ballRadius:
        dx = -dx
    if ball.centery < ballRadius + 50:
        dy = -dy

    # Handling ball collision with paddle
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)

    # Handling ball collision with breakable blocks
    hitIndex = ball.collidelist(block_list)
    if hitIndex != -1:
        hitRect = block_list.pop(hitIndex)
        hitColor = color_list.pop(hitIndex)
        dx, dy = detect_collision(dx, dy, ball, hitRect)
        game_score += 1
        collision_sound.play()

    # Handling ball collision with unbreakable blocks
    for i, unbreakable_block in enumerate(unbreakable_block_list):
        if ball.colliderect(unbreakable_block):
            dx, dy = detect_collision(dx, dy, ball, unbreakable_block)

    # Drawing and handling bonus bricks
    for block, bonus_type in bonus_brick_list:
        pygame.draw.rect(screen, bonus_brick_types[bonus_type]["color"], block)

    for i, (bonus_brick, bonus_type) in enumerate(bonus_brick_list):
        if ball.colliderect(bonus_brick):
            # Applying bonus brick perk
            if bonus_brick_types[bonus_type]["perk"] == "speed":
                ballSpeed += 2  # Example increase in speed

            # Updating last message
            last_message = bonus_brick_types[bonus_type]["message"]
            last_message_surface = message_font.render(last_message, True, (255, 255, 255))
            last_message_rect = last_message_surface.get_rect(topright=(WINDOW_WIDTH - 10, -10))

            # Removing the bonus brick from the list
            del bonus_brick_list[i]
            break

    # Displaying last message
    if last_message:
        screen.blit(last_message_surface, last_message_rect)

    # Updating and displaying game score
    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)

    # Checking for game over conditions
    if ball.bottom > WINDOW_HEIGHT:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
    elif not len(block_list):
        screen.fill((255, 255, 255))
        screen.blit(wintext, wintextRect)
        pygame.display.flip()
        continue

    # Increasing ball speed over time
    time_elapsed += clock.get_rawtime()
    if time_elapsed >= speed_increase_interval:
        ballSpeed += speed_increase_amount
        time_elapsed = 0

    # Shrinking paddle over time
    if time_elapsed >= shrink_paddle_interval:
        paddleW -= shrink_paddle_amount
        if paddleW < 50:
            paddleW = 50
        paddle.width = paddleW
        time_elapsed = 0

    # Handling paddle movement
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < WINDOW_WIDTH:
        paddle.right += paddleSpeed

    # Updating the display and controlling the frame rate
    pygame.display.flip()
    clock.tick(FPS)
