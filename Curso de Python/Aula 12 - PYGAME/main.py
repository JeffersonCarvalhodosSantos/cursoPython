import pygame
from pygame.locals import *              # Importar todas os métodos do Pygame 
from sys import exit                     # Usuário fechar o jogo
from random import *


pygame.init()   # Iniciar o método/biblioteca

# Armazenando o diâmetro da tela
altura = 400
largura = 640
# Definindo posição
pos_x_retangulo = largura / 2
pos_y_retangulo = altura / 2
# Definindo altura do objeto 
largura_retangulo = 40
altura_retangulo = 40
# Definindo variaveis de posição e tamanho do círculo
pos_x_circulo = 40
pos_y_circulo = 40
raio_criculo = 10

# Definindo fonte
fonte = pygame.font.SysFont("Arial", 20, True, False)
pontos = 0

tela = pygame.display.set_mode((largura, altura))       # Criar a janela, só aceita tuplas

# Definir título da janela
pygame.display.set_caption("Criando Jogos")

# Modifica a taxa de atualização de pixels/segundo
relogio = pygame.time.Clock()

# Loop infinito
while True:
    relogio.tick(30)                              # Quanto maior o valor mais rapido fica o "PPS"
    tela.fill((0,0,0))                            # Para excluir o rastro de movimentação
    mensagem = f'Pontos: {pontos}'
    textoFormatado = fonte.render(mensagem, True,(0,255,0))
    for event in pygame.event.get():              # Adicionar eventos dentro do Pygame, todos.
        if event.type == QUIT:                    # Sair
            pygame.quit()
            exit()
            
        # if event.type == KEYDOWN:                 # Eventos de interação do usuário com o mouse
        #     if event.key == K_UP:                 # Eventos de interação do usuário com o teclado
        #         pos_y_retangulo -= 10
        #     if event.key == K_DOWN:
        #         pos_y_retangulo += 10
        #     if event.key == K_LEFT:
        #         pos_x_retangulo -= 10
        #     if event.key == K_RIGHT:
        #         pos_x_retangulo += 10
        
    if pygame.key.get_pressed()[K_w]:
        pos_y_retangulo -= 1
    elif pygame.key.get_pressed()[K_s]:
        pos_y_retangulo += 1
    elif pygame.key.get_pressed()[K_a]:
        pos_x_retangulo -= 1
    elif pygame.key.get_pressed()[K_d]:
        pos_x_retangulo += 1
                    
    circulo = pygame.draw.circle(tela, (255,255,0), (pos_x_circulo,pos_y_circulo), 10)         
    retangulo = pygame.draw.rect(tela, (255, 0, 0), (pos_x_retangulo,pos_y_retangulo,largura_retangulo,altura_retangulo))   # Criar forma geométrica e dentro dos parênteses o local onde será criado; segundo: parâmetro de valores de cor RGB;   
    
    if retangulo.colliderect(circulo):
        pos_x_circulo = randint(40,600)
        pos_y_circulo = randint(50,430)
        pontos += 1
    tela.blit(textoFormatado, (400,40))
# Atualizar o jogo a cada interação
    pygame.display.update()

