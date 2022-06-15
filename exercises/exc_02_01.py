import pandas as pd #importing the pandas library
url = 'https://raw.githubusercontent.com/callysto/data-files/main/Science/Climatograph/climatograph-weather-and-precipitation.csv'
weather = pd.read_csv(url) #the data from the url is read into the weather variable
weather = weather.drop(["Unnamed: 0"], axis=1)
print(weather)