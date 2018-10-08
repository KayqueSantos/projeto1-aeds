# -*- coding: cp1252 -*-
"""
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
IF969 - Algoritmos e Estruturas de Dados

Autor: Kayque Lucas Santana dos Santos
Email: klss@cin.ufpe.br
Data: 2018-09-29

Descrição:  Algoritmo para implementação do objeto Documento.

Copyright(c) 2018 Kayque Lucas Santana dos Santos
"""

from NGrama import NGrama
from ListaEncadeada import ListaEnc as Lista
import numpy as np

class Documento:
    '''
    A classe documento armazena uma lista de palavras a partir de um arquivo.
    '''
    
    def __init__(self, arquivo):
        '''
        Objeto Documento. Input: endereço de um arquivo de texto.        
        '''
        self.__endereco=arquivo
        self.__vetorPalavras=self.__gerarVetorPalavras(arquivo)
        self.__listaNGramas=self.__gerarNgramas()
    
    def __str__(self):
        return 'Documento: %s \n %s' % (self.__endereco, str(self.__vetorPalavras))
    
    def __repr__(self):
        return 'Documento("'"%s"'")'%(self.__endereco)
        
    def contencao(self, other):
        contador=0
        for nGself in self.__listaNGramas:
            for nGother in other.__listaNGramas:
                if (nGself==nGother):
                    contador+=1
        return (contador/len(self.__listaNGramas))
        
    def __gerarVetorPalavras(self, arquivo):
        arq=open(arquivo, 'r', encoding="utf8")
        conteudo=arq.read()
        arq.close()
        lista=[]
        palavra=''
        for i in conteudo:
            if((i>='a' and i<='z') or (i>='A' and i<='Z') or (i>='1' and i<='9')):
                palavra+=i
            else:
                if(palavra!=''):
                    lista.append(palavra.lower())
                    palavra=''
        if(palavra!=''):
            lista.append(palavra)
        return np.asarray(lista)
    
    def __gerarNgramas(self,n=3):
        lista=Lista()
        for i in range(0,len(self.__vetorPalavras)-n):
            lista.inserir(NGrama(self.__vetorPalavras[i:i+n]))
        return lista
    
    def getVetorPalavras(self):
        return self.__vetorPalavras
    