import pandas as pd #importing the pandas library
url = 'https://raw.githubusercontent.com/callysto/data-files/main/Science/Climatograph/world-bank-climate-data-canada.csv'
weather = pd.read_csv(url) #the data from the url is read into the weather variable

precipitation = weather[weather["Type"] == "precipitation"] #filter data for precipitation and assign to precipitation variable

print("June",precipitation["Jun"].mean()) #calculate and print the average precipitation value for June
print("August",precipitation["Aug"].mean()) #calculate and print the average precipitation value for August
