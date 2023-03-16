# importing panda library
import pandas as pd
  
# readinag given csv file
# and creating dataframe
dataframe1 = pd.read_csv("output.txt")
  
# storing this dataframe in a csv file
dataframe1.to_csv('book4.xlsx', 
                  index = None)