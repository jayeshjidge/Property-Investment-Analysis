import pandas as pd
import os
    
class SimpleDataAnalyser:
    
    def extract_property_info(self,file_path: str) :
        handleError = None
        try:
            if not file_path:
                raise ValueError("Error: File path cannot be empty")
            
            if isinstance(file_path, int):
                raise ValueError("Error: File path cannot be an integer")
            if not os.path.isfile(file_path):
                raise ValueError(f"Error: File '{file_path}' does not exist")
            
            csv_data = pd.read_csv(file_path)
            return csv_data
            
        except ValueError as e:
            print(e)
            return pd.DataFrame() 
        except KeyboardInterrupt:
            os.system('cls')




# obj = SimpleDataAnalyser()
# filePath = os.path.join('property_information.csv')
# check = obj.extract_property_info(filePath)
