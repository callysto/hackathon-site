import pandas as pd #importing the pandas library
url = 'https://raw.githubusercontent.com/callysto/data-files/main/Science/Climatograph/climatograph-weather-and-precipitation.csv'
weather = pd.read_csv(url) #the data from the url is read into the weather variable
weather = weather.drop(["Unnamed: 0"], axis=1) #drop unnecessary column

weather["Location"].unique() #List of all territories that we can look into

temperature = weather[weather["Type"] == "temperature"] #filter data for temperatures and assign to temperature variable

alberta = temperature.loc[temperature["Location"] == "AB"] #filter alberta as the region of focus

print("June",alberta["Jun"].median()) #calculate and print the average temperature value for June
print("August",alberta["Aug"].median()) #calculate and print the average temperature value for August
