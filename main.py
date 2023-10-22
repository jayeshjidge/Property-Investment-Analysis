
from investor import Investor
from simple_data_analyser import SimpleDataAnalyser
import os
from validate_data import ValidateRequest
from data_visualiser import DataVisualiser
import pandas as pd


def get_currency_type(user_suburb):
    """
    This function is used to return currency type which is typed by user.

    Args:
        user_suburb (str): takes suburb as a string

    Returns:
        str: Returns user input currency type.
    """
    while True:
        try:
            print(f"\n Suburb selected : {user_suburb.capitalize()}")
            print(
                "\n Choose from [AUD, USD, INR, CNY, JPY, HKD, KRW, GBP, EUR, SGD]\n\n [Type menu to go back]")
            user_currency_type = input("\n Enter your currency type: ")
            # validate the string for any error
            ValidateRequest.validate_string(user_currency_type)
            # return currency type
            return user_currency_type
        except ValueError as e:
            # error handling if error occurs
            os.system('cls')
            print(f"\n {e}")
        except KeyboardInterrupt:
            os.system('cls')
            break


def get_target_currency(user_suburb):
    """
    This function is used to return target price which is input by the user

    Args:
        user_suburb (str): takes suburb as a string

    Returns:
        str:  Returns user input currency type.
    """
    while True:
        try:
            print(
                f"\n Suburb selected : {user_suburb.capitalize()} \n\n [Type 0 to go back]")
            user_traget_currency = input("\n Enter your target price: ")
            # validates price for any errors
            ValidateRequest.validate_target_price(user_traget_currency)
            # returns the target price entered by the user
            return user_traget_currency
        except ValueError as e:
            # displays erros if any occurs
            os.system('cls')
            print(f"\n {e}")
        except KeyboardInterrupt:
            os.system('cls')
            break


def show_suburb_summary_1(dframe, simple_data_obj):
    """
    This function is used to display the summary of subrubs. 
    It includes details like count, mean, std, min, 
    25%, 5-%, 75%, max of the specific suburb properties 
    with respect to number of bedroom, bathroom and parking.

    Args:
        dframe (pd.DataFrame): takes dataframe of a csv data file.
        simple_data_obj (SimpleDataAnalyser): takes object of SimpleDataAnalyser.

    Returns:
        It does not return any value
    """
    while True:
        try:
            print("\n  --------------------------")
            print(" | Summary of your Suburb : |")
            print("  --------------------------")
            print(
                "\n [Type 'all' to get summary of all suburb]\n\n [Type 'menu' to go back]")
            user_suburb = input("\n Enter your suburb: ")
            # take suburb as a input from user
            os.system('cls')
            if user_suburb.lower() == 'menu':
             # break the loop if the input is menu to go back to previous menu
                break
            # calls the suburb summary function to display the summary
            simple_data_obj.suburb_summary(dframe, user_suburb)
            break
        except ValueError as e:
            # error handling if error occurs
            os.system('cls')
            print(f"\n {e}")
        except KeyboardInterrupt:
            os.system('cls')
            break


def determine_avg_land_size_2(dframe, simple_data_obj):
    """
    This function is used to give the average land size in a given specific suburb. 
    It basically takes input as suburb or all to display the average land size in m2 by 
    calculating the mean of all the land size. 

    Args:
        dframe (pd.DataFrame): takes dataframe of a csv data file.
        simple_data_obj (SimpleDataAnalyser): takes object of SimpleDataAnalyser.

    Returns:
        None
    """
    while True:
        try:
            print("\n  ------------------------------------")
            print(" | Get Avg land size of your suburb : |")
            print("  ------------------------------------")
            print(
                "\n [Type 'all' to get avg size of all suburb]\n\n [Type 'menu' to go back]")
            # take suburb as a input from user
            user_suburb = input("\n Enter your suburb: ")
            os.system('cls')
            if user_suburb.lower() == 'menu':
                # break the loop if the input is menu to go back to previous menu
                break
            simple_data_obj.avg_land_size(dframe, user_suburb)
            break
        except ValueError as e:
            # error handling if error occurs
            os.system('cls')
            print(f"\n {e}")
        except KeyboardInterrupt:
            os.system('cls')
            break


