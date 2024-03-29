import pandas as pd #importing the pandas library
url = 'https://raw.githubusercontent.com/callysto/data-files/main/Science/Climatograph/world-bank-climate-data-canada-abbreviated.csv'
weather = pd.read_csv(url) #the data from the url is read into the weather variable

print(weather["Abbreviated"].unique()) #List of all territories that we can look into

precipitation = weather[weather["Type"] == "precipitation"] #filter data for precipitation and assign to precipitation variable

province = precipitation.loc[precipitation["Abbreviated"] == "AB"] #filter Alberta as the region of focus

print("June",province["Jun"].mean(), "mm") #calculate and print the average precipitation value for June
print("August",province["Aug"].mean(), "mm") #calculate and print the average precipitation value for August