# -*- coding: cp1252 -*-
"""
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
IF969 - Algoritmos e Estruturas de Dados

Autor: Kayque Lucas Santana dos Santos
Email: klss@cin.ufpe.br
Data: 2018-10-20

Descrição:  Algoritmo para profiling de verificação de plágio entre dois arquivos.

Copyright(c) 2018 Kayque Lucas Santana dos Santos
"""

from Corpus import Corpus, Documento
from memory_profiler import profile
import cProfile, pstats, io

def profilefunc(func):
    '''
    Decorador do profiling de tempo. Escreve o resultado no arquivo timeprofiling.txt.
    '''
    def _wrapper(*args, **kwargs):
        prof = cProfile.Profile()
        prof.enable()
        retval = prof.runcall(func, *args, **kwargs)
        prof.disable()
        
        s = io.StringIO()
        ps = pstats.Stats(prof, stream=s).sort_stats('cumulative')
        ps.print_stats()

        with open('timeprofiling.txt', 'w+') as f:
            f.write(s.getvalue())
            
        return retval
    return _wrapper

@profilefunc
def verificarPlagioTimeProfile(diretorioCorpus, diretorioDocumento, limiar):
    c=Corpus(diretorioCorpus)
    doc=Documento(diretorioDocumento)
    return c.verificarPlagio(doc, limiar)

@profile
def verificarPlagioMemUsageProfile(diretorioCorpus, diretorioDocumento, limiar):
    c=Corpus(diretorioCorpus)
    doc=Documento(diretorioDocumento)
    return c.verificarPlagio(doc, limiar)
