# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 16:07:19 2021

@author: klimi
"""

from pathlib import Path
import csv

from .Handler import Handler
from .LogEntry import LogEntry


class CSVHandler(Handler):
    """ handler that stores and retrieves the list of LogEntry in a CSV file """
    
    
    def __init__(self, path: str):
        self.path = path
    
    def store(self, entry):  
        headers = ['date', 'level', 'message']
        mapping = {}
        mapping['date'] = str(entry.date)
        mapping['level'] = entry.level
        mapping['message'] = entry.msg
        
        if not Path(self.path).is_file():
            with open(self.path, 'a', newline = '') as f:
                writer = csv.DictWriter(f, fieldnames=headers)
                writer.writeheader()
                writer.writerow(mapping)
        else:
            with open(self.path, 'a', newline = '') as f:
                writer = csv.DictWriter(f, fieldnames=headers)
                writer.writerow(mapping)
             
    def read_log(self):
        with open('logs.csv') as f:
            reader = csv.DictReader(f)
            result = []
            for row in reader:
                new = LogEntry(row['date'], row['level'], row['message'])
                result.append(new)
            return result
        