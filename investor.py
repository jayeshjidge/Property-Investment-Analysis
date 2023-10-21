import os,time

class Investor:
    def __init__(self):
        self.choice = None

    @staticmethod
    def print_menu():
        print("\n 1. Get summary of your suburb \n")
        print(" 2. Check average land size \n")
        print(" 3. Visualize data of your suburb with histogram\n")
        print(" 4. Get sales trend analysis through line chart\n")
        print(" 5. Find Property prices\n")
        print(" 6. Exit")
        
    @staticmethod    
    def exit_system():
        os.system('cls')
        print("\n  ---------------------------")
        print(" | Exiting Advisor System... |")
        print("  ---------------------------")
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

