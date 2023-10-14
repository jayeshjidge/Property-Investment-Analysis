import pandas as pd
import os
import numpy as np


class SimpleDataAnalyser:

    def extract_property_info(self, file_path=''):
        try:
            if not file_path.strip():
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

    def currency_exchange(self, dataframe=None, exchange_rate=None):
        try:

            if not isinstance(dataframe, pd.DataFrame) or dataframe.empty:
                raise ValueError("\nError: Invalid or Empty data in file")

            if not isinstance(exchange_rate, float):
                raise ValueError(
                    "\nInput Error: Please enter correct input type")

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

    def suburb_summary(self, dataframe=None, suburb=''):
        try:
            if not isinstance(dataframe, pd.DataFrame) or dataframe.empty:
                raise ValueError("\nError: Invalid or Empty data in file")

            if not isinstance(suburb, str) or not suburb.strip():
                raise ValueError("\nInput Error: Please enter correct input")

            if suburb.lower() == "all":
                columns = dataframe[['bedrooms',
                                     'bathrooms', 'parking_spaces']].describe()
            else:
                temp = dataframe.copy()
                temp['suburb'] = dataframe['suburb'].str.lower()
                suburb_dataframe = temp[temp['suburb'] == suburb.lower()]

                if suburb_dataframe.empty:
                    raise ValueError(
                        f"\nResult Not found: Suburb '{suburb.capitalize()}' does not exist in the data")

                columns = suburb_dataframe[[
                    'bedrooms', 'bathrooms', 'parking_spaces']].describe()
            os.system('cls')
            print(f"\n Summary Details for {suburb.capitalize()} Suburb:\n")
            print(columns)

        except ValueError as e:
            os.system('cls')
            print(e)

    def avg_land_size(self, dataframe=None, suburb=''):
        try:
            if not isinstance(dataframe, pd.DataFrame) or dataframe.empty:
                raise ValueError("\nError: Invalid or Empty data in file")

            if not isinstance(suburb, str) or not suburb.strip():
                raise ValueError("\nInput Error: Please enter correct input")

            temp = dataframe.copy()
            temp['suburb'] = dataframe['suburb'].str.lower()
            suburb = suburb.lower()

            if suburb == 'all':
                suburb_dataframe = temp
            else:
                suburb_dataframe = temp[temp['suburb'] == suburb.lower()]

            if suburb_dataframe.empty:
                raise ValueError(
                    f"\nResult Not found: Suburb '{suburb}' does not exist in the data")
            land_size_col_dataframe = suburb_dataframe['land_size']
            land_size_unit_col_dataframe = dataframe['land_size_unit'].str.strip().str.lower()
            csv_file_units = {
                'ha': 10000.0,      
                'm�': 1.0,          
                }
            land_size_area = land_size_col_dataframe * land_size_unit_col_dataframe.map(csv_file_units)
            correct_entries_boolean = (land_size_area > 0) & (land_size_area.notna())
            avg_land_size = land_size_area[correct_entries_boolean].mean()
            os.system('cls')
            if pd.isna(avg_land_size):
                print(f"\nNo valid land size data found in {suburb.capitalize()}.")
                return None
            else:
                print(f"\nAverage Land Size in {suburb.capitalize()} suburb is : {avg_land_size:.2f} m²")
                return avg_land_size
        except ValueError as e:
            os.system('cls')
            print(e)
            
    


# obj = SimpleDataAnalyser()
# filePath = os.path.join('property_information.csv')
# dataframe = obj.extract_property_info(filePath)
# # empty_df = pd.DataFrame()
# currency_np_array = obj.currency_exchange(dataframe,1.0)
# print(currency_np_array)
# obj.suburb_summary(dataframe,'all')
