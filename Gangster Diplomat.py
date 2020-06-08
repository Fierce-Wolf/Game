import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))  # Create a window
pygame.display.set_caption('Gangster Diplomat')  # Give name of the application

# Loading sprites:

# Sprites walk to right
walkRight = [
	pygame.image.load('right_1.png'), 
	pygame.image.load('right_2.png'), 
	pygame.image.load('right_3.png'), 
	pygame.image.load('right_4.png'), 
	pygame.image.load('right_5.png')
]

# Sprites walk to left
walkLeft = [
	pygame.image.load('left_1.png'), 
	pygame.image.load('left_2.png'), 
	pygame.image.load('left_3.png'), 
	pygame.image.load('left_4.png'), 
	pygame.image.load('left_5.png')
]

bg = pygame.image.load('bg.jpg')	# Background

# This is where the sprite of the player standing still is stored
playerStand = pygame.image.load('idle.png')	

# INITIAL COORDINATES OF PLAYER
x = 50
y = 425

# Player parameters
width = 60  # Ширина
height = 71  # Высота
speed = 5  # Скорость

# Game physics parameters
isJump = False	# Jump status (the player jumped or DIDN't jump)
jumpCount = 10 # This variable determines the height of the jump

# For animating objects:
Left = False
Right = False
animCount = 0

clock = pygame.time.Clock()


def draw_window():
	'''This function redraws and updates the game window
	During each iteration of the game cycle
	'''
	global animCount
	global isJump
	global jumpCount
	global x
	global y

	win.blit(bg, (0, 0)) # Displaying the background image on our window
	
	jumping()

	# Create the animation of the game
	if (animCount + 1) >= 25:
		animCount = 0

	
	if Left:
		win.blit(walkLeft[animCount // 5], (x, y))
		animCount += 1

	elif Right:
		win.blit(walkRight[animCount // 5], (x, y))
		animCount += 1
	else:
		win.blit(playerStand, (x, y))

	pygame.display.update()  # Обновляем окно игры
	isJump = False


def jumping():
	'''Jump function'''
	global jumpCount
	global isJump
	global y

	if isJump:
		y += jumpCount
	else:
		y -= jumpCount



# Создаем игровой цикл
my_game = True
while my_game:
	clock.tick(25)	# fps

	# ↓ Этот цикл (for) обрабатывает все игровые события.
	# Но в данном случае, нам нужен только один тип событий.
	for event in pygame.event.get():
		# Если юзер нажал на 'красный крестик' в углу окна приложения, то
		if event.type == pygame.QUIT:
            # Приложение закрывается т.к цикл больше не выполняется
			my_game = False

	keys = pygame.key.get_pressed()
	# Move left
	if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and x > 5:
		x -= speed

		Left = True
		Right = False

	# Move right
	elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and x < (500 - width - 5):
		x += speed

		Left = False
		Right = True

	else:
		Left = False
		Right = False


	if keys[pygame.K_SPACE]:
		isJump = True

	draw_window()

pygame.quit()
