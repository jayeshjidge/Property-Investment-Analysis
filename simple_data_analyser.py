import pandas as pd
import os
import numpy as np  
class SimpleDataAnalyser:
    
    def extract_property_info(self,file_path='') :
        handleError = None
        try:
            if not file_path:
                raise ValueError("\nError: File path cannot be empty")
            
            if isinstance(file_path, int):
                raise ValueError("\nError: File path cannot be an integer")
            if not os.path.isfile(file_path):
                raise ValueError(f"\nError: File '{file_path}' does not exist")
            
            csv_data = pd.read_csv(file_path)
            return csv_data
            
        except ValueError as e:
            os.system('cls')
            print(e)
            return pd.DataFrame() 
        except KeyboardInterrupt:
            os.system('cls')
            
    def currency_exchange(self, dataframe = None, exchange_rate = None):
        try:
            
            if not isinstance(dataframe, pd.DataFrame) or dataframe.empty:
                raise ValueError("\nError: Invalid or Empty data")

            if not isinstance(exchange_rate,float) :
                raise ValueError("\nInput Error: Please enter correct input type")
            
            if not exchange_rate or exchange_rate == 0:
                raise ValueError("\nEmpty Error: Exchange rate cannot be zero")
            
            temp_frame = dataframe.copy()
            temp_frame['price'].fillna(0, inplace=True)
            temp_frame['price'] = temp_frame['price'] * exchange_rate
            target_rate = temp_frame['price'].to_numpy()
            return target_rate

        except ValueError as e:
            os.system('cls')
            print(e)
            return np.array([])




# obj = SimpleDataAnalyser()
# filePath = os.path.join('property_information.csv')
# dataframe = obj.extract_property_info(filePath)
# empty_df = pd.DataFrame()
# currency_np_array = obj.currency_exchange(dataframe,1.0)
# print(currency_np_array)
