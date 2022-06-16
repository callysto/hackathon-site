import pandas as pd #importing the pandas library
url = 'https://raw.githubusercontent.com/callysto/data-files/main/Science/Climatograph/world-bank-climate-data-canada.csv'
weather = pd.read_csv(url) #the data from the url is read into the weather variable
weather