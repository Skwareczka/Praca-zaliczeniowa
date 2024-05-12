import pygame
import timer
import random

pygame.init()

colour_1 = (255, 255, 255)
colour_2 = (255, 255, 102)
colour_3 = (0, 0, 0)
colour_4 = (213, 200, 80)
colour_5 = (0, 255, 0)
colour_6 = (255, 0, 0)

WIDHT = 900
HEIGHT = 600

add_caption = pygame.display.set_mode((WIDHT, HEIGHT))
pygame.display.set_caption('Snake')

timer = pygame.time.Clock()

snake_block = 10
snake_speed = 10



display_style = pygame.font.SysFont('arial', 30, 'bold')
score_font = pygame.font.SysFont('arial', 45, 'bold')

def final_score(score):
    value = score_font.render('Twój wynik to : ' + str(score), True, colour_2)
    add_caption.blit(value, [0,0])

def make_snake(snake_block, list_snake):
    for x in list_snake:
        pygame.draw.rect(add_caption, colour_3, [x[0], x[1], snake_block, snake_block])

def display_msg(msg,colour):
    mssg = display_style.render(msg, True, colour)
    add_caption.blit(mssg, [WIDHT/6, HEIGHT/3])

def game_start():
    game_over = False
    game_close = False

    value_x1 = WIDHT/2
    value_y1 = HEIGHT/2

    new_x1= 0
    new_y1 = 0

    list_snake = []
    snake_len = 1

    foodx_pos = round(random.randrange(0, WIDHT-snake_block) / 10.0) * 10.0
    foody_pos = round(random.randrange(0, HEIGHT-snake_block) / 10.0) * 10.0
    while not game_over:

        while game_close == True:
            add_caption.fill(colour_6)
            display_msg('Przegrałeś! Zagraj ponownie naciśnij S, koniec gry K', colour_4)
            final_score(snake_len-1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_k:
                        game_over = True
                        game_close = False
                    if event.key == pygame. K_s:
                        game_start()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame. K_LEFT:
                    new_x1 = -snake_block
                    new_y1 = 0
                elif event.key == pygame.K_RIGHT:
                    new_x1 = snake_block
                    new_y1 = 0
                elif event.key == pygame.K_UP:
                    new_y1 = -snake_block
                    new_x1 = 0
                elif event.key == pygame.K_DOWN:
                    new_y1 = snake_block
                    new_x1 = 0
        if value_x1>=WIDHT or value_x1<=0 or value_y1>=HEIGHT or value_y1<=0:
            game_close = True

        value_x1 = value_x1+new_x1
        value_y1 = value_y1+new_y1
        add_caption.fill(colour_6)
        pygame.draw.rect(add_caption, colour_5, [foodx_pos, foody_pos, snake_block, snake_block])
        snake_head = []
        snake_head.append(value_x1)
        snake_head.append(value_y1)
        list_snake.append(snake_head)
        if len(list_snake) > snake_len:
            del list_snake[0]

        for x in list_snake[:-1]:
            if x==snake_head:
                game_close = True

        make_snake(snake_block, list_snake)
        final_score(snake_len-1)


        pygame.display.update()

        if value_x1 == foodx_pos and value_y1 == foody_pos:
            foodx_pos = round(random.randrange(0, WIDHT-snake_block) / 10.0) * 10.0
            foody_pos = round(random.randrange(0, HEIGHT -snake_block) / 10.0) *10.0
            snake_len = snake_len+1

        timer.tick(snake_speed)

    pygame.quit()
    quit()

game_start()