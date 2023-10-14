import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from validate_data import ValidateRequest 
from simple_data_analyser import SimpleDataAnalyser
from suburbs import suburbs_data

class DataVisualiser: 

    def prop_val_distribution(self,dataframe = None,suburb='',target_currency='AUD') :
        try:
            currency_dict = {
                "AUD": 1.0, 
                "USD": 0.66, 
                "INR": 54.25, 
                "CNY": 4.72,
                "JPY": 93.87,
                "HKD": 5.12,
                "KRW": 860.92,
                "GBP": 0.51,
                "EUR": 0.60,
                "SGD": 0.88 }
        
            ValidateRequest.validate_dataframe(dataframe)
            ValidateRequest.validate_string(suburb)
            
            target_currency = target_currency.upper()
            temp = dataframe.copy()
            temp['suburb'] = dataframe['suburb'].str.lower()
            suburb = suburb.lower()
            
            if suburb == 'all':
                suburb_dataframe = temp
            else:
                suburb_dataframe = temp[temp['suburb'] == suburb.lower()]
                
            ValidateRequest.is_dataframe_empty(suburb_dataframe, suburb)
            data_obj = SimpleDataAnalyser()
            if target_currency in currency_dict:
                exchange_rate = currency_dict[target_currency]
                new_suburb_dataframe = suburb_dataframe.copy()
                new_suburb_dataframe['price'] = data_obj.currency_exchange(suburb_dataframe, exchange_rate)
                suburb_dataframe = new_suburb_dataframe
                  
            else:
                print(f"\nWarning: {target_currency} cannot be identified. Converting to AUD !")
            suburb_dataframe = suburb_dataframe.copy()
            suburb_dataframe.dropna(subset=['price'], inplace=True)
            plt.hist(suburb_dataframe['price'], bins=5, edgecolor='k', alpha=0.7)
            plt.xlabel('Property Value')
            plt.ylabel('Frequency')
            plt.title(f'Property Value Distribution in {suburb.capitalize()} ({target_currency})')
            output_dir = 'Histograms'
            os.makedirs(output_dir, exist_ok=True)
            output_file = os.path.join(output_dir, f'{suburb.lower()}_property_histogram_{target_currency}.png')
            plt.savefig(output_file)
            print(f"\nCreated histogram for {suburb} with location : {output_file}")
   
        except ValueError as e:
            os.system('cls')
            print(f"\n{e}")
        except KeyboardInterrupt:
            os.system('cls')
        
        
        
        
# data_obj = DataVisualiser()
# simple_obj = SimpleDataAnalyser()
# file_path = os.path.join('property_information.csv')
# dataframe = simple_obj.extract_property_info(file_path)


# data_obj.prop_val_distribution(dataframe,"clayton","AUD")
# for sub in suburbs_data:
#     data_obj.prop_val_distribution(dataframe,sub,"A")