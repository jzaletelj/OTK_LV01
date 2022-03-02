# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 12:38:10 2016

@author: matevzk
"""

import numpy as np


class vrsta:
    def __init__(self, size):
        self.struct = np.empty(size, dtype=object)
        self.size = size
        self.prosta_mesta = size

    def push(self,podatek):
        self.prosta_mesta = len([i for i,x in enumerate(self.struct) if x == None]);
        if self.prosta_mesta > 0:
            self.struct = np.insert(self.struct,self.prosta_mesta,podatek);
            self.struct = np.delete(self.struct,0);
            self.prosta_mesta = len([i for i,x in enumerate(self.struct) if x == None]);
            status = 1; #vnos je bil uspesen
        else:
           status = 0;  #vnos ni bil uspesen
        return [status]


    def pop(self):
        podatek = None; 
        podatek = self.struct[self.size-1];
        self.struct = np.insert(self.struct,0,None);
        self.struct = np.delete(self.struct,self.size);
        self.prosta_mesta = len([i for i,x in enumerate(self.struct) if x == None]);     
       
        if self.prosta_mesta==self.size:
            status = 0; #vrsta je prazna
        else:
            status = 1; #v vrsti se se nahajajo podatki
        return [status,podatek]


class sklad:
    def __init__(self, size):
        self.struct = np.empty(size, dtype=object)
        self.size = size
        self.prosta_mesta = size
        

    def push(self, podatek ):
        self.prosta_mesta = len([i for i,x in enumerate(self.struct) if x == None]);
        if self.prosta_mesta > 0:
            self.struct = np.append(self.struct,podatek);
            self.struct = np.delete(self.struct,0);
            self.prosta_mesta = len([i for i,x in enumerate(self.struct) if x == None]);
            status = 1; # vnos je bil uspesen
        else:
           status = 0;  #vnos ni uspel
        return [status]
    
    
    def pop(self):
        podatek = None; 
        podatek = self.struct[self.size-1];
        self.struct = np.insert(self.struct,0,None);
        self.struct = np.delete(self.struct,self.size);
        self.prosta_mesta = len([i for i,x in enumerate(self.struct) if x == None]);     
       
        if self.prosta_mesta==self.size:
            status = 0; # self.struct je prazen
        else:
            status = 1; #c self.structu so se podatki
        return [status,podatek]
        
