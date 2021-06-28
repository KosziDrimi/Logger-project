# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 13:37:49 2021

@author: klimi
"""

from typing import List
from datetime import datetime

from .LogEntry import LogEntry
from .Handler import Handler


class ProfilLogger:
    
    
    def __init__(self, handlers: List[Handler]):
        self.handlers = handlers   
        self._log_level = 0
    """
    param: handlers - list of handlers that will be responsible for saving
    log entries
    """
    
    def write_entry(self, entry):   
        """ sends the entry to the appropriate handler for storing """
        for handler in self.handlers:
            handler.store(entry)       
       
    def info(self, msg: str):
        """ logs a message with level INFO """
        lev = 2
        if lev >= self._log_level:
            new_entry = LogEntry(datetime.now(), 'INFO', msg)
            self.write_entry(new_entry)

    def warning(self, msg: str):
        """ logs a message with level WARNING """
        lev = 3
        if lev >= self._log_level:
            new_entry = LogEntry(datetime.now(), 'WARNING', msg)
            self.write_entry(new_entry)

    def debug(self, msg: str):
        """ logs a message with level DEBUG """
        lev = 1
        if lev >= self._log_level:
            new_entry = LogEntry(datetime.now(), 'DEBUG', msg)
            self.write_entry(new_entry)
    
    def critical(self, msg: str):
        """ logs a message with level CRITICAL """
        lev = 5
        if lev >= self._log_level:
            new_entry = LogEntry(datetime.now(), 'CRITICAL', msg)
            self.write_entry(new_entry)
    
    def error(self, msg: str):
        """ logs a message with level ERROR """
        lev = 4
        if lev >= self._log_level:
            new_entry = LogEntry(datetime.now(), 'ERROR', msg)
            self.write_entry(new_entry)
    
    def set_log_level(self, level: str):
        """ sets minimal log level to be saved """
        priority = {'DEBUG': 1, 'INFO': 2, 'WARNING': 3, 'ERROR': 4, 'CRITICAL': 5}
        for key, val in priority.items():
            if key == level:
                self._log_level = val
        