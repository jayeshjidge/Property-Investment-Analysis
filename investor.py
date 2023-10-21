import os,time

class Investor:
    def __init__(self):
        self.choice = None

    @staticmethod
    def print_menu():
        print(" 1. Get summary of your suburb")
        print(" 2. Check average land size")
        print(" 3. Visualize data of your suburb with histogram")
        print(" 4. Get sales trend analysis through line chart")
        print(" 5. find Property prices")
        print(" 6. Exit")
        
    @staticmethod    
    def exit_system():
        os.system('cls')
        print("\n Exiting Advisor System...")
        time.sleep(1)
        os.system('cls')
        
   
    def main_menu(self):
            self.choice = None
            print("\n  -----------------------------------------")
            print(" | Welcome to Property Investment Analyzer |")
            print("  -----------------------------------------")
            self.print_menu()
            choice = input("\n Enter your choice: ")
            if choice.isdigit():
                choice = int(choice)
            else:
                raise ValueError("Invalid Input type. please enter correct input")
                
            if 1 <= choice <= 6:
                self.choice = choice
            else:
                raise ValueError(f"Incorrect Choice {choice} : Does not exist ! Please select choice from Menu")

