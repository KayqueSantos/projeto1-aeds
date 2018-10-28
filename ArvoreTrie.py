# -*- coding: cp1252 -*-
'''
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Inform�tica (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informa��o
IF969 - Algoritmos e Estruturas de Dados

Autor: Kayque Lucas Santana dos Santos
Email: klss@cin.ufpe.br
Data: 2018-09-29

Descri��o:  Algoritmo para implementa��o do objeto �rvore trie.

Copyright(c) 2018 Kayque Lucas Santana dos Santos
'''
from ListaEncadeada import ListaEnc as Lista

class TrieNo:
    
    def __init__(self, chave=None, valor=Lista(), filhos={}):
        self.chave=chave
        self.valor=valor
        self.filhos=filhos

class ArvoreTrie:
    
    def __init__(self):
        self.__raiz=TrieNo()
    
    def add(self, chave, valor):
        '''
        Adicionando elementos � �rvore trie.
        '''
        no=self.__raiz
        for palavra in chave:
            encontrado=False
            #procurar pela palavra entre os filhos do no atual
            if(no.filhos==None):
                novoNo=TrieNo(palavra, Lista(), {})
                no.filhos[palavra]=novoNo
                no=novoNo
                encontrado=True
            if(palavra in no.filhos):
                #se a palavra � encontrada, apontamos o no para o filho que contem a palavra
                no=no.filhos[palavra]
                encontrado=True
            if(not encontrado):
                #se a palavra n�o � encontrada em nenhum dos filhos do n� atual, criamos um novo n� com a palavra e apontamos para ele
                novoNo=TrieNo(palavra, Lista(), {})
                no.filhos[palavra]=novoNo
                no=novoNo
        #ao finalizar a busca, chegamos ao n� correspondente ao ultimo elemento da chave, e nele guardamos o valor
        if((not valor in no.valor)):
            no.valor.inserir(valor)
    
    def busca(self, chave):
        no=self.__raiz
        for palavra in chave:
            encontrado=False
            for filho in no.filhos:
                if(palavra==filho):
                    no=no.filhos[palavra]
                    encontrado=True
                    break
        if(not encontrado):
            return None
        return no.valor
