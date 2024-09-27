import pygame as pg 
from random import randrange

# Constants
window = 1000
Title_Size = 50
half_title = Title_Size // 2

# Helper function to get random positions
def get_random_position():
    return [randrange(half_title, window - half_title, Title_Size),
            randrange(half_title, window - half_title, Title_Size)]

# Initialize the snake and its properties
snake = pg.rect.Rect([0, 0, Title_Size - 2, Title_Size - 2])
snake.center = get_random_position()
length = 1
segments = [snake.copy()]
snake_dir = (0, 0)

# Timing and food
time, time_step = 0, 110
food = snake.copy()
food.center = get_random_position()

# Pygame setup
pg.init()
screen = pg.display.set_mode([window] * 2)
clock = pg.time.Clock()

# Direction restrictions (to prevent reverse movement)
dirs = {pg.K_w: (0, -Title_Size), pg.K_s: (0, Title_Size), pg.K_a: (-Title_Size, 0), pg.K_d: (Title_Size, 0)}

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w and snake_dir != dirs[pg.K_s]:  # Prevent reverse movement
                snake_dir = dirs[pg.K_w]
            if event.key == pg.K_s and snake_dir != dirs[pg.K_w]:  # Prevent reverse movement
                snake_dir = dirs[pg.K_s]
            if event.key == pg.K_a and snake_dir != dirs[pg.K_d]:  # Prevent reverse movement
                snake_dir = dirs[pg.K_a]
            if event.key == pg.K_d and snake_dir != dirs[pg.K_a]:  # Prevent reverse movement
                snake_dir = dirs[pg.K_d]

    # Fill the screen with black color
    screen.fill('black')

    # Check for border collisions or self-eating
    self_eating = pg.Rect.collidelist(snake, segments[:-1]) != -1
    if (snake.left < 0 or snake.right > window or snake.top < 0 or snake.bottom > window or self_eating):
        # Reset the game if collision occurs
        snake.center, food.center = get_random_position(), get_random_position()
        length, snake_dir = 1, (0, 0)
        segments = [snake.copy()]

    # Check for food collision
    if snake.colliderect(food):  # Use colliderect to check collision
        food.center = get_random_position()
        length += 1  # Increase snake length

    # Draw the food
    pg.draw.rect(screen, 'red', food)

    # Draw the snake
    [pg.draw.rect(screen, 'green', segment) for segment in segments]

    # Move the snake based on the time_step
    time_now = pg.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir)  # Move the snake
        segments.append(snake.copy())  # Add new segment
        segments = segments[-length:]  # Keep only the last 'length' segments

    # Update the display
    pg.display.flip()
    clock.tick(60)