def calculate_property_val_dist_3(dframe, data_visual_obj):
    """
    This function is used to determine the property prices of the user input suburb or all the suburb. 
    It creates and stores the histogram of the suburb upon completion.

    Args:
        dframe (pd.DataFrame): takes dataframe of a csv data file.
        data_visual_obj (DataVisualiser): takes object of DataVisualiser class

    Returns:
        None
    """
    while True:
        try:
            print("\n  ----------------------------------------------")
            print(" | Property value distribution of your suburb : |")
            print("  ----------------------------------------------")
            print(
                "\n [Type 'all' to get distribution of all suburb]\n\n [Type 'menu' to go back]")
            # takes suburb as a input from user
            user_suburb = input("\n Enter your suburb: ")
            # validate the string for any errors
            ValidateRequest.validate_string(user_suburb)
            os.system('cls')

            if user_suburb.lower() == 'menu':
                # break the loop if the input is menu to go back to previous menu
                break
            # call the get_currency function to retrieve the user input price
            user_currency_type = get_currency_type(user_suburb)

            if not user_currency_type or user_currency_type.lower() == 'menu':
                # to go back to previous menu
                os.system('cls')
                continue
            else:
                # calls the prop_val_distribution function to create an histogram
                data_visual_obj.prop_val_distribution(
                    dframe, user_suburb, user_currency_type)
                break

        except ValueError as e:
            # error handling if error occurs
            os.system('cls')
            print(f"\n {e}")
        except KeyboardInterrupt:
            os.system('cls')
            break


def find_property_prices_5(dframe, data_visual_obj):
    """
    This function is used to check if a specific price property is present in a suburb by taking suburb and target
    price as a input from the user. It displays a message if the property is found for the specific price. 

    Args:
        dframe (pd.DataFrame):  takes dataframe of a csv data file.
        data_visual_obj (DataVisualiser):  takes object of DataVisualiser class

    Returns:
        None
    """
    while True:
        try:
            print("\n  ------------------------")
            print(" | Find property prices : |")
            print("  ------------------------")
            print("\n [Type 'menu' to go back]")
            # takes suburb as a input from user
            user_suburb = input("\n Enter your suburb: ")
            # validates the string
            ValidateRequest.validate_string(user_suburb)
            os.system('cls')
            if user_suburb.lower() == 'menu':
                # break the loop if the input is menu to go back to previous menu
                break
            user_target_currency = get_target_currency(user_suburb)
            if not user_target_currency or int(user_target_currency) == 0:
                # go back to previous menu if input 0
                os.system('cls')
                continue
            else:
                # call the class function to identify if the price is present or not
                check_if_present = data_visual_obj.locate_price(
                    user_target_currency, dframe, user_suburb)
                os.system('cls')
                # display a message based on boolean value
                if check_if_present:
                    print(
                        f"\n Property found : expected property price :- {user_target_currency} is present in given data")

                else:
                    print(
                        f"\n Sorry ! Target property price {user_target_currency} not found")
                break

        except ValueError as e:
            # error handling if error occurs
            os.system('cls')
            print(f"\n {e}")
        except KeyboardInterrupt:
            os.system('cls')
            break


def load_csv_file(simple_data_obj):
    """
    This function is used to load the csv file and handle any errors if occurs. 
    This function checks if the file is present or not and if it is not present 
    then it displays a error message and asks the user to re add the file and continue.

    Args:
        simple_data_obj (SimpleDataAnalyser): takes dataframe of a csv data file.

    Returns:
        pd.DataFrame: returns a dataframe of the csv file data.
    """

    dframe = pd.DataFrame()
    try:
        filePath = os.path.join('property_information.csv')
        # run the loop until it finds the file
        while not os.path.isfile(filePath):
            os.system('cls')
            try:
                # display message if file does not exist
                print(f"\n Error: File {filePath} does not exist")
                print(
                    f" File location should be : Property-Investment-Analysis/{filePath}")
                print(
                    "\n Press Enter to continue after you have added the file or '0' to exit.")
                user_option = input("\n Enter you choice : ")
                if user_option == '0':
                    # exits the program if inputs 0
                    return dframe
            except KeyboardInterrupt:
                return dframe
        # return the dataframe
        return simple_data_obj.extract_property_info(filePath)
    except ValueError as e:
        os.system('cls')
        print(f"\n {e}")
        return dframe
    except KeyboardInterrupt:
        os.system('cls')
        return dframe


def main():
    """
    This is the main function that runs the property investment analyser.
    It basically runs each function from above based on the user choice

    Returns:
    None
    """
    os.system('cls')
    # create class objects
    investor_obj = Investor()
    simple_data_obj = SimpleDataAnalyser()
    data_visual_obj = DataVisualiser()
    dframe = load_csv_file(simple_data_obj)
    if dframe.empty:
        # exit program if entered 0
        return
    while True:
        try:
            # run the loops until user exits the program
            investor_obj.main_menu()
            # get the user input chocice
            choice = investor_obj.choice
            os.system('cls')
            if choice == 1:
                # calls the suburb summary function to display the summary
                show_suburb_summary_1(dframe, simple_data_obj)

            elif choice == 2:
                # calls the function to display avg land size
                determine_avg_land_size_2(dframe, simple_data_obj)

            elif choice == 3:
                # calls the function to get property distribution
                calculate_property_val_dist_3(dframe, data_visual_obj)

            elif choice == 4:
                # calls the function using obj to get the sales trends
                data_visual_obj.sales_trend(dframe)

            elif choice == 5:
                # calls the function to check the property prices exist or not
                find_property_prices_5(dframe, data_visual_obj)
            else:
                # exit the program
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
