    
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from validate_data import ValidateRequest 
from simple_data_analyser import SimpleDataAnalyser
from suburbs import suburbs_data

class DataVisualiser: 

    def prop_val_distribution(self,dataframe = None,suburb='',target_currency = '') :
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
                os.system('cls')
                print(f"\n Warning: {target_currency} cannot be identified. Converting to AUD !")
                target_currency = "AUD"
            suburb_dataframe = suburb_dataframe.copy()
            suburb_dataframe.dropna(subset=['price'], inplace=True)
            plt.hist(suburb_dataframe['price'], bins=5, edgecolor='k', alpha=0.7)
            plt.xlabel('Property Value')
            plt.title(f'Property Value Distribution in {suburb.capitalize()} ({target_currency})')
            plt.tight_layout()
            output_dir = 'Histograms'
            os.makedirs(output_dir, exist_ok=True)
            output_file = os.path.join(output_dir, f'{suburb.lower()}_property_histogram_{target_currency}.png')
            plt.savefig(output_file)
            print(f"\n Created histogram for {suburb} with location : {output_file}")
   
        
    def sales_trend(self,dataframe):
            ValidateRequest.validate_dataframe(dataframe)
            temp = dataframe.copy()
            temp['sold_date'] = pd.to_datetime(temp['sold_date'], format="%d-%m-%Y")
            temp.dropna(subset=['sold_date'], inplace=True)
            property_sold = temp['sold_date'].dt.year.value_counts().sort_index()
            plt.figure(figsize=(10, 6))
            plt.plot(property_sold.index, property_sold.values, marker='o', linestyle='-')
            plt.xlabel('Year')
            plt.ylabel('Properties Sold')
            plt.title('Sales Trend')
            plt.grid(True)
            output_dir = 'Linechart'
            os.makedirs(output_dir, exist_ok=True)
            output_file = os.path.join(output_dir, 'sales_trend.png')
            plt.savefig(output_file)
            print(f"\n Created sales trend chart at : {output_file}")
                
    def locate_price(self,target_price, data,target_suburb):
            ValidateRequest.validate_dataframe(data)
            ValidateRequest.validate_target_price(target_price)
            ValidateRequest.validate_string(target_suburb)
            temp = data.copy()
            temp['suburb'] = temp['suburb'].str.lower()
            target_suburb = target_suburb.lower()
            get_suburb = temp[temp['suburb'] == target_suburb]
            get_suburb_price = get_suburb.copy()
            get_suburb_price.dropna(subset=['price'], inplace=True)
            ValidateRequest.is_dataframe_empty(get_suburb_price, target_suburb)
            get_price_list = list(get_suburb_price['price'])
            ValidateRequest.reverse_insertion_sort(get_price_list)
            found = ValidateRequest.binary_search(get_price_list, target_price, 0, len(get_price_list) - 1)
            return found



