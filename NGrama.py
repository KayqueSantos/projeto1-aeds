# -*- coding: cp1252 -*-
"""
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
IF969 - Algoritmos e Estruturas de Dados

Autor: Kayque Lucas Santana dos Santos
Email: klss@cin.ufpe.br
Data: 2018-09-29

Descrição:  Algoritmo para implementação do objeto n-grama.

Copyright(c) 2018 Kayque Lucas Santana dos Santos
"""

import numpy as np

class NGrama:
    '''
    A classe NGrama é uma estrutura que armazena uma sequência de n palavras.
    '''
    def __init__(self, doc, inicio, fim):
        '''
        Objeto NGrama. Input: qualquer conjunto de palavras em forma de lista ou tupla.
        '''
        self.__doc=doc
        self.__palavras=np.array([inicio, fim])
        
    def __str__(self):
        return str(self.__palavras)
    
    def __repr__(self):
        return "nGrama (%s)"%(self.__palavras)
    
    def __eq__(self, other):
        '''
        Compara o objeto do tipo NGrama com outro Ngrama, e retorna True se todas as palavras da sequência de cada objeto são iguais.
        '''
        return (self.__palavras==other.__palavras).all()==True
    
    def __getitem__(self, index):
        if(index<len(self.__palavras)):
            palavra=self.__palavras[index]
            return palavra
        else:
            raise IndexError(index)
    
    def __iter__(self):
        self.__index=0
        return self
    
    def __next__(self):
        if self.__index>=len(self.__palavras):
            raise StopIteration
        palavra = self.__palavras[self.__index]
        self.__index+=1
        return palavra
    
    def getPalavras(self):
        return (self.__palavras)
    
    def getDoc(self):
        return (self.__doc)
