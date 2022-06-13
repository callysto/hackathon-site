import pandas as pd #importing the pandas library
url = 'https://raw.githubusercontent.com/callysto/data-files/main/Science/Climatograph/world-bank-climate-data-canada.csv'
weather = pd.read_csv(url) #the data from the url is read into the weather variable

temperature = weather[weather["Type"] == "temperature"] #filter data for temperatures and assign to temperature variable

print("June",temperature["Jun"].mean()) #calculate and print the average temperature value for June
print("August",temperature["Aug"].mean()) #calculate and print the average temperature value for August
