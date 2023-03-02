import curses
from settings import *
from solucionador import *
import time


class Game:
    def __init__(self):
        self.menu = ['Resolver', 'Embaralhar', 'Exit']
        curses.wrapper(self.main)

    def resolver(self, arr):
        self.stdscr.clear()
        self.stdscr.refresh()
        #    Gerar um solucionador
        solucionador = Solucionador(arr, 0, [])
        #   Chamar a funcao que resolve
        a = solucionador.BuscaInformada()
        #   pegar o retorno
        if a is None:
            self.stdscr.addstr(10, 10, "Estado nao solucionavel")
            return None
        else:
            if a.passado is not None:
                for element in a.passado:
                    self.stdscr.refresh()
                    time.sleep(1)
                    ...
                    self.stdscr.clear()
                    matriz = make_matrix(element)
                    for i in range(3):
                        for j in range(3):
                            self.stdscr.addstr(i+5, j*(4+2) + 10+1,
                                               "%*d " % (2, matriz[i][j]))

                return None

    def make_matrix(lis):
        m = []
        for i in range(GAME_SIZE):
            m.append([])
            for j in range(GAME_SIZE):
                m[i].append(lis[(i*GAME_SIZE) + j])
        return m

    def print_menu(self, selected_row_idx):
        self.stdscr.clear()
        for idx, row in enumerate(self.menu):
            x = self.screen_width // 2 - len(row) // 2
            y = self.screen_height // 2 - len(self.menu) // 2 + idx
            if idx == selected_row_idx:
                self.stdscr.attron(curses.color_pair(1))
                self.stdscr.addstr(y, x, row)
                self.stdscr.attroff(curses.color_pair(1))
            else:
                self.stdscr.addstr(y, x, row)
        self.stdscr.refresh()

    def print_center(self, text):
        self.stdscr.clear()
        h, w = self.stdscr.getmaxyx()
        x = w//2 - len(text)//2
        y = h//2
        self.stdscr.addstr(y, x, text)
        self.stdscr.refresh()

    def main(self, stdscr):
        # turn off cursor blinking
        curses.curs_set(0)

        # color scheme for selected row
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

        self.stdscr = stdscr
        self.screen_height, self.screen_width = self.stdscr.getmaxyx()
        # specify the current selected row
        current_row = 0

        # print the menu
        self.print_menu(current_row)
        lista = self.lista_inicial()
        self.imprime_matriz(lista)

        while 1:
            key = stdscr.getch()

            if key == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(self.menu)-1:
                current_row += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                if self.menu[current_row] == "Resolver":
                    self.resolver(lista)
                elif self.menu[current_row] == "Embaralhar":
                    lista = self.cria_aleatorio()
                    self.imprime_matriz(lista)
                stdscr.getch()
                # if user selected last row, exit the program
                if current_row == len(self.menu)-1:
                    break

            self.print_menu(current_row)
            self.imprime_matriz(lista)

    def imprime_matriz(self, lista):
        matriz = make_matrix(lista)
        for i in range(3):
            for j in range(3):
                self.stdscr.addstr(i+5, j*(4+2) + 10+1,
                                   "%*d " % (2, matriz[i][j]))

    def lista_inicial(self):
        lista = [1, 4, 2, 3, 5, 8, 6, 7, 0]
        return lista

    def cria_aleatorio(self):
        lista = list(range(0, 9))
        random.shuffle(lista)
        return lista


game = Game()
