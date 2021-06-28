# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 19:58:05 2021

@author: klimi
"""

from pathlib import Path
import sqlite3

from .Handler import Handler
from .LogEntry import LogEntry


class SQLiteHandler(Handler):
    """ handler that stores and retrieves the list of LogEntry in sqlite database """
    
    
    def __init__(self, path: str):
        self.path = path
    
    def store(self, entry):
        
        if not Path(self.path).is_file():
            Path(self.path).touch()
            conn = sqlite3.connect(self.path)
            c = conn.cursor()
            c.execute('''CREATE TABLE Logs (date TEXT, level TEXT, message TEXT)''')               
            data = (entry.date, entry.level, entry.msg)
            insert = '''INSERT INTO logs (date, level, message)
                     VALUES (?, ?, ?)'''
            c.execute(insert, data)
            conn.commit()
            c.close()  
        else:
            conn = sqlite3.connect(self.path)
            c = conn.cursor()
            data = (entry.date, entry.level, entry.msg)
            insert = '''INSERT INTO logs (date, level, message)
                     VALUES (?, ?, ?)'''
            c.execute(insert, data)
            conn.commit()
            c.close()
             
    def read_log(self):
        conn = sqlite3.connect('logs.sqlite')
        c = conn.cursor()
        select = '''SELECT * FROM Logs'''
        c.execute(select)
        entries = c.fetchall()
        result = []
        for entry in entries:
            new = LogEntry(entry[0], entry[1], entry[2])
            result.append(new)
        return result
        c.close()     
        