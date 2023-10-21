import pandas as pd
import os
from validate_data import ValidateRequest

class SimpleDataAnalyser:

    @staticmethod
    def extract_property_info(file_path=''):   
            print("\n Reading your csv file ...")
            ValidateRequest.validate_file_path(file_path)
            csv_data = pd.read_csv(file_path, engine='python')
            ValidateRequest.validate_dataframe(csv_data)
            os.system('cls')
            return csv_data

    @staticmethod
    def currency_exchange(dataframe=None, exchange_rate=None):
            ValidateRequest.validate_dataframe(dataframe)
            ValidateRequest.validate_exchange_rate(exchange_rate)
            temp_frame = dataframe.copy()
            temp_frame['price'] = temp_frame['price'] * exchange_rate
            target_rate = temp_frame['price'].to_numpy()
            return target_rate
        
    @staticmethod
    def suburb_summary(dataframe=None, suburb=''):
            ValidateRequest.validate_dataframe(dataframe)
            ValidateRequest.validate_string(suburb)
            if suburb.lower() == "all":
                columns = dataframe[['bedrooms',
                                     'bathrooms', 'parking_spaces']].describe()
            else:
                temp = dataframe.copy()
                temp['suburb'] = dataframe['suburb'].str.lower()
                suburb_dataframe = temp[temp['suburb'] == suburb.lower()]
                ValidateRequest.is_dataframe_empty(suburb_dataframe,suburb)
                columns = suburb_dataframe[[
                    'bedrooms', 'bathrooms', 'parking_spaces']].describe()
            print(f"\n Summary details for {suburb.capitalize()} suburb:\n")
            print(f"\n {columns}")
            
    @staticmethod        
    def avg_land_size(dataframe=None, suburb=''):

            ValidateRequest.validate_dataframe(dataframe)
            ValidateRequest.validate_string(suburb)

            temp = dataframe.copy()
            temp['suburb'] = dataframe['suburb'].str.lower()
            suburb = suburb.lower()

            if suburb == 'all':
                suburb_dataframe = temp
            else:
                suburb_dataframe = temp[temp['suburb'] == suburb.lower()]

            ValidateRequest.is_dataframe_empty(suburb_dataframe,suburb)
            land_size_col_dataframe = suburb_dataframe['land_size']
            land_size_unit_col_dataframe = dataframe['land_size_unit'].str.strip().str.lower()
            csv_file_units = {
                'ha': 10000.0,      
                'm�': 1.0,          
                }
            land_size_area = land_size_col_dataframe * land_size_unit_col_dataframe.map(csv_file_units)
            correct_entries_boolean = (land_size_area > 0) & (land_size_area.notna())
            avg_land_size = land_size_area[correct_entries_boolean].mean()
            if pd.isna(avg_land_size):
                print(f"\n No valid land size data found in {suburb.capitalize()}.")
                return None
            else:
                print(f"\n Average Land Size in {suburb.capitalize()} suburb is : {avg_land_size:.2f} m²")
                return avg_land_size