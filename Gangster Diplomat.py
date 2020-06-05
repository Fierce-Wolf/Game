import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))  # Создаем окно
pygame.display.set_caption('Gangster Diplomat')  # Даём название приложению

# Подгружаем спрайты:

# Спрайты ходьбы вправо
walkRight = [
	pygame.image.load('right_1.png'), 
	pygame.image.load('right_2.png'), 
	pygame.image.load('right_3.png'), 
	pygame.image.load('right_4.png'), 
	pygame.image.load('right_5.png')
]

# Спрайты ходьбы влево
walkLeft = [
	pygame.image.load('left_1.png'), 
	pygame.image.load('left_2.png'), 
	pygame.image.load('left_3.png'), 
	pygame.image.load('left_4.png'), 
	pygame.image.load('left_5.png')
]

bg = pygame.image.load('bg.jpg')

# Здесь хранится спрайт игрока, стоящего на месте
playerStand = pygame.image.load('idle.png')	

#  НАЧАЛЬНЫЕ КООРДИНАТЫ ИГРОКА
x = 50
y = 425

# Параметры игрока
width = 60  # Ширина
height = 71  # Высота
speed = 5  # Скорость

# Параметры физики игры
isJump = False	# Статус прыжка (игрук прыгнул или НЕ прыгнул)
jumpCount = 10 # От этой переменной зависит высота прыжка

# Для анимации объектов: 
Left = False
Right = False
animCount = 0

clock = pygame.time.Clock()

def draw_window():
	'''Это функция перерисовывает о обновляет игровое окно
	Во время каждой итерации игрового цикла
	'''
	win.blit(bg, (0, 0)) # Отображаем фоновый рисунак на нашем окне
	
	# Создаем анимацию игры
	global animCount
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
	# Движение влево
	if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and x > 5:
		x -= speed

		Left = True
		Right = False

	# Движение вправо
	if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and x < (500 - width - 5):
		x += speed

		Left = False
		Right = True

	if not(isJump):	# Если игрок не прыгнул

	   	# Прыжок
		if keys[pygame.K_SPACE]:
	   		isJump = True

	   	# Если игрок не движется
		else:
	   		Left = False
	   		Right = False
	   		animCount = 0

	# Если игрок прыгнул
	else:
		# Создаем физику прыжка
		if jumpCount >= -10:

			# ↓ Этот оператор нужен для того, чтобы игрок опускался вниз
			# после подъема вверх
			if jumpCount < 0:
				y += (jumpCount ** 2) / 2
			else:
				# Поднимаем игрока вверх
				y -= (jumpCount ** 2) / 2

			# Уменьшаем еденицу прыжка
			jumpCount -= 1

			# Таким образом игрок поднимется на одинаковое кол-во едениц
			# вверх и вниз => вверх = вниз

		# Прыжок 'окончен'
		else:
			# Возвращаем переменной isJump первоначальное значение,
			# чтобы юзер мог снова нажимать на клавиши и перемещаться
			isJump = False

			# Возвращаем переменной jumpCount старое значение едениц
			# высоты прыжка
			jumpCount = 10

	draw_window()

pygame.quit()
