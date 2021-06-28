# -*- coding: utf-8 -*-
"""
Created on Thu Sat 26 13:54:39 2021

@author: klimi
"""

from typing import List, Dict, Optional
from datetime import datetime
import re

from .LogEntry import LogEntry
from .Handler import Handler


class ProfilLoggerReader: 
    
    
    def __init__(self, handler: Handler):
        self.handler = handler
    """
    param: handler - handler that will be responsible for reading log entries
    """
     
    @staticmethod
    def date_to_datetime(date):
        """ amends the date in string format into datetime format """
        date = date[:-7]
        return datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    
    @staticmethod
    def start_date_filter(entries, start_date):
        """ filters logs according to start_date given """
        entries = [entry for entry in entries if 
                 ProfilLoggerReader.date_to_datetime(entry.date) >= start_date]
        return entries
    
    @staticmethod
    def end_date_filter(entries, end_date):
        """ filters logs according to end_date given """
        entries = [entry for entry in entries if 
                 ProfilLoggerReader.date_to_datetime(entry.date) <= end_date]
        return entries

    def find_by_text(self, text: str, start_date: Optional[datetime] = None, 
                     end_date: Optional[datetime] = None) -> List[LogEntry]:
        """
        Finds log entries that contain given text. If any datetime is given, 
        filter logs according to that datetime.
        """
        entries = self.handler.read_log()
        entries = [entry for entry in entries if text in entry.msg]
        
        if start_date and end_date:
            assert end_date > start_date, 'End_date needs to be after start_date.'
        
        if start_date:
            entries = ProfilLoggerReader.start_date_filter(entries, start_date)
        if end_date:
            entries = ProfilLoggerReader.end_date_filter(entries, end_date)  
        return entries

    def find_by_regex(self, regex: str, start_date: Optional[datetime] = None, 
                      end_date: Optional[datetime] = None) -> List[LogEntry]:
        """    
        Finds logs by a given regex. If any datetime is given, filter logs 
        according to that datetime.
        """
        entries = self.handler.read_log()
        entries = [entry for entry in entries if re.findall(regex, entry.msg)]
        
        if start_date and end_date:
            assert end_date > start_date, 'End_date needs to be after start_date.'
            
        if start_date:
            entries = ProfilLoggerReader.start_date_filter(entries, start_date)
        if end_date:
            entries = ProfilLoggerReader.end_date_filter(entries, end_date)  
        return entries
    
    def groupby_level(self, start_date: Optional[datetime] = None, end_date: 
                      Optional[datetime] = None) -> Dict[str, List[LogEntry]]:
       """
       Group logs by level. If any datetime is given, filter logs according to 
       that datetime.
       """
       levels = {}
       levels['DEBUG'] = []
       levels['INFO'] = [] 
       levels['WARNING'] = [] 
       levels['ERROR'] = [] 
       levels['CRITICAL'] = [] 
       
       entries = self.handler.read_log()
       
       if start_date and end_date:
            assert end_date > start_date, 'End_date needs to be after start_date.'
            
       if start_date:
            entries = ProfilLoggerReader.start_date_filter(entries, start_date)
       if end_date:
            entries = ProfilLoggerReader.end_date_filter(entries, end_date)  
              
       for entry in entries:
           for key in levels.keys():
               if entry.level == key:
                   levels[key].append(entry)
       return levels
    
    def groupby_month(self, start_date: Optional[datetime] = None, end_date: 
                      Optional[datetime] = None) -> Dict[str, List[LogEntry]]:
       """
       Group logs by month. If any datetime is given, filter logs according to 
       that datetime.
       """
       mapping = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 
                  'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9,
                  'October': 10, 'November': 11, 'December': 12}
       
       entries = self.handler.read_log()
       
       if start_date and end_date:
            assert end_date > start_date, 'End_date needs to be after start_date.'
            
       if start_date:
            entries = ProfilLoggerReader.start_date_filter(entries, start_date)
       if end_date:
            entries = ProfilLoggerReader.end_date_filter(entries, end_date)  
        
       months = {}
       months['January'] = []
       months['February'] = [] 
       months['March'] = [] 
       months['April'] = [] 
       months['May'] = [] 
       months['June'] = [] 
       months['July'] = [] 
       months['August'] = [] 
       months['September'] = [] 
       months['October'] = [] 
       months['November'] = [] 
       months['December'] = []
       
       for entry in entries:
           for key, val in mapping.items():
               if (ProfilLoggerReader.date_to_datetime(entry.date)).month == val:
                   months[key].append(entry)
       return months                
 