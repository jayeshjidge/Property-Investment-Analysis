import pandas as pd
import os
import numpy as np



class ValidateRequest:
    
    @staticmethod
    def validate_file_path(file_path):
        
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
        
        if not isinstance(string, str) or not string.strip() or string.isdigit():
            raise ValueError("Input Error: Please enter correct input")
        
    
    @staticmethod
    def is_dataframe_empty(dataframe,suburb):
        
        if dataframe.empty:
            raise ValueError(f"Result Not found: Suburb '{suburb.capitalize()}' does not exist in the data")
        
    @staticmethod
    def validate_target_price(target_price):
        if target_price.isdigit():
            target_price = int(target_price)
        if not target_price and not target_price == 0:
            
            raise ValueError("Empty Error: Target price cannot be zero")
        if not isinstance(target_price, int):
            raise ValueError("Input Error: Please enter a correct input type")
        
        
        
    @staticmethod
    def reverse_insertion_sort(prices):
        for i in range(1, len(prices)):
            key = prices[i]
            j = i - 1
            while j >= 0 and key > prices[j]:
                prices[j + 1] = prices[j]
                j -= 1
            prices[j + 1] = key
            
    @staticmethod
    def binary_search(prices, target_price, low, high):
        target_price = float(target_price)
        if low > high:
            return False
        mid = (low + high) // 2
        if prices[mid] == target_price:
            return True
        elif prices[mid] > target_price:
            return ValidateRequest.binary_search(prices, target_price, mid + 1, high)
        else:
            return ValidateRequest.binary_search(prices, target_price, low, mid - 1)

