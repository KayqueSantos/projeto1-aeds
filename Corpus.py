# -*- coding: cp1252 -*-
'''
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Inform�tica (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informa��o
IF969 - Algoritmos e Estruturas de Dados

Autor: Kayque Lucas Santana dos Santos
Email: klss@cin.ufpe.br
Data: 2018-10-08

Descri��o:  Algoritmo para implementa��o do objeto Corpus.

Copyright(c) 2018 Kayque Lucas Santana dos Santos
'''
from ListaEncadeada import ListaEnc as Lista
from Documento import Documento
from NGrama import NGrama
from ArvoreTrie import ArvoreTrie
import os


class Corpus:
    '''
    A classe Corpus armazena uma lista de objetos do tipo Documento.
    '''

    def __init__(self, diretorio):
        '''
        Objeto Corpus. Input: endere�o de uma pasta contendo arquivos de texto.        
        '''
        dirs=os.listdir(diretorio)
        self.__documentos=Lista()
        for arquivo in dirs:
            self.__documentos.inserir(Documento(diretorio+'\\'+arquivo))
        self.__TrieNGramas=self.__gerarTrie()
        
    def __gerarTrie(self):
        '''
        Adiciona todos os NGramas de todos os documentos como chaves da �rvore trie, e adiciona para cada NGrama uma refer�ncia para lista de documentos � qual pertence.
        '''
        trie=ArvoreTrie()
        for doc in self.__documentos:
            for ngrama in doc.getNGramas():
                trie.add(ngrama, doc)
        return trie
    
    def verificarPlagio(self, documentoSuspeito, limiar):
        '''
        Recebe um documento e um limiar de conten��o como par�metros e retorna uma lista ordenada dos documentos mais prov�veis de
        terem servido de base para o pl�gio.
        '''
        listaPlagio=Lista()
        contencaoDocumentos=self.__buscarNGramas(documentoSuspeito.getNGramas())
        for doc in contencaoDocumentos:
            if(contencaoDocumentos[doc]/len(documentoSuspeito.getNGramas()))>limiar:
                listaPlagio.inserir(doc)
        return listaPlagio
    
    def __buscarNGramas(self, listaNGramas):
        '''
        Recebe uma lista de NGramas e retorna um dicion�rio contendo para cada documento do corpus, a quantidade de NGramas iguais ao do documento suspeito.
        '''
        documentos={}
        for NGrama in listaNGramas:
            busca=self.__TrieNGramas.busca(NGrama)
            if(busca):
                for doc in busca:
                    if(not doc in documentos):
                        documentos[doc]=0
                    else:
                        documentos[doc]+=1
        return documentos
