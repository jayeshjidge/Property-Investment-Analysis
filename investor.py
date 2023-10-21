import os,time

class Investor:
    def __init__(self):
        self.choice = None

    @staticmethod
    def print_menu():
        print(" 1. Get summary of your suburb")
        print(" 2. Display Property Information")
        print(" 3. Visualize Data")
        print(" 4. Exit")
        
    @staticmethod    
    def exit_system():
        os.system('cls')
        print("\n Exiting Advisor System...")
        time.sleep(1)
        os.system('cls')
        
   
    def main_menu(self):
        # while True:
            self.choice = None
            # os.system('cls')
            print("\n  -----------------------------------------")
            print(" | Welcome to Property Investment Analyser |")
            print("  -----------------------------------------")
            self.print_menu()
            # try:
            choice = input("\n Enter your choice: ")
            if choice.isdigit():
                choice = int(choice)
            else:
                raise ValueError("\n Invalid Input type. please enter correct input")
                
            if 1 <= choice <= 4:
                self.choice = choice
            else:
                raise ValueError(f"\n Incorrect Choice {choice} : Does not exist ! Please select choice from Menu")
                # break
            # except ValueError as e:
            #     os.system('cls')
            #     print(e)
            # except KeyboardInterrupt:
            #     os.system('cls')
            #     break
