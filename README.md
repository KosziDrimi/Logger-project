# Logger 

This programme allows working with logs. It offers the possibility to create logs with the specific date, level and message. 
In order to check this project you should run the main.py script.

ProfilLogger class is responsible for creating and saving logs. 
In order to set the level of the log, the concrete method should be chosen.

The user can set the minimal level of logs to be saved.
The level from the lowest to the highest priority is as follows:
DEBUG -> INFO -> WARNING -> ERROR -> CRITICAL

LogEntry is a class that is actually storing the logs. 

It is also neccessary to choose the Handler that handles the saving requests. 
Its responsibility is also to read the files with the logs and preparing the lists of logs (in the format of LogEntry objects).

Handler class is the abstract class which covers the implementation of the following classes:
- JsonHandler - handler that stores and retrieves the list of logs in a JSON file,
- CSVHandler - handler that stores and retrieves the list of logs in a CSV file, 
- SQLiteHandler - handler that stores and retrieves the list of logs in sqlite database,
- FileHandler - handler that stores and retrieves the list of logs in a text file.

ProfilLoggerReader class is responsible for filtering the logs accoring the the users' requests. 
There are four filtering methods available. Each of them offers the possibility to optionally choose the starting and/or ending date.

This project is created in Python 3.8.3.

