import pandas as pd #importing the pandas library
url = 'https://raw.githubusercontent.com/callysto/data-files/main/Science/Climatograph/climatograph-weather-and-precipitation.csv'
weather = pd.read_csv(url) #the data from the url is read into the weather variable
weather = weather.drop(["Unnamed: 0"], axis=1) #drop unnecessary column

weather["Location"].unique() #List of all territories that we can look into

precipitation = weather[weather["Type"] == "precipitation"] #filter data for precipitation and assign to precipitation variable

alberta = precipitation.loc[precipitation["Location"] == "AB"] #filter alberta as the region of focus

print("June",alberta["Jun"].mean()) #calculate and print the average precipitation value for June
print("August",alberta["Aug"].mean()) #calculate and print the average precipitation value for August