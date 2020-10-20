import pygame
import random
import os

pygame.init()
screen_width=1200
screen_height=600
gameWindow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("my first game")

white=(255,255,255)
red=(255,0,0)
black=(0,0,0)

font = pygame.font.SysFont(None, 55)
clock = pygame.time.Clock()




def screen_score(text,color,x,y):           #text on screen func
    screen_text= font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])

def plot_snake(gameWindow, color,snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x,y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(white)
        screen_score("welcome to snakes press space to play",black,260,250)
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()
        pygame.display.update()
        clock.tick(60)



def game_loop():
    if(not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w") as f:
            f.write("0")

	
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    exit_game = False
    game_over = False
    snake_x = 55
    snake_y = 40
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snake_length = 1
    snake_size = 20
    fps = 60
    init_velocity = 5
    food_x = random.randint(0, screen_width / 2)
    food_y = random.randint(0, screen_height / 2)
    score = 0

    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            screen_score("game over press enter to play again",red,300,300)
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()
        else:
            for event in pygame.event.get():
                #print(event)
                if event.type==pygame.QUIT:
                    exit_game = True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x=init_velocity
                        velocity_y =0
                    if event.key==pygame.K_LEFT:
                        velocity_x=-init_velocity
                        velocity_y = 0
                    if event.key==pygame.K_UP:
                        velocity_y=-init_velocity
                        velocity_x =0
                    if event.key==pygame.K_DOWN:
                        velocity_y=init_velocity
                        velocity_x =0
                    if event.key==pygame.K_q:
                        score=score+10
            snake_x=snake_x+velocity_x
            snake_y=snake_y+velocity_y



            if abs(snake_x-food_x)<15 and abs(snake_y-food_y)<15:
                score=score+10
                food_x = random.randint(0, screen_width/2)
                food_y = random.randint(0, screen_height/2)
                snake_length+=5
                if score>int(hiscore):
                    hiscore=score
                    with open("hiscore.txt", "w") as f:
                        f.write(str(hiscore))

            gameWindow.fill(white)
            screen_score("score "+str(score)+"  Highscore "+str(hiscore),red,5,5)

            pygame.draw.rect(gameWindow,red,[food_x,food_y,snake_size,snake_size])
            head=[]
            head.append(snake_x)
            head.append(snake_y)

            snk_list.append(head)

            if len(snk_list)>snake_length:
                del snk_list[0]
            if head in snk_list [:-1]:
                game_over=True
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over=True

            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()
        hiscore = f.read()

    exit_game = False
    game_over = False
    snake_x = 55
    snake_y = 40
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snake_length = 1
    snake_size = 20
    fps = 60
    init_velocity = 5
    food_x = random.randint(0, screen_width / 2)
    food_y = random.randint(0, screen_height / 2)
    score = 0

    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            screen_score("game over press enter to play again",red,300,300)
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()
        else:
            for event in pygame.event.get():
                #print(event)
                if event.type==pygame.QUIT:
                    exit_game = True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x=init_velocity
                        velocity_y =0
                    if event.key==pygame.K_LEFT:
                        velocity_x=-init_velocity
                        velocity_y = 0
                    if event.key==pygame.K_UP:
                        velocity_y=-init_velocity
                        velocity_x =0
                    if event.key==pygame.K_DOWN:
                        velocity_y=init_velocity
                        velocity_x =0
                    if event.key==pygame.K_q:
                        score=score+10
            snake_x=snake_x+velocity_x
            snake_y=snake_y+velocity_y



            if abs(snake_x-food_x)<15 and abs(snake_y-food_y)<15:
                score=score+10
                food_x = random.randint(0, screen_width/2)
                food_y = random.randint(0, screen_height/2)
                snake_length+=5
                if score>int(hiscore):
                    hiscore=score
                    with open("hiscore.txt", "w") as f:
                        f.write(str(hiscore))

            gameWindow.fill(white)
            screen_score("score "+str(score)+"  Highscore "+str(hiscore),red,5,5)

            pygame.draw.rect(gameWindow,red,[food_x,food_y,snake_size,snake_size])
            head=[]
            head.append(snake_x)
            head.append(snake_y)

            snk_list.append(head)

            if len(snk_list)>snake_length:
                del snk_list[0]
            if head in snk_list [:-1]:
                game_over=True
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over=True

            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()
