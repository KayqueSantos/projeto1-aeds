# -*- coding: cp1252 -*-
'''
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
IF969 - Algoritmos e Estruturas de Dados

Autor: Kayque Lucas Santana dos Santos
Email: klss@cin.ufpe.br
Data: 2018-09-29

Descrição:  Algoritmo para implementação do objeto árvore trie.

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
        Adiciona elementos à árvore trie, sendo a chave um objeto iterável, e o valor um objeto qualquer.
        '''
        no=self.__raiz
        for letra in chave:
            encontrado=False
            #procurar pela letra entre os filhos do no atual
            if(no.filhos==None):
                novoNo=TrieNo(letra, Lista(), {})
                no.filhos[letra]=novoNo
                no=novoNo
                encontrado=True
            if(letra in no.filhos):
                #se a letra é encontrada, apontamos o no para o filho que contem a letra
                no=no.filhos[letra]
                encontrado=True
            if(not encontrado):
                #se a letra não é encontrada em nenhum dos filhos do nó atual, criamos um novo nó com a letra e apontamos para ele
                novoNo=TrieNo(letra, Lista(), {})
                no.filhos[letra]=novoNo
                no=novoNo
        #ao finalizar a busca, chegamos ao nó correspondente à última letra da chave, e nele guardamos o valor
        if((not valor in no.valor)):
            no.valor.inserir(valor)
    
    def busca(self, chave):
        '''
        Busca e retorna o valor guardado na chave passada como parâmetro.
        '''
        no=self.__raiz
        for letra in chave:
            encontrado=False
            if(letra in no.filhos):
                no=no.filhos[letra]
                encontrado=True
        if(not encontrado):
            return None
        return no.valor
