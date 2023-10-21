
from investor import Investor
from simple_data_analyser import SimpleDataAnalyser
import os
from validate_data import ValidateRequest
from data_visualiser import DataVisualiser


def show_suburb_summary(dframe, simple_data_obj):
    os.system('cls')
    while True:
        try:
            print("\n Summary of your Area")
            print("\n (Type 'all' to get summary of all suburb) or \n (Type 'menu' to go back)")
            print("\n (Type 'menu' to go back)")
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
        
def determine_avg_land_size(dframe, simple_data_obj):
    os.system('cls')
    while True:
        try:
            print("\n Avg land size of your Area")
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
        
def get_user_currency_type(user_suburb):
    while True:
        try:
            print(f"\n Suburb selected : {user_suburb.capitalize()}")
            print("\n Eg: [AUD, USD, INR, CNY, JPY, HKD, KRW, GBP, EUR, SGD] or type menu to go back")
            user_currency_type = input("\n Enter your currency type: ")
            ValidateRequest.validate_string(user_currency_type)
            return user_currency_type
        except ValueError as e:
            os.system('cls')
            print(f"\n {e}")
        except KeyboardInterrupt:
            os.system('cls')
            break
       
        
def calculate_property_val_dist(dframe,data_visual_obj):
    os.system('cls')
    while True:
        try:
            print("\n Property value distribution of your Area :-")
            print("\n (Type 'all' to get summary of all suburb) or \n (Type 'menu' to go back)")
            user_suburb = input("\n Enter your suburb: ")
            ValidateRequest.validate_string(user_suburb)
            
            os.system('cls')
            if user_suburb.lower() == 'menu':
                break
            user_currency_type = get_user_currency_type(user_suburb)
            if not user_currency_type or user_currency_type.lower() == 'menu':
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
    

def main():
    os.system('cls')
    filePath = os.path.join('property_information.csv')
    investor_obj = Investor()
    simple_data_obj = SimpleDataAnalyser()
    data_visual_obj = DataVisualiser()
    try:
                dframe = simple_data_obj.extract_property_info(filePath)
                while True:
                    try:
                        investor_obj.main_menu()
                        choice = investor_obj.choice
                        if choice == 1:
                            show_suburb_summary(dframe, simple_data_obj)
                            
                        elif choice == 2:
                            determine_avg_land_size(dframe,simple_data_obj)
                            
                        elif choice == 3:
                            calculate_property_val_dist(dframe,data_visual_obj)
                        else:
                            break    
                    except ValueError as e:
                        os.system('cls')
                        print(f"\n{e}")
                    except KeyboardInterrupt:
                        os.system('cls')
                        break

    except ValueError as e:
                os.system('cls')
                print(f"\n {e}")
    except KeyboardInterrupt:
                os.system('cls')


if __name__ == '__main__':
    main()
