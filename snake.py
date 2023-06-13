import pygame
import random

# Initialize the game
pygame.init()

# Set up the display
display_info = pygame.display.Info()
width, height = display_info.current_w, display_info.current_h
display = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.display.set_caption("Snake Game")

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the game clock
clock = pygame.time.Clock()

# Set up the snake
snake_block_size = 20
snake_speed = 15
direction = "right"

def snake(snake_block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(display, BLACK, [block[0], block[1], snake_block_size, snake_block_size])

def game_loop():
    game_quit = False

    while not game_quit:
        game_over = False
        multiplayer = False

        while not multiplayer:
            display.fill(WHITE)
            font_style = pygame.font.SysFont(None, int(height / 12))
            message = font_style.render("Snake Game", True, BLACK)
            display.blit(message, [width / 2 - message.get_width() / 2, height / 3 - message.get_height() / 2])
            message = font_style.render("Press 'S' for Single Player", True, BLACK)
            display.blit(message, [width / 2 - message.get_width() / 2, height / 2 - message.get_height() / 2])
            message = font_style.render("Press 'M' for Multiplayer", True, BLACK)
            display.blit(message, [width / 2 - message.get_width() / 2, height / 1.7 - message.get_height() / 2])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_quit = True
                    multiplayer = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        multiplayer = False
                        game_loop_single()
                    elif event.key == pygame.K_m:
                        multiplayer = True
                        game_loop_multi()

        pygame.display.update()

    pygame.quit()

def game_loop_single():
    # Set up the snake's initial position
    x1 = width / 2
    y1 = height / 2

    # Set up the snake's initial movement
    x1_change = 0
    y1_change = 0

    # Set up the snake's initial length and score
    snake_list = []
    snake_length = 1
    score = 0

    # Set up the food's initial position
    food_x = round(random.randrange(0, width - snake_block_size) / 20.0) * 20.0
    food_y = round(random.randrange(0, height - snake_block_size) / 20.0) * 20.0

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block_size
                    y1_change = 0
                    direction = "left"
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block_size
                    y1_change = 0
                    direction = "right"
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block_size
                    x1_change = 0
                    direction = "up"
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block_size
                    x1_change = 0
                    direction = "down"
                elif event.key == pygame.K_q:
                    game_over = True

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_over = True

        x1 += x1_change
        y1 += y1_change
        display.fill(WHITE)
        pygame.draw.rect(display, RED, [food_x, food_y, snake_block_size, snake_block_size])
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_over = True

        snake(snake_block_size, snake_list)
        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, width - snake_block_size) / 20.0) * 20.0
            food_y = round(random.randrange(0, height - snake_block_size) / 20.0) * 20.0
            snake_length += 1
            score += 1

        clock.tick(snake_speed)

    display.fill(WHITE)
    font_style = pygame.font.SysFont(None, int(height / 12))
    message = font_style.render("Game Over! Score: " + str(score), True, RED)
    display.blit(message, [width / 2 - message.get_width() / 2, height / 2 - message.get_height() / 2])
    pygame.display.update()
    pygame.time.wait(2000)

def game_loop_multi():
    # Set up the snakes' initial positions
    x1 = width / 4
    y1 = height / 2
    x2 = 3 * width / 4
    y2 = height / 2

    # Set up the snakes' initial movements
    x1_change = 0
    y1_change = 0
    x2_change = 0
    y2_change = 0

    # Set up the snakes' initial lengths and scores
    snake_list1 = []
    snake_list2 = []
    snake_length1 = 1
    snake_length2 = 1
    score1 = 0
    score2 = 0

    # Set up the food's initial position
    food_x = round(random.randrange(0, width - snake_block_size) / 20.0) * 20.0
    food_y = round(random.randrange(0, height - snake_block_size) / 20.0) * 20.0

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x1_change = -snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_d:
                    x1_change = snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_w:
                    y1_change = -snake_block_size
                    x1_change = 0
                elif event.key == pygame.K_s:
                    y1_change = snake_block_size
                    x1_change = 0
                elif event.key == pygame.K_LEFT:
                    x2_change = -snake_block_size
                    y2_change = 0
                elif event.key == pygame.K_RIGHT:
                    x2_change = snake_block_size
                    y2_change = 0
                elif event.key == pygame.K_UP:
                    y2_change = -snake_block_size
                    x2_change = 0
                elif event.key == pygame.K_DOWN:
                    y2_change = snake_block_size
                    x2_change = 0
                elif event.key == pygame.K_q:
                    game_over = True

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0 or x2 >= width or x2 < 0 or y2 >= height or y2 < 0:
            game_over = True

        x1 += x1_change
        y1 += y1_change
        x2 += x2_change
        y2 += y2_change
        display.fill(WHITE)
        pygame.draw.rect(display, RED, [food_x, food_y, snake_block_size, snake_block_size])
        snake_head1 = [x1, y1]
        snake_head2 = [x2, y2]
        snake_list1.append(snake_head1)
        snake_list2.append(snake_head2)
        if len(snake_list1) > snake_length1:
            del snake_list1[0]
        if len(snake_list2) > snake_length2:
            del snake_list2[0]

        for segment in snake_list1[:-1]:
            if segment == snake_head1 or segment == snake_head2:
                game_over = True
        for segment in snake_list2[:-1]:
            if segment == snake_head1 or segment == snake_head2:
                game_over = True

        snake(snake_block_size, snake_list1)
        snake(snake_block_size, snake_list2)
        pygame.display.update()

        if (x1 == food_x and y1 == food_y) or (x2 == food_x and y2 == food_y):
            food_x = round(random.randrange(0, width - snake_block_size) / 20.0) * 20.0
            food_y = round(random.randrange(0, height - snake_block_size) / 20.0) * 20.0
            if x1 == food_x and y1 == food_y:
                snake_length1 += 1
                score1 += 1
            if x2 == food_x and y2 == food_y:
                snake_length2 += 1
                score2 += 1

        clock.tick(snake_speed)

    display.fill(WHITE)
    font_style = pygame.font.SysFont(None, int(height / 12))
    if score1 > score2:
        message = font_style.render("Player 1 Wins! Score: " + str(score1), True, RED)
    elif score2 > score1:
        message = font_style.render("Player 2 Wins! Score: " + str(score2), True, RED)
    else:
        message = font_style.render("It's a Tie! Score: " + str(score1), True, RED)
    display.blit(message, [width / 2 - message.get_width() / 2, height / 2 - message.get_height() / 2])
    pygame.display.update()
    pygame.time.wait(2000)

game_loop()
