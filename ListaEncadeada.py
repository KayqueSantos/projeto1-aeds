# -*- coding: cp1252 -*-
'''
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
IF969 - Algoritmos e Estruturas de Dados

Autor: Kayque Lucas Santana dos Santos
Email: klss@cin.ufpe.br
Data: 2018-09-29

Descrição:  Algoritmo para implementação do objeto lista encadeada.

Copyright(c) 2018 Kayque Lucas Santana dos Santos
'''

from NGrama import NGrama
 
class No:
    def __init__(self, item=None, prox=None):
        self.item= item
        self.prox= prox
    
class ListaEnc:
    def __init__(self):
        self.__primeiro=self.__ultimo=No()
    
 
    def __iter__(self):
        self.__ponteiro=Ponteiro(self)
        return self.__ponteiro
                
    def __getitem__(self, index):
        if(self.vazia()):
            return None
        aux=self.__primeiro.prox
        cont=0
        while(cont<index and aux!=None):
            aux=aux.prox
            cont+=1
        if(aux==None):
            return IndexError(index)
        return aux.item
    
    def __str__(self):
        string="["
        aux=self.__primeiro.prox
        while(aux.prox!=None):
            string+=str(aux.item)+','
            aux=aux.prox
        string+=str(aux.item)+"]"
        return string
    
    def __repr__(self):
        string="("
        aux=self.__primeiro.prox
        while(aux.prox!=None):
            string+=str(aux.item)+','
            aux=aux.prox
        string+=str(aux.item)+")"
        return 'ListaEncadeada'+string
    
    def __len__(self):
        cont=0
        aux=self.__primeiro.prox
        while(aux!=None):
            cont+=1
            aux=aux.prox
        return cont
    
    def inserir(self, item):
        '''Insere um valor no final da lista.'''
        self.__ultimo.prox=No(item,None)
        self.__ultimo=self.__ultimo.prox
        
    def inserirInicio(self, item):
        '''Insere um valor no início da Lista.'''
        self.__primeiro.prox=No(item,self.__primeiro.prox)
        if(self.vazia()):
            self.__ultimo=self.__primeiro.prox
            
    def inserirOrdenado(self, item):
        '''Insere um valor ordenadamente na lista.'''
        if(self.vazia()):
            self.inserir(item)
        else:
            ante=self.__primeiro
            atual=self.__primeiro.prox
            while(atual!=None and atual.item<item):
                ante=atual
                atual=ante.prox
            ante.prox=No(item,atual)
            if (atual is None):
                self.__ultimo=ante.prox
                  
    def pesquisa(self, item):
        '''Pesquisa uma posição na lista pelo item.'''
        aux=self.__primeiro.prox
        while (aux!=None and aux.item!=item):
            aux=aux.prox
        if(aux is None):
            return "Valor não encontrado."
        else:
            return aux.item

    def removerInicio(self):
        '''Remove a  primeira posição da lista e retorna o item guardado nela.'''
        if(self.vazia()):
            return None
        aux=self.__primeiro.prox
        self.__primeiro.prox=aux.prox
        item=aux.item
        if(self.__ultimo==aux):
            self.__ultimo=self.__primeiro
        aux.prox = None
        del aux
        return item

    def removerFim(self):
        '''Remove a última posição da lista e retorna o item guardado nela.'''
        if(self.vazia()):
            return None
        aux=self.__primeiro.prox
        while(aux.prox!=self.__ultimo):
            aux=aux.prox
        self.__ultimo=aux
        aux=aux.prox
        self.__ultimo.prox=None
        item=aux.item
        del aux
        return item

    def removerItem(self, item):
        '''Remove na lista a primeira ocorrência do valor recebido como parâmetro.'''
        if(self.vazia()):
            raise ValueError(item)
        aux=self.__primeiro
        while(aux.prox!=None and aux.prox.item!=item):
            aux=aux.prox
        print(aux.prox.item)
        if(aux.prox==None):
            raise ValueError(item)
        item=aux.prox.item
        tmp=aux.prox
        aux.prox=tmp.prox
        if(aux.prox is None):
            self.__ultimo=aux
        del tmp
        del aux
        return item
        
    def vazia(self):
        '''Retorna valor verdade sobre a lista estar vazia.'''
        return self.__primeiro==self.__ultimo
    
    def getPrimeiro(self):
        return self.__primeiro.prox
    
    def getUltimo(self):
        return self.__ultimo
    
        
class Ponteiro:
    def __init__(self, objetoIter):
        self.posicaoAtual=objetoIter.getPrimeiro()

    def __next__(self):
        if(self.posicaoAtual==None):
            raise StopIteration
        else:
            aux=self.posicaoAtual.item
            self.posicaoAtual=self.posicaoAtual.prox
            return aux
            
            
            