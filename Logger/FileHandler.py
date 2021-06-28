# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 19:48:39 2021

@author: klimi
"""

from .Handler import Handler
from .LogEntry import LogEntry


class FileHandler(Handler):
    """ handler that stores and retrieves the list of LogEntry in a text file """
   
    
    def __init__(self, path: str):
        self.path = path
    
    def store(self, entry):
        with open(self.path, 'a') as f:
            print(entry, file=f)     
            
    def read_log(self):
        with open('logs.txt') as f:
            result = []
            for line in f.readlines():
                entry = line.split('|')
                date = entry[0].strip()  
                level = entry[1].strip()
                msg = entry[2].strip()    
                new = LogEntry(date, level, msg)
                result.append(new)
            return result
        