
from investor import Investor
from simple_data_analyser import SimpleDataAnalyser
import os
from validate_data import ValidateRequest
from data_visualiser import DataVisualiser
import pandas as pd

def get_currency_type(user_suburb):
    while True:
        try:
            print(f"\n Suburb selected : {user_suburb.capitalize()}")
            print("\n Eg: [AUD, USD, INR, CNY, JPY, HKD, KRW, GBP, EUR, SGD] or \n (Type menu to go back)")
            user_currency_type = input("\n Enter your currency type: ")
            ValidateRequest.validate_string(user_currency_type)
            return user_currency_type
        except ValueError as e:
            os.system('cls')
            print(f"\n {e}")
        except KeyboardInterrupt:
            os.system('cls')
            break
        
def get_target_currency(user_suburb):
    while True:
        try:
            print(f"\n Suburb selected : {user_suburb.capitalize()} \n\n (Type 0 to go back)")
            user_traget_currency = input("\n Enter your target price: ")
            ValidateRequest.validate_target_price(user_traget_currency)
            return user_traget_currency
        except ValueError as e:
            os.system('cls')
            print(f"\n {e}")
        except KeyboardInterrupt:
            os.system('cls')
            break
    

def show_suburb_summary_1(dframe, simple_data_obj):
    while True:
        try:
            print("\n Summary of your Area")
            print("\n (Type 'all' to get summary of all suburb) or \n (Type 'menu' to go back)")
            user_suburb = input("\n Enter your suburb: ")
            if user_suburb.lower() == 'menu':
                os.system('cls')
            else:
                simple_data_obj.suburb_summary(dframe, user_suburb)
            break

        except ValueError as e:
            os.system('cls')
            print(f"\n {e}")
        except KeyboardInterrupt:
            os.system('cls')
            break
        
def determine_avg_land_size_2(dframe, simple_data_obj):
    while True:
        try:
            print("\n Get Avg land size of your Area :-")
            print("\n (Type 'all' to get summary of all suburb) or \n (Type 'menu' to go back)")
            user_suburb = input("\n Enter your suburb: ")
            if user_suburb.lower() == 'menu':
                os.system('cls')
            else:
                simple_data_obj.avg_land_size(dframe, user_suburb)
            break

        except ValueError as e:
            os.system('cls')
            print(f"\n {e}")
        except KeyboardInterrupt:
            os.system('cls')
            break
        
def calculate_property_val_dist_3(dframe,data_visual_obj):
    while True:
        try:
            print("\n Property value distribution of your Area :-")
            print("\n (Type 'all' to get summary of all suburb) or \n (Type 'menu' to go back)")
            user_suburb = input("\n Enter your suburb: ")
            ValidateRequest.validate_string(user_suburb)
            
            os.system('cls')
            if user_suburb.lower() == 'menu':
                break
            user_currency_type = get_currency_type(user_suburb)
            
            if not user_currency_type or user_currency_type.lower() == 'menu':
                os.system('cls')
                continue
            
            else:
                data_visual_obj.prop_val_distribution(dframe, user_suburb,user_currency_type)
                break

        except ValueError as e:
            os.system('cls')
            print(f"\n {e}")
        except KeyboardInterrupt:
            os.system('cls')
            break
        
def find_property_prices_5 (dframe,data_visual_obj):
    while True:
        try:
            print("\n Find property prices :-")
            print("\n (Type 'menu' to go back)")
            user_suburb = input("\n Enter your suburb: ")
            ValidateRequest.validate_string(user_suburb)
            os.system('cls')
            if user_suburb.lower() == 'menu':
                break
            user_target_currency = get_target_currency(user_suburb)
            if not user_target_currency or int(user_target_currency) == 0:
                os.system('cls')
                continue
            else:
                check_if_present = data_visual_obj.locate_price(user_target_currency,dframe,user_suburb)
                os.system('cls')
                if check_if_present:
                    print(f"\n Property found : expected property price :- {user_target_currency} is present in given data")
                
                else:
                    print(f"\n Sorry ! Target property price {user_target_currency} not found")
                break
            
        except ValueError as e:
            os.system('cls')
            print(f"\n {e}")
        except KeyboardInterrupt:
            os.system('cls')
            break
        
def load_csv_file(simple_data_obj):
    dframe = pd.DataFrame()
    try:
        filePath = os.path.join('property_information.csv')
        while not os.path.isfile(filePath):
            os.system('cls')
            try:
                print(f"\n Error: File {filePath} does not exist")
                print(f" File location should be : Property-Investment-Analysis/{filePath}")
                print("\n Press Enter to continue after you have added the file or '0' to exit.")
                user_option = input("\n Enter you choice : ")
                if user_option == '0':
                    return dframe
            except KeyboardInterrupt:
                return dframe
            
        return simple_data_obj.extract_property_info(filePath)
    except ValueError as e:
        os.system('cls')
        print(f"\n {e}")
        return dframe
    except KeyboardInterrupt:
        os.system('cls')   
        return dframe
    
    

def main():
            os.system('cls')
            investor_obj = Investor()
            simple_data_obj = SimpleDataAnalyser()
            data_visual_obj = DataVisualiser()
            
            dframe = load_csv_file(simple_data_obj)
            if dframe.empty:
                return
            while True:
                try:
                    investor_obj.main_menu()
                    choice = investor_obj.choice
                    os.system('cls')
                    if choice == 1:
                        show_suburb_summary_1(dframe, simple_data_obj)
                                    
                    elif choice == 2:
                        determine_avg_land_size_2(dframe,simple_data_obj)
                                    
                    elif choice == 3:
                        calculate_property_val_dist_3(dframe,data_visual_obj)
                                    
                    elif choice == 4:
                        data_visual_obj.sales_trend(dframe)
                        
                    elif choice == 5:
                        find_property_prices_5(dframe,data_visual_obj)
                    else:
                        investor_obj.exit_system()  
                        return  
                except ValueError as e:
                    os.system('cls')
                    print(f"\n {e}")
                except KeyboardInterrupt:
                    os.system('cls')
                    break

if __name__ == '__main__':
    main()
