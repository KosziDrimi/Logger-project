# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 14:51:47 2021

@author: klimi
"""

from abc import ABC, abstractmethod


class Handler(ABC):
    
    
    def __init__(self, path: str):
        self.path = path
    
    @abstractmethod
    def store(self, entry):
        pass
    
    @abstractmethod
    def read_log(self):
        pass        
    