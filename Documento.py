# -*- coding: cp1252 -*-
"""
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Inform�tica (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informa��o
IF969 - Algoritmos e Estruturas de Dados

Autor: Kayque Lucas Santana dos Santos
Email: klss@cin.ufpe.br
Data: 2018-09-29

Descri��o:  Algoritmo para implementa��o do objeto Documento.

Copyright(c) 2018 Kayque Lucas Santana dos Santos
"""

from NGrama import NGrama
from ListaEncadeada import ListaEnc
import numpy as np

class Documento:
    def __init__(self, arquivo):
        self.__vetorPalavras=self.__gerarVetorPalavras(arquivo)
        self.__listaNGramas=self.__gerarNgramas()
        
    def contencao(self, other):
        contador=0
        for nGself in self.__listaNGramas:
            for nGother in other.__listaNGramas:
                if (nGself==nGother):
                    contador+=1
        return (contador/len(self.__listaNGramas))
            
        
    def __gerarVetorPalavras(self, arquivo):
        arq=open(arquivo, 'r')
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
    
    def __gerarNgramas(self,n=3): #ver depois uma forma de implementar com o n din�mico
        lista=ListaEnc()
        for i in range(0,len(self.__vetorPalavras)-n):
            lista.inserir(NGrama(self.__vetorPalavras[i:i+n]))
        return lista
    
    def getVetorPalavras(self):
        return self.__vetorPalavras
    
          