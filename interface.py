import pygame
import solucionador
import settings


class Puzzle:
  def __init__(self):
    self.x = 200
    self.y = 130
    self.start = int(10000)

  
  def inicia_jogo(self,janela):
    self.draw(janela)
    pygame.display.update()
    
  def draw(self, janela):
    font = pygame.font.SysFont("Arial",30)
    title = font.render("Mova as teclas A,W,S,D",True,(255,196,166))
    janela.blit(title,(180,20))

    for i in range(4):
      pygame.draw.line(janela,(160,52,110),(self.x-4, self.y+90*i),(self.x+5+3*90,self.y+90*i),5)
    for i in range(4):
      pygame.draw.line(janela,(109,22,90),(self.x+90*i, self.y),(self.x+90*i,self.y+3*90),5)	


class Interface:
    def __init__(self, altura, largura,puzzle):
        self.altura = altura
        self.largura = largura
        self.puzzle = puzzle
        self.janela = pygame.display.set_mode((self.largura,self.altura))
        self.nome_janela = pygame.display.set_caption("8Puzzle")
    
    def pega_evento(self):
        for evento in pygame.event.get():
            self.acao_evento(evento)

    def acao_evento(self,evento):
        if evento.type == pygame.QUIT:
            self.fecha_tela()

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_1:
                self.puzzle.inicia_jogo(self.janela)

    def fecha_tela(self):
        pygame.quit()
        exit()

    def inicia_tela(self):
        pygame.init()
        font = pygame.font.SysFont("Arial",60)
        titulo = font.render("8-Puzzle",True,(255,196,166))
        self.janela.blit(titulo,(220,20))    
       

        while True:
            self.pega_evento()
            pygame.display.update()

puzzle = Puzzle()
interface = Interface(480,640,puzzle)
interface.inicia_tela()