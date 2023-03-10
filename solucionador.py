import random


def index_zero(config):
    for index in range(len(config)):
        if config[index] == 0:
            return index


def move_peca(config, direcao):
    index_vazio = index_zero(config)
    novo_estado = config.copy()
    if direcao == 'a':
        if index_vazio % 3 != 0:
            novo_estado[index_vazio], novo_estado[index_vazio -
                                                  1] = novo_estado[index_vazio - 1], novo_estado[index_vazio]

    if direcao == 'd':
        if index_vazio % 3 != 2:
            novo_estado[index_vazio], novo_estado[index_vazio +
                                                  1] = novo_estado[index_vazio + 1], novo_estado[index_vazio]

    if direcao == 'w':
        if index_vazio > 2:
            novo_estado[index_vazio], novo_estado[index_vazio -
                                                  3] = novo_estado[index_vazio - 3], novo_estado[index_vazio]

    if direcao == 's':
        if index_vazio < 6:
            novo_estado[index_vazio], novo_estado[index_vazio +
                                                  3] = novo_estado[index_vazio + 3], novo_estado[index_vazio]

    return novo_estado


def insere_chave_nova_min_heap(heap, tam, chave):
    heap.append(chave)
    aumentar_chave(heap, tam, chave)


def aumentar_chave(heap, pos, novo):
    if novo.f <= heap[pos].f:
        heap[pos] = novo
        while pos > 0 and heap[(pos-1)//2].f > heap[pos].f:
            heap[pos], heap[(pos-1)//2] = heap[(pos-1)//2], heap[pos]
            pos = (pos-1)//2


class Solucionador:
    def __init__(self, estado, passos, passado):
        self.estado = estado
        self.g = passos
        self.h = self.calcula_h()
        self.f = self.g + self.h
        self.passado = passado

    def calculaQuantidadeDeInversoes(self):
        num_inversoes = 0
        for i in range(len(self.estado)):
            for j in range(i + 1, len(self.estado)):
                if self.estado[i] != 0 and self.estado[j] != 0:
                    if (self.estado[i] > self.estado[j]):
                        num_inversoes += 1

        return num_inversoes

    def calcula_h(self):
        h = 0
        for index in self.estado:
            if self.estado[index] != 0:
                if self.estado[index] != index:
                    h = h + 1
        return h

    def transicoes(self):
        p = self.passado
        p.append(self.estado)
        transicoes = list(filter(lambda e: e.calculaQuantidadeDeInversoes() % 2 == 0, [Solucionador(move_peca(self.estado, "a"), self.g+1, p),
                                                                                       Solucionador(
                                                                                           move_peca(self.estado, "d"), self.g+1, p),
                                                                                       Solucionador(
                                                                                           move_peca(self.estado, "w"), self.g+1, p),
                                                                                       Solucionador(move_peca(self.estado, "s"), self.g+1, p)]))

        return transicoes

    def BuscaInformada(self):
        agenda = []
        agenda.append(self)

        passados = {self}
        estado = self
        while len(agenda) > 0:
            estado = agenda.pop(0)
            if estado.estado == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                self.passado.append(estado.estado)
                return estado
            transi = estado.transicoes()

            if len(transi) == 0:  # se nao houver transicao para o estado
                return None

            for transicao in transi:
                proximo = transicao
                if proximo not in passados and proximo not in agenda:
                    insere_chave_nova_min_heap(
                        agenda, len(agenda), proximo)
                    passados.add(proximo)

        return None

    def __hash__(self):  # para o set conseguir guardar um objeto
        return hash(self.g)

    def __eq__(self, other):  # para o set conseguir diferenciar objetos (nao inserir elementos repetidos)
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.estado == other.estado

    def __lt__(self, other):
        return self.f < other.f

    def __repr__(self):
        return "{}".format(self.estado)


def cria_aleatorio():

    lista = list(range(0, 9))
    random.shuffle(lista)
    return Solucionador(lista, 0)


def make_matrix(lis):
    m = []
    for i in range(3):
        m.append([])
        for j in range(3):
            m[i].append(lis[(i*3) + j])
    return m
