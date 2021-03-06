from math import log2
from typing import List

from Dia import Dia


class ID3:

    def __init__(self):
        self.dias: List[Dia] = []
        self.backup: List[Dia] = self.dias

    @staticmethod
    def entropia(positivo, total):
        diferenca = total - positivo
        if diferenca == 0 or diferenca == total:
            return 0, total

        a = positivo / total
        b = diferenca / total
        return - a * log2(a) - b * log2(b), total

    def entropia_simp(self, lista):
        return self.entropia(self.soma_jogar_tenis(lista), len(lista))

    def ganho(self, lista_entropia):
        soma = 0
        for entropia_item in lista_entropia:
            soma += entropia_item[0] * entropia_item[1] / self.num_objetos
        return self.entropia_geral[0] - soma

    @staticmethod
    def soma_jogar_tenis(lista):
        return sum(x.jogarTenis == 'Sim' for x in lista)

    @property
    def num_objetos(self):
        return len(self.dias)

    @property
    def entropia_geral(self):
        return self.entropia(self.soma_jogar_tenis(self.dias), self.num_objetos)

    def entropia_by_str_name(self, nomes, obj_str):
        saida = []
        for item in nomes:
            lista = []
            for x in self.dias:
                if getattr(x, obj_str) == item:
                    lista.append(x)
            saida.append(self.entropia_simp(lista))
        return saida

    def entropia_perpectiva(self, nomes):
        return self.entropia_by_str_name(nomes, 'perspectiva')

    def entropia_temperatura(self, nomes):
        return self.entropia_by_str_name(nomes, 'temperatura')

    def entropia_umidade(self, nomes):
        return self.entropia_by_str_name(nomes, 'umidade')

    def entropia_vento(self, nomes):
        return self.entropia_by_str_name(nomes, 'vento')

    @staticmethod
    def raiz_arvore(lista_ganhos):
        return max(lista_ganhos)

    def arestas(self, raiz_nome):
        return self.unique([getattr(x, raiz_nome.lower()) for x in self.dias])

    @staticmethod
    def unique(lista):
        lista = list(set(lista))
        lista.sort()
        return lista

    def filtrar_dias_por_atributo(self, aresta):
        self.dias = self.backup
        if aresta != '':
            self.dias = [x for x in self.backup if x.perspectiva == aresta]

    @property
    def restaurar_dias(self):
        self.dias = self.backup
