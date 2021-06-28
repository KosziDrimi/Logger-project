# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 14:50:53 2021

@author: klimi
"""

from datetime import datetime


class LogEntry:
    """ class for storing the log entry """
    
    
    log_entries = []
    
    def __init__(self, date: datetime, level: str, msg: str):
        self.date = date
        self.level = level
        self.msg = msg
        self.log_entries.append(self)
        
    def __str__(self):
        return f'{self.date} | {self.level} | {self.msg}'
    
    def __repr__(self):
        return f'<{self.date}, {self.level}, {self.msg}>'
    
    @classmethod
    def show_log_entries(cls):
        for entry in cls.log_entries:
            print(entry)
            