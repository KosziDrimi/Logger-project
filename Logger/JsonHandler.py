# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 14:54:41 2021

@author: klimi
"""

import json

from .Handler import Handler
from .LogEntry import LogEntry


class JsonHandler(Handler):
    """ handler that stores and retrieves the list of LogEntry in a JSON file """
   
    
    def __init__(self, path: str):
        self.path = path
    
    def store(self, entry):
        mapping = {}
        mapping['date'] = str(entry.date)
        mapping['level'] = entry.level
        mapping['message'] = entry.msg
        
        with open(self.path, 'a') as f:
            json.dump(mapping, f)
            f.write('\n')
            
    def read_log(self):
        with open('logs.json') as f:
            result = []
            for line in f.readlines():
                entry = json.loads(line)
                new = LogEntry(entry['date'], entry['level'], entry['message'])
                result.append(new)
            return result
        