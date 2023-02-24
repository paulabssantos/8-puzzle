import pygame
import random
from settings import *
from solucionador import *
import sprite
import time

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(title)

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.tiles_grid = make_matrix([0,1,2,3,4,5,6,7,8])
        self.tiles_grid_completed = self.create_game()
        self.buttons_list = [
            sprite.Button(500, 100, 200, 50, "Novo Jogo", WHITE, BLACK),
            sprite.Button(500, 175, 200, 50, "Resolver", WHITE, BLACK)
        ]
        self.draw_tiles()

    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
       

    def create_game(self):
        # uma matriz contendo os valores
        grid = []
        number = 0
        for x in range(GAME_SIZE):
            grid.append([])
            for _ in range(GAME_SIZE):
                grid[x].append(number)
                number += 1
        return grid

    def draw_tiles(self):
        self.tiles = []
        for row, x in enumerate(self.tiles_grid):
            self.tiles.append([])
            for col, tile in enumerate(x):
                self.tiles[row].append(sprite.Tile(self, col, row, str(tile)))


    def draw_grid(self):
        for row in range(-1, GAME_SIZE * TILESIZE, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (row, 0), (row, GAME_SIZE * TILESIZE))
        for col in range(-1, GAME_SIZE * TILESIZE, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (0, col), (GAME_SIZE * TILESIZE, col))

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BGCOLOUR)
        self.all_sprites.draw(self.screen)
        self.draw_grid()
        for button in self.buttons_list:
            button.draw(self.screen)
        pygame.display.flip()

    ## Essa aqui é a lógica de atualizar o valor da tela de acordo com uma matriz passada
    def change_frame(self, matrix):
        self.all_sprites = pygame.sprite.Group()
        self.tiles_grid = matrix
        self.tiles_grid_completed = self.create_game()
        self.draw_tiles()

    def get_array(self):   
        arr = []
        for line in self.tiles:
            for element in line:
                arr.append(int(element.text))
        return arr


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for row, tiles in enumerate(self.tiles):
                    for col, tile in enumerate(tiles):
                        if tile.click(mouse_x, mouse_y):
                            if tile.right() and self.tiles_grid[row][col + 1] == 0:
                                self.tiles_grid[row][col], self.tiles_grid[row][col + 1] = self.tiles_grid[row][col + 1], self.tiles_grid[row][col]

                            if tile.left() and self.tiles_grid[row][col - 1] == 0:
                                self.tiles_grid[row][col], self.tiles_grid[row][col - 1] = self.tiles_grid[row][col - 1], self.tiles_grid[row][col]

                            if tile.up() and self.tiles_grid[row - 1][col] == 0:
                                self.tiles_grid[row][col], self.tiles_grid[row - 1][col] = self.tiles_grid[row - 1][col], self.tiles_grid[row][col]

                            if tile.down() and self.tiles_grid[row + 1][col] == 0:
                                self.tiles_grid[row][col], self.tiles_grid[row + 1][col] = self.tiles_grid[row + 1][col], self.tiles_grid[row][col]

                            self.draw_tiles()

                for button in self.buttons_list:
                    if button.click(mouse_x, mouse_y):
                        if button.text == "Novo Jogo":
                            self.new()
                        if button.text == "Resolver":
                            #    Gerar um array com a combinacao atual
                            arr = self.get_array()
                            print("Calculando solução...")
                           #    Gerar um solucionador
                            solucionador = Solucionador(arr, 0, [])
                            #   Chamar a funcao que resolve
                            a = solucionador.BuscaInformada()
                             #   pegar o retorno
                            if a is None:
                                print("Estado não solucionável")
                            else:
                                if a.passado is None:
                                    print("passado ta vazio")
                                else:
                                    for element in a.passado:
                                        print("Nova Matriz")
                                        for lin in make_matrix(element):
                                            print(lin)
                        

                        
                       
                        #   chamar um a um no change_frame
                            # for element in matrizes:
                            #     self.change_frame(element)
                            #     time.sleep(1)
            

def make_matrix(lis):
    m = []
    for i in range(GAME_SIZE):
        m.append([])
        for j in range(GAME_SIZE):
            m[i].append(lis[(i*GAME_SIZE) + j])
    return m

def cria_aleatorio():
    lista = list(range(0,9))
    random.shuffle(lista)
    return lista

game = Game()

while True:
    game.new()
    game.run()