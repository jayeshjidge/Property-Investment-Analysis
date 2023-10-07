from simple_data_analyser import SimpleDataAnalyser
import os,time

class Inverstor:
    def __init__(self):
        self.choice = None

    def print_menu(self):
        print("1. Load Property Data")
        print("2. Display Property Information")
        print("3. Visualize Data")
        print("4. Exit")
        
    def exit_system(self):
        os.system('cls')
        print("\n Exiting Advisor System...")
        time.sleep(1)
        os.system('cls')

    def main_menu(self):
        while True:
            print("\n  -----------------------------")
            print(" | Property Investment Analyser |")
            print("  -----------------------------")
            self.print_menu()
            try:
                choice = input("\n Enter your choice: ")
                if choice.isdigit():
                    choice = int(choice)
                else:
                    raise ValueError("\n Invalid Input type. please enter correct input")
                
                if choice == 1:
                    pass

                elif choice == 2:
                    pass

                elif choice == 3:
                    pass

                elif choice == 4:
                    self.exit_system()
                    break
                else:
                    raise ValueError(f"\n Incorrect Choice {choice} : Does not exist ! Please select choice from Menu")
                self.choice = choice
                break
            except ValueError as e:
                os.system('cls')
                print(e)
            except KeyboardInterrupt:
                os.system('cls')
                break
