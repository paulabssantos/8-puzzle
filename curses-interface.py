import curses
from solucionador import *
import time


class Game:
    def __init__(self):
        self.menu = ['R - Resolver', 'E - Embaralhar', 'Esc - Sair']
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
                    self.lista = element
                    for i in range(3):
                        for j in range(3):
                            self.stdscr.addstr(i+5, j*(4+2) + 10+1,
                                               "%*d " % (2, matriz[i][j]))

                return None

    def make_matrix(lis):
        m = []
        for i in range(3):
            m.append([])
            for j in range(3):
                m[i].append(lis[(i*3) + j])
        return m

    def print_menu(self):
        self.stdscr.clear()
        for idx, row in enumerate(self.menu):
            x = self.screen_width // 2 - len(row) // 2
            y = self.screen_height // 2 - len(self.menu) // 2 + idx
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
        self.print_menu()
        self.lista = self.lista_inicial()
        self.imprime_matriz(self.lista)

        while 1:
            key = stdscr.getch()
            # Se selecionou E de embaralhar
            if int(key) == 101:
                self.lista = self.cria_aleatorio()
                self.imprime_matriz(self.lista)

            # Se selecionou o R de resolver
            elif int(key) == 114:
                self.resolver(self.lista)

            # Se selecionou o Esc de sair
            elif int(key) == 27:
                break

            elif key == curses.KEY_UP:
                new_lista = move_peca(self.lista, 'w')
                self.lista = new_lista

            elif key == curses.KEY_LEFT:
                new_lista = move_peca(self.lista, 'a')
                self.lista = new_lista

            elif key == curses.KEY_RIGHT:
                new_lista = move_peca(self.lista, 'd')
                self.lista = new_lista

            elif key == curses.KEY_DOWN:
                new_lista = move_peca(self.lista, 's')
                self.lista = new_lista

            self.print_menu()
            self.imprime_matriz(self.lista)

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
