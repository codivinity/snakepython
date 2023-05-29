import pygame
import random


class GAME:
    def __init__(self):
        pygame.init()

        # Screen size      # 1
        self.display_width = 600
        self.display_height = 400

        # Colors
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (213, 50, 80)
        self.green = (0, 255, 0)
        self.green_head = (0, 140, 0)
        self.blue = (50, 153, 213)

        # Initialize the game display
        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('Snake Game')

        # Set the clock
        self.clock = pygame.time.Clock()

        # Set the block size
        self.block_size = 10

        # Set the font for the score display
        self.font = pygame.font.SysFont(None, 30)

    def message_to_screen(self, msg, color):
        screen_text = self.font.render(msg, True, color)
        self.gameDisplay.blit(screen_text, [self.display_width / 6, self.display_height / 2])

    def game(self, ):  #      2
        gameExit = False
        gameOver = False

        # Set the starting position of the snake
        lead_x = self.display_width / 2
        lead_y = self.display_height / 2

        # Set the change in position of the snake
        lead_x_change = 0
        lead_y_change = 0

        # Set the initial length of the snake
        snakeList = []
        snakeLength = 1

        # Set the position of the food
        randAppleX = round(random.randrange(0, self.display_width - self.block_size) / 10.0) * 10.0
        randAppleY = round(random.randrange(0, self.display_height - self.block_size) / 10.0) * 10.0

        # Main game loop
        while not gameExit:

            # Game over loop
            while gameOver == True:
                # gameDisplay.fill(white)
                self.message_to_screen("Game over, press C to play again or Q to quit", self.red)
                pygame.display.update()

                # Check for player input
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            gameExit = True
                            gameOver = False
                        if event.key == pygame.K_c:
                            self.gameLoop()

            # Check for player input      # ask chat-gpt
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and lead_x_change != self.block_size:
                        lead_x_change = -self.block_size
                        lead_y_change = 0
                    elif event.key == pygame.K_RIGHT and lead_x_change != -self.block_size:
                        lead_x_change = self.block_size
                        lead_y_change = 0
                    elif event.key == pygame.K_UP and lead_y_change != self.block_size:
                        lead_y_change = -self.block_size
                        lead_x_change = 0
                    elif event.key == pygame.K_DOWN and lead_y_change != -self.block_size:
                        lead_y_change = self.block_size
                        lead_x_change = 0

            # Check if the snake hits the wall
            if lead_x < 0:
                lead_x = self.display_width - self.block_size
            elif lead_x >= self.display_width:
                lead_x = 0
            elif lead_y < 0:
                lead_y = self.display_height - self.block_size
            elif lead_y >= self.display_height:
                lead_y = 0

            # Update the position of the snake
            lead_x += lead_x_change
            lead_y += lead_y_change

            # Fill the screen with white
            self.gameDisplay.fill(self.white)

            # Draw the food
            pygame.draw.rect(self.gameDisplay, self.red, [randAppleX, randAppleY, self.block_size, self.block_size])

            # Check if the snake hits itself
            snakeHead = []
            snakeHead.append(lead_x)
            snakeHead.append(lead_y)
            if snakeHead in snakeList[:-1]:
                gameOver = True

            snakeList.append(snakeHead)
            if len(snakeList) > snakeLength:
                del snakeList[0]

            # Draw the snake
            for segment in snakeList:
                if segment == snakeHead:
                    pygame.draw.circle(self.gameDisplay, self.green_head, [segment[0] + 5, segment[1] + 5], 7)
                else: # first this and run then the above if statement
                    pygame.draw.rect(self.gameDisplay, self.green,
                                     [segment[0], segment[1], self.block_size, self.block_size])

            # Update the score
            score = snakeLength
            scoreText = self.font.render("Score: " + str(score), True, self.black)
            self.gameDisplay.blit(scoreText, [0, 0])

            # Update the display
            pygame.display.update()

            # Check if the snake eats the food
            if lead_x == randAppleX and lead_y == randAppleY:
                randAppleX = round(random.randrange(0, self.display_width - self.block_size) / 10.0) * 10.0
                randAppleY = round(random.randrange(0, self.display_height - self.block_size) / 10.0) * 10.0
                snakeLength += 1

            # Set the speed of the game
            self.clock.tick(15)

        # Quit the game
        pygame.quit()
        quit()

g = GAME()
g.game()