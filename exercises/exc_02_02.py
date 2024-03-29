import pandas as pd #importing the pandas library
url = 'https://raw.githubusercontent.com/callysto/data-files/main/Science/Climatograph/world-bank-climate-data-canada-abbreviated.csv'
weather = pd.read_csv(url) #the data from the url is read into the weather variable

print(weather["Abbreviated"].unique()) #List of all territories that we can look into

temperature = weather[weather["Type"] == "temperature"] #filter data for temperatures and assign to temperature variable

province = temperature.loc[temperature["Abbreviated"] == "AB"] #filter Alberta as the region of focus

print("June",province["Jun"].median(), "°C") #calculate and print the average temperature value for June

print("August",province["Aug"].median(), "°C") #calculate and print the average temperature value for August