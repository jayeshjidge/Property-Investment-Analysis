import pandas as pd
import os
import numpy as np



class ValidateRequest:
    
    @staticmethod
    def validate_file_path(file_path):
        
        if not file_path.strip():
            raise ValueError("Error: File path cannot be empty")
        
        if isinstance(file_path, int):
            raise ValueError("Error: File path cannot be an integer")
        
        if not os.path.isfile(file_path):
            raise ValueError(f"Error: File '{file_path}' does not exist")    
            
    @staticmethod
    def validate_dataframe(dataframe):
        
        if not isinstance(dataframe, pd.DataFrame) or dataframe.empty:
            raise ValueError("Error: Invalid or Empty data in file")
        
    @staticmethod
    def validate_exchange_rate(exchange_rate):
        
        if not isinstance(exchange_rate, float):
            raise ValueError("Input Error: Please enter a correct input type")
        
        if not exchange_rate or exchange_rate == 0:
            raise ValueError("Empty Error: Exchange rate cannot be zero")
        
    @staticmethod
    def validate_string(string):
        
        if not isinstance(string, str) or not string.strip():
            raise ValueError("Input Error: Please enter correct input")
        
    
    @staticmethod
    def is_dataframe_empty(dataframe,suburb):
        
        if dataframe.empty:
            raise ValueError(f"Result Not found: Suburb '{suburb.capitalize()}' does not exist in the data")