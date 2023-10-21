
from investor import Investor
from simple_data_analyser import SimpleDataAnalyser
import os
from validate_data import ValidateRequest


def show_user_summary(dframe, simple_data_obj):
    os.system('cls')
    while True:
        try:
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


def main():
    os.system('cls')
    filePath = os.path.join('property_information.csv')
    investor_obj = Investor()
    simple_data_obj = SimpleDataAnalyser()
    try:
                dframe = simple_data_obj.extract_property_info(filePath)
                while True:
                    try:
                        investor_obj.main_menu()
                        choice = investor_obj.choice
                        if choice == 1:
                            show_user_summary(dframe, simple_data_obj)
                    except ValueError as e:
                        os.system('cls')
                        print(f"\n{e}")
                    except KeyboardInterrupt:
                        os.system('cls')
                        break

    except ValueError as e:
                os.system('cls')
                print(f"\n{e}")
    except KeyboardInterrupt:
                os.system('cls')


if __name__ == '__main__':
    main()
