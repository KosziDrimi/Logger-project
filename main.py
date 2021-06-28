# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 14:52:36 2021

@author: klimi
"""

from datetime import datetime

from Logger.JsonHandler import JsonHandler
from Logger.CSVHandler import CSVHandler
from Logger.FileHandler import FileHandler
from Logger.SQLiteHandler import SQLiteHandler
from Logger.ProfilLogger import ProfilLogger
from Logger.ProfilLoggerReader import ProfilLoggerReader


if __name__ == "__main__":
        
    json_handler = JsonHandler("logs.json")
    csv_handler = CSVHandler("logs.csv")
    sql_handler = SQLiteHandler("logs.sqlite")
    file_handler = FileHandler("logs.txt")

    logger = ProfilLogger(handlers=[json_handler, csv_handler, sql_handler, file_handler])
    
    logger.set_log_level("INFO")
    logger.info("Some info message")
    logger.warning("Some warning message")
    logger.debug("Some debug message")
    logger.critical("Some critical message")
    logger.error("Some error message")

    log_reader = ProfilLoggerReader(handler=json_handler)
    
    
    print(log_reader.find_by_text("info message", 
                                  end_date = datetime(2021, 6, 28, 18, 30)))
        
    print(log_reader.find_by_regex("[r]{2}", 
                        datetime(2021, 6, 27, 18), datetime(2021, 6, 28, 19)))
           
    print(log_reader.groupby_level(datetime(2021, 6, 27, 18), 
                                   datetime(2021, 6, 27, 18, 30)))

    print(log_reader.groupby_month(datetime(2021, 6, 27, 17, 50), 
                                   datetime(2021, 6, 27, 18, 10)))
