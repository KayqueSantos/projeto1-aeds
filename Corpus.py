# -*- coding: cp1252 -*-
'''
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
IF969 - Algoritmos e Estruturas de Dados

Autor: Kayque Lucas Santana dos Santos
Email: klss@cin.ufpe.br
Data: 2018-10-08

Descrição:  Algoritmo para implementação do objeto Corpus.

Copyright(c) 2018 Kayque Lucas Santana dos Santos
'''
import os
from ListaEncadeada import ListaEnc as Lista
from Documento import Documento

class Corpus:
    '''
    A classe Corpus armazena uma lista de objetos do tipo Documento.
    '''

    def __init__(self, diretorio):
        '''
        Objeto Corpus. Input: endereço de uma pasta contendo arquivos de texto.        
        '''
        dirs=os.listdir(diretorio)
        self.__documentos=Lista()
        for arquivo in dirs:
            self.__documentos.inserir(Documento(diretorio+'\\'+arquivo))
    
    def 
        