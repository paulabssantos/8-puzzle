import pygame
import random
from settings import *
import sprite

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(title)

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.tiles_grid = self.create_game()
        self.tiles_grid_completed = self.create_game()
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
        pygame.display.flip()


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

            # if event.type == pygame.KEYDOWN:
            #     for row, tiles in enumerate(self.tiles):
            #         for col, tile in enumerate(tiles):

            #             if event.key == pygame.K_LEFT:
            #                 print("Apertou pra Esqueda")

            #             elif event.key == pygame.K_RIGHT:
            #                 print("Apertou pra Direita")

            #             elif event.key == pygame.K_UP:
            #                 print("Apertou pra Cima")

            #             elif event.key == pygame.K_DOWN:
            #                 print("Apertou pra Baixo")
            
                

game = Game()

while True:
    game.new()
    game.run()