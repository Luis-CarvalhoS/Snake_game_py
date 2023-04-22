# Importa a biblioteca Pygame para criar o jogo e a função randrange da biblioteca random para gerar números aleatórios
import pygame as pg  
from random import randrange  

# Define o tamanho da janela do jogo e o tamanho das células que formam a cobra e a comida
WINDOW = 1000  
TILE_SIZE = 50  

# Define uma faixa de valores dentro da janela para a cobra e a comida
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)  

# Define uma função que retorna uma posição aleatória dentro da faixa definida
get_random_position = lambda: [randrange(*RANGE), randrange(*RANGE)]  

# Cria um objeto de retângulo para representar a cobra
snake = pg.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])  

# Define a posição inicial da cobra aleatoriamente e define o tamanho inicial da cobra
snake.center = get_random_position()  
lenght = 1  

# Cria uma lista de segmentos da cobra, adicionando o objeto snake à lista
segments = [snake.copy()]  

# Cria um objeto de retângulo para representar a comida e define sua posição aleatoriamente
food = snake.copy()  
food.center = get_random_position()  

# Define a direção inicial da cobra e o intervalo de tempo entre cada atualização de tela
snake_dir = (0, 0)  
time, time_step = 0, 110  

# Inicializa o Pygame, define o tamanho da tela do jogo e o relógio
pg.init()  
screen = pg.display.set_mode([WINDOW] * 2)  
clock = pg.time.Clock()  

# Define um dicionário para armazenar as teclas pressionadas e as direções correspondentes
dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1 }  

# Carrega a imagem de fundo do jogo
background_image = pg.image.load("snake.jpg").convert()

# Inicialização do loop principal
while True:
    # Verifica eventos de teclado e saída
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            # Muda a direção da cobra de acordo com a tecla pressionada
            if event.key == pg.K_w and [pg.K_w]:
                snake_dir = (0, -TILE_SIZE)
                dirs = {pg.K_w: 1, pg.K_s: 0, pg.K_a: 1, pg.K_d: 1}
            if event.key == pg.K_s and [pg.K_s]:
                snake_dir = (0, TILE_SIZE)
                dirs = {pg.K_w: 0, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}
            if event.key == pg.K_a and [pg.K_a]:
                snake_dir = (-TILE_SIZE, 0)
                dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 0}
            if event.key == pg.K_d and [pg.K_d]:
                snake_dir = (TILE_SIZE, 0)
                dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 0, pg.K_d: 1 }
    
    # Desenha o fundo na tela
    screen.blit(background_image, [0, 0])
    
    # Verifica se a cobra colidiu consigo mesma ou com as bordas da tela
    self_eating = pg.Rect.collidelist(snake, segments[:-1]) != -1
    if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW or self_eating:
        # Se sim, reinicia a cobra e a comida
        snake.center, food.center = get_random_position(), get_random_position()
        lenght, snake_dir = 1, (0,0)
        segments = [snake.copy()]
    
    # Verifica se a cobra comeu a comida
    if snake.center == food.center:
        # Se sim, gera uma nova posição para a comida e aumenta o tamanho da cobra
        food.center = get_random_position()
        lenght += 1
    
    # Desenha a comida e a cobra na tela
    pg.draw.rect(screen, 'yellow', food)
    [pg.draw.rect(screen, 'purple', segment) for segment in segments]
    
    # Move a cobra a cada intervalo de tempo
    time_now = pg.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments[-lenght:]
    
    # Atualiza a tela e define a taxa de quadros
    pg.display.flip()
    clock.tick(60)

