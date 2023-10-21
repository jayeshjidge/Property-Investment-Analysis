from simple_data_analyser import SimpleDataAnalyser
import os 
from data_visualiser import DataVisualiser


#-----------------------------------------------------------------
# Extracting Property Information

simple_data_object = SimpleDataAnalyser()
file_path = os.path.join('property_information.csv')
dataframe = simple_data_object.extract_property_info(file_path)
print(len(dataframe))

# -----------------------------------------------------------------
# Currency Exchange

exchange_rate = 1.2
currency = simple_data_object.currency_exchange(dataframe,exchange_rate)
print(currency)

# -----------------------------------------------------------------
# Suburb Property Summary

suburb = 'Clayton'
simple_data_object.suburb_summary(dataframe,suburb)

# -----------------------------------------------------------------
# Average Land Size

land_size = simple_data_object.avg_land_size(dataframe,suburb)
print(land_size)

# -----------------------------------------------------------------
# Property Value Distribution

data_visualize_obj = DataVisualiser()
target_currency = "INR"
data_visualize_obj.prop_val_distribution(dataframe,suburb,target_currency)

# -----------------------------------------------------------------
#  Sales Trend

data_visualize_obj.sales_trend(dataframe)

# -----------------------------------------------------------------
# Identifying a Property of a Specific Price in a Suburb
target_price = "965000"
check_if_present = data_visualize_obj.locate_price(target_price,dataframe,suburb)
print(check_if_present)

# -----------------------------------------------------------------